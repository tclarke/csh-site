---
layout: post
categories: livejournal
title: stupid windows
date: 2001-06-26 23:58:54
lj_slug: stupid-windows
lj_id: 18614
---
So, I tried to insdtall XOSL on my win98 machine. I've done this before and it worked fine. However, this time, the machine never rebooted...hung when it was time to boot from the drive. I tried booting a 98 rescue disk figuring I could run the xosl uninstaller. I couldn't access the drive...either the recuse disk didn't know about fat32 or didn't know about my RAID controller (unlikely cause the BIOS should be handling it here). Anyway, I tried to rebuild the MBR when I got the drive to be recognized, but not the filesystem. Now, the RAID BIOS utility thinks I have 2 independant drives instead of a stripe set...and, of course, I don't have a backup yet (no SCSI card for my tape drive). I emailed highpoint support, hopefully there is a way to rebuild the stripe set.  



Right now, I'm using QNX on a third drive so I at least have some net access, etc.  



Anyone know how to rebuild a stripe set on an HPT Ultra/100 RAID system? I think only the very beginning of the drives got overwritten (first 63 bytes probably).....YARG!!!


<div id="comments"><h4>Comments:</h4><div class="lj-comments"><ul>
<li><h3>bits: </h3>
<a id="comment-11"></a>
<p>Is it the HPT370?<br>
<br>
I've used the HPT370 on my ABIT VP6 in a mirror configuration.  Even though it's BIOS configurable, both drives showed up in Win98 until I installed the drivers for HPT controller.<br>
<br>
It dogged the performance of the system under Win98 when swapping. Especially when I was editing video.  Better performance with it off. <br>
<br>
Under linux, they still acted as independent drives. It did boot fine, but not until after I upgraded to kernel 2.4.1. Decided to stop using the RAID until I got more memory in the system and could shut off swap, so I never got around to looking at the proper linux configuration. </p>
</li>
<li><h3>retrev: </h3>
<a id="comment-12"></a>
<p>That's the one. The problem I have now, is that the HPT BIOS no longer sees the drives as a set. They must store information about the set, etc. that a drive is in at the beginning of the disk and this got overwritten by a stupid win98 (w/o the HPT drivers running). If I tell it to create a set, the last step is to "prepare the set". This may just rebuild a bad set but I'm not willing to make a leap of faith so I'm waiting to hear from highpoint tech support. BTW, I usually don't run out of RAM and when I do need to swap, I use an 800mb IDE drive that is not on the HPT. Up until now, I've had no complaints with the system and this is not the fault of the RAID controller. It would be nice to have QNX drivers for the HPT tho....I believe there are NetBSD drivers for the controller and it should be trivial to modify RAIDframe to support stripping with the controller. Maybe I'll work on that if I have to scrub the drives...:(</p>
</li>
</ul></div></div>
