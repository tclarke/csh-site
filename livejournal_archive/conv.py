#!/usr/bin/env python3
#
# Post-process output from https://github.com/arty-name/livejournal-export for inclusion in jekyll blogs

from datetime import datetime
import os
import os.path
import sys

if len(sys.argv) != 4:
    print("{} <path to posts-markdown> <path to comments-markdown> <patch to _posts>".format(sys.argv[0]))
    sys.exit(-1)

def load_parts(f):
    meta = {}
    body = ""
    in_meta = True
    for line in f.readlines():
        if in_meta:
            if line.strip() == '':
                in_meta = False
            else:
                parts = line.split(':')
                if len(parts) > 2:
                    parts = parts[0], ":".join(parts[1:])
                parts = list(map(lambda s: s.strip(), parts))
                if len(parts) != 2:
                    raise UserWarning("ERROR GETTING METADATA! {}".format(parts))
                else:
                    meta[parts[0]] = parts[1]
        else:
            if line.strip() == '':
                body += '\n\n'
            else:
                body += line
    return meta,body

for root, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        oname = os.path.relpath(os.path.join(root, fname), sys.argv[1])
        f = open(os.path.join(root, fname))
        meta, body = load_parts(f)
        if 'categories' in meta:
            raise UserWarning("Found categories!")
        if 'date' not in meta:
            raise UserWarning("No date found!")
        if 'title' not in meta:
            raise UserWarning("No title found!")
        if 'slug' in meta:
            meta['lj_slug'] = meta['slug']
            del meta['slug']
        if 'id' in meta:
            meta['lj_id'] = meta['id']
            del meta['id']
        try:
            f = open(os.path.join(sys.argv[2], meta['lj_slug']+".md"))
            body += '\n<div id="comments"><h4>Comments:</h4><div class="lj-comments">{}</div></div>\n'.format(f.read())
        except FileNotFoundError:
            pass  # no comments for this post
        meta['title'] = meta['title'].replace(':', '&colon;')
        post_date = datetime.strptime(meta['date'], '%Y-%m-%d %H:%M:%S')
        new_name = os.path.join(sys.argv[3], "{:02d}-{:02d}-{:02d}-{}.md".format(post_date.year, post_date.month, post_date.day, meta['lj_slug']))
        print("{} -> {}".format(oname, new_name))
        f2 = open(new_name, 'w')
        f2.write("---\nlayout: post\ncategories: livejournal\n")
        for k, v in meta.items():
            f2.write("{}: {}\n".format(k, v))
        f2.write("---\n")
        f2.write(body.replace("\n\n", "\n\n\n"))
        f2.close()
