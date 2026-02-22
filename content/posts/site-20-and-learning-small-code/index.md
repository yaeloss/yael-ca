---
title: "Site 2.0 and Learning Small Code"
date: 2013-06-23
tags: 
  - "blog"
  - "coding"
  - "css"
  - "opml"
  - "river2"
  - "rss"
---

It only took me a few days of background work, but I’ve completed the re-design of the pages I use to represent myself on the net:

- [yael.ca](http://yael.ca)
- [blog.yael.ca](http://blog.yael.ca)
- [news.yael.ca](http://news.yael.ca)
- [linkblog.yael.ca](http://linkblog.yael.ca)

My [intro page](http://yael.ca) has been set up as a _bonjour_, welcoming readers, breaking down my affiliations, linking my other web sites, and displaying a short biography.

The page is built with [basic bootstrap CSS](http://twitter.github.io/bootstrap/), using small pieces of javascript to make the output clean and effective. I’ve also embedded a java version of my [Linkblog](http://linkblog.yael.ca), in order to show people articles and videos I’m linking to and reading.

The resulting [RSS feed](https://s3.amazonaws.com/im.yael.ca/linkblog.xml) is how I push out most of my information.

Elsewhere on the page, I have links to this blog, some of the articles I’ve written in the past, my [Podcast RSS feed](http://libertyinexile.jellycast.com/podcast/feed/2), and my professional connections.

> ![image](images/tumblr_inline_mova30TPnd1qz4rgp.jpg)

The template is one of the most basic out there, but it makes a very effective presentation–at least that’s what my biased sense tells me. The entire page is run out of Amazon’s S3 service, so it’s very reliable.

Next is [this blog](http://blog.yael.ca), which you’re hopefully reading as of this moment. It still runs on Tumblr, which offers a lot of freedom to customize different themes, and is pretty well receptive to embedding content.

The downside, unfortunately, is that I have to share servers with the same people who publish thousands of cat GIFs per hour, meaning they’re prone to breakdown at peak hours (damn those hipsters).

While the header picture is simple enough, the coolest part is the added menu bar. This bar, easily made with OPML code, connects all of my sites together and provides a central location for my Internet identity. It links to my _bonjour_ page, news river, email, Twitter page, and Liberty In Exile. It can easily be turned off by clicking the blue wedge.

I’m still working on the font and spacing of the posts, but visually everything is pretty well set out.

Now the [news river site](http://news.yael.ca) is where I had to spend most of my coding hours. Granted, I was able to pull a lot of original source code from **Dave Winer**’s [tabbed river page](http://tabs.mediahackers.org), but it remained a daunting task. 

I’m the first to admit I’m nothing but a novice when it comes to tweaking CSS or HTML, but I felt like I accomplished a lot in linking different .js files to display correctly on the page.

I’ve separated my favorite news into different categories, including one for news in French, another for my friends’ websites, and the last one for Podcasts I enjoy. Foreign language accents still hiccup on the page, causing strange coding, but I’m currently looking into this as best I can.

> ![image](images/tumblr_inline_movaixkU6Z1qz4rgp.jpg)

The page has the same menu bar as the _bonjour_ and blog, and links to the same websites. The tabs truly allow me to follow different languages, regions, and subjects all in one design.

Thank you to [**Dave Winer**](http://davewiner.com) for creating the OPML editor and the River2 design in order to make this work and to [**Adam Curry**](http://blog.curry.com) for leading the way.

The [linkblog](http://linkblog.yael.ca) isn’t much different than previously, and there isn’t really much to add, but I hope people will use it as a central RSS feed and a way to understand my brain. So much of what we see on the Internet never really gets mentioned elsewhere, so here’s to trying to map it.

To be clear, I’m no web designer. In fact, most of everything I’ve learned in maintaining websites comes from influential people across the net, who’ve spent countless hours perfecting their craft and unknowingly mentoring the curious wanderers who are just now jumping in.

I hope the site redesigns will be graceful enough for your eyes and the reliability strong enough to be beneficial in the end. Perhaps it will even improve my image on the Internets!

But I could be wrong.
