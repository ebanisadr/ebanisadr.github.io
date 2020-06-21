---
layout: post
date: May 23, 2020
title: Building this blog with Jekyll
---

I started using Jekyll in high school for a blog that I needed for a class
project. I had a number of complaints about it, namely that the syntax to do
anything complicated is nearly unintelligible to me, so I naturally decided to
leave Jekyll behind for my new blog. I looked into other <abbr title="Static
Site Generators">SSGs</abbr>, but Hugo and Gatsby didn't seem like they had what
I wanted either. So I set out to build my own.

I managed to make [a simple SSG in 186 lines of
Javascript](https://gist.github.com/ebanisadr/891f686ffbc09947bbcbfc0270c7225b),
split across two files. I was pretty happy with myself, because I liked knowing
exactly what my code was doing but I quickly realized that I had two problems.

1. Processing files one at a time meant that I couldn't auto-generate index
   files, lists of posts, or pages.
2. I had used my existing knowledge of Jekyll as a base for the design of post
   metadata (YAML frontmatter) and sitewide configuration variables. I realized
   my time would have been better spent simply learning to use Jekyll more
   effectively.

Realizing that I need not reinvent the wheel, I migrated my budding blog to
Jekyll (which was really easy because I was already using a pretty similar
format). I chose not to use a theme at all, because I want a site that is
uniquely mine. Instead, I went for the old fashioned HTML-and-CSS route,
inspired by
[bettermotherfuckingwebsite.com](http://bettermotherfuckingwebsite.com) and its
ilk.

I started with a very nice drop in stylesheet called
[Water.css](https://watercss.netlify.app), and did some updating to make it
better suit a blog. I also added a few classes for use on some pages, but the
styles on this site are still mostly classless.

Next, I used [Adobe Color](https://color.adobe.com) to pick new theme colors
that I like a bit better than the Water.css defaults.

Since I'm working in HTML, I also wrote each of the index pages by hand. The
landing page with my face on it is based on [the Coder theme for
Hugo](https://github.com/luizdepra/hugo-coder/), my about page is laid out as a
post and the everything else page is a table under the hood. Pages that have a
list of posts, like `/blog` use Jekyll's liquid templating features to enumerate
and filter posts at build time.

For analytics I decided on [Goat Counter](https://www.goatcounter.com), a
barebones analytics script that's pretty privacy friendly.

Since I have yet to need any fancy Jekyll plugins or features, I'm able to use
GitHub pages to host this site super easily. I don't even have to build it
locally, just push to the `master` branch of [the repository for this
site](https://github.com/ebanisadr/ebanisadr.github.io).

After getting everything up and running, I realized that Google Fonts was the
main bottleneck for my site's initial loading performance, so I decided to
selfhost the two fonts I use too.

So far, I have yet to encounter any problems with this setup, but I also haven't
started on some of the more advanced features that I might want, like tagging
and pagination (which I understand are possible to implement with Jekyll, but
might require me building the site locally).
