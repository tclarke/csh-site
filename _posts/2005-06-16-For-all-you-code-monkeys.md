---
layout: post
categories: livejournal
title: For all you code monkeys
date: 2005-06-16 19:00:58
lj_slug: For-all-you-code-monkeys
lj_id: 196512
---
Calculates a list of all fibonnacci numbers starting with a,b that are less than stop.



    >>> fib = lambda a,b,stop: (a+b < stop) and [a]+fib(b,a+b,stop) or [a,b]  
    >>> fib(1,1,50)  
    [1, 1, 2, 3, 5, 8, 13, 21, 34]



Calculates all fibonnacci numbers starting with a,b. The blist function is converts the result into a fixed length list.



    >>> blist = lambda obj,n: (n > 0) and [obj.next()]+blist(obj,n-1) or []  
    >>> def fib(a,b:)  
    ...        yield a  
    ...        while 1:  
    ...              yield b  
    ...              a,b=b,b+a  
    >>> f=fib(1,1)  
    >>> blist(f,10)  
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]  
    >>> blist(f,10)  
    [89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


<div id="comments"><h4>Comments:</h4><div class="lj-comments"><ul>
<li><h3>tekmagika: </h3>
<a id="comment-440"></a>
<p><img src="http://pics.livejournal.com/tekmagika/pic/0009r3qq"></p>
</li>
</ul></div></div>
