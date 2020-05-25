---
layout: post
title: Writing my own static site generator for this blog
date: May 23, 2020
---

Before this blog, I had a website that was also hosted on GitHub Pages, but it was generated with Jekyll. I didn't use it very often, and it didn't achieve the level of simplicity I hoped for. When I was recently inspired to update my website, I decided to start from scratch, leading to the creation of this site.

## Motivation

Why I decided to start my website from scratch.

- I believe nearly everyone in most computing-related fields could benefit from having their own website.
- Server-side rendering. Code blocks (and math equations if necessary) are rendered at compile time, removing client-side dependencies.
- Inteligibility. Sites like motherfuckingwebsite.com and bettermotherfuckingwebsite.com have impressed the importance of not over-complicating the web on me. Additionally the [Water.css stylesheet](https://watercss.netlify.app) proves that a lot can be done without fancy frameworks or tools.
- To learn. Anyone can make a WordPress site, but I think it worth learning how to make something a little bit lighter and more secure.

## Starting out

I started by copying [Water.css](https://watercss.netlify.app) and adapting it with colors that I picked using the [Adobe color website](https://color.adobe.com/). I wrote a quick script to compile markdown with [markdown-it](https://github.com/markdown-it/markdown-it) and started trying to make a functional site.

I quickly realized that hardcoding everything was a good way to have different headers on different pages, so I realized I needed to implement a templating system. Many good ones exist, but I chose to use [mustache.js](http://mustache.github.io). To decide which template to use for each file, I borrowed from Jekyll's idea of using YAML frontmatter, so I updated my compile script to pick a template based on the YAML frontmatter of a page, then render the template using the compiled markdown.

In the process of adding templates, I used another of Jekyll's ideas---a site configuration file that stores sitewide variables. I knew that I would want to switch to `https` later on, so I extracted the base URL for my site (`http://ericbanisadr.com/`) into a variable, so I could add the `s` later.

## Build system

Right now, I have a content folder that houses the source for everything on the site. The content is processed, one file at a time, then the rendered version is output to a staging folder, keeping the same directory structure. I chose this approach because it allows me to co-locate related files. For example, an image and a blog post can be stored together in `content/blog/example-post` as `index.md` and `post-image.jpg`, or posts can be stored as individual markdown files like `content/blog/example-post.md`. In both cases, the post would be accessible at `/blog/example-post`

To implement this, I needed a place to store all my templates and build scripts, so I decided to create a [second GitHub repository with the source of my website](https://github.com/ebanisadr/website). In it, I put [the script to compile an individual file](https://github.com/ebanisadr/website/blob/master/compile-markdown.js), and [the script to build the whole site](https://github.com/ebanisadr/website/blob/master/build-site.js).

They combine for a total of 152 lines of JavaScript, which is pretty good for a home-grown static site generator.

## Enabling HTTPS

Apparently it's as simple as checking the box in the GitHub Pages settings now. Not that a static site really needs an encrypted connection, but it does look professional.

## Conclusion

I have a generally working website after a few days' work, and I'm happy with it. I basically just re-implemented Jekyll in the end, so maybe my time would've been better spent learning Jekyll, but I'm happy that my site is simple enough that the HTML, CSS, and generator are all human-readable because that means I'll have an easy time maintaining them in the future.

Check out the [source of this site](https://github.com/ebanisadr/website), and feel free to use any part of it you like.

