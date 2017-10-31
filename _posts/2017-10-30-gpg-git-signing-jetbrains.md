---
layout: post
title:  "GPG Git Signing with Jetbrains IDEs"
date:   2017-10-30 14:44:00
categories: ["git", "development", "security"]
---
Git has a great feature to prevent fraudulent commits, especially in public repositories.
You can signed a commit with a PGP compatible tool (GnuPG is probably the most common).
This is great when you're using the command line tools, just do a `git commit -s` and you're good to go.

If you're like a lareg number of developers, you're using an IDE of some sort for your heavy coding days.
I'm a particular fan of the various Jetbrains IDEs: PyCharm, WebStorm, RubyMine, etc.
There's a pretty full featured git integration available for all of these and while I still use the command line somewhat often, it's nice to be able to hit `⌘k` and commit from the IDE.
There's currently no option to sign a particular commit from the IDE (there's Sign-Off but that just adds a line to the commit message).
However, you can set things up to sign all of your commits, but there are a couple of gotchas.
Here's a quick walkthrough of the process.

* Install GnuPG. Ok, this is more of a pre-requisite, so it's up to you to do this one your own.

* Create a key for signing. There are lots of tutorials on this process, so again, left as an exercise for the reader. Note your key ID, you can get it with:
{% highlight bash %}
> gpg --list-secret-keys --keyid-format LONG
...
ssb   rsa2048/0F40BD647EFF33D6 2017-10-12 [S] [expires: 2021-10-12]
{% endhighlight %}
That `0F40BD647EFF33D6` is your key ID.

* Configure git to allow signing. Use `git --global --add commit.gpgsign true`, etc. to configure the following, with your values substituted.
{% highlight bash %}
> git config --global --list
user.name=Trevor R.H. Clarke
user.email=tclarke@ball.com
user.signingkey=0F40BD647EFF33D6
commit.gpgsign=true
{% endhighlight %}

* Configure GnuPG to use a graphical agent to prompt for passwords. This goes in your `~/.gnupg/pgp.conf` file which probably lives in a slightly different location on Windows.
{% highlight bash %}
no-tty
use-agent
{% endhighlight %}

* Commit a change in your IDE. I always select the Sign-Off option as well. You should be prompted for your GnuPG password. Once you've committed, you can double check that it worked with the command line.
This example shows a commit without a signature and one with a signature.
{% highlight bash %}
> git log --show-signature -1 -2
commit 54c9c211cb478c91d2ecf8e11a31ceaccb7ea179
gpg: Signature made Mon Oct 30 14:39:21 2017 EDT
gpg:                using RSA key F7B6A5FC5C46CAC13B221E920F40BD647EFF33D6
gpg: Good signature from "Trevor R.H. Clarke (Computer Science House default) <retrev@csh.rit.edu>" [ultimate]
gpg:                 aka "Trevor R.H. Clarke <trevor@notcows.com>" [ultimate]
gpg:                 aka "Trevor R.H. Clarke <tclarke@ball.com>" [ultimate]
gpg:                 aka "Trevor R.H. Clarke <pythonpimp@gmail.com>" [ultimate]
Author: Trevor R.H. Clarke <tclarke@ball.com>
Date:   Mon Oct 30 14:39:21 2017 -0400

    Working minus orientation.
    
    Signed-off-by: Trevor R.H. Clarke <tclarke@ball.com>

commit 611d5aa25d0326a8db68715036232d3a5bfd5615
Author: Trevor R.H. Clarke <tclarke@ball.com>
Date:   Fri Oct 27 12:23:44 2017 -0400

    Added Rakefile and restructure dir structure
{% endhighlight %}
