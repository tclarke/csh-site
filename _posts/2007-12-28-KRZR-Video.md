---
layout: post
categories: livejournal
title: KRZR Video
date: 2007-12-28 21:00:36
lj_slug: KRZR-Video
lj_id: 265253
---
I got a new memory card for my KRZR so I decided to figure out how to encode video so I can put podcasts on it. This is mostly for my reference...anyway, the following seems to work pretty well and generates files that are a reasonable size and quality.  



ffmpeg -y -i infile.mov -s 176x128 -r 15 -vcodec mpeg4 -b 150000 -ar 8000 -ab 4750 -ac 1 outfile.3g2  



Generates an mpeg4/samr file at 176x128x15fps 150kbps with mono audio 8kHz 16bit 4kbs
