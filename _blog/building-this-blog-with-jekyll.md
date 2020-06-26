---
layout: post
date: June 21, 2020
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
selfhost the two fonts I use too. This turned out to be slightly more
complicated than I expected, but there's a really good [guide on selfhosting
fonts](https://www.tunetheweb.com/blog/should-you-self-host-google-fonts/) on
_Tune The Web_. After deciding I wanted to use [Inter](https://rsms.me/inter/)
for this site's body, I got suckered in to the alternate numbers (with a flat
upper line on the 3 instead of a curly one). I only wanted that option, so I
tried to use FontSquirrel's webfont generator to flatten it into the main font,
but that feature seemed broken when I tried it.  I ended up editing the font
myself using [FontForge](https://fontforge.org/en-US/) and using the [FontTools
Python Library](https://github.com/fonttools/fonttools) to subset the modified
font with the Unicode range Google fonts uses for Latin: `U+0000-00FF, U+0131,
U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC,
U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD`. Then I used
[Transfonter](https://transfonter.org) to generate the CSS `@font-face` rules to
make everything work together. Finally, I added [preload
links](https://developer.mozilla.org/en-US/docs/Web/HTML/Preloading_content) to
the fonts that are used on the index page in the HTML head. Now I only have a
limited glyph set, but I'm not sure it's a problem. I did cut about a quarter of
a second off my initial load time, though.


So far, I have yet to encounter any problems with this setup, but I also haven't
started on some of the more advanced features that I might want, like tagging
and pagination (which I understand are possible to implement with Jekyll, but
might require me building the site locally).

The full [source of this
website](https://github.com/ebanisadr/ebanisadr.github.io) is available on
GitHub. I still have a few things to implement, though, like SEO tagging, a
favicon, breadcrumb links on pages, and some more posts.

