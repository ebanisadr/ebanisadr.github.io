---
layout: post
date: May 23, 2020
title: Building this blog with Jekyll
---

Prior to having this website I had a similar blog, also made with Jekyll, hosted
at this domain. I had a number of complaints about it, so I naturally decided to
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


