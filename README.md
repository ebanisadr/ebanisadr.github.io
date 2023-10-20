# ericbanisadr.com

Hi, welcome to my website's repo. If you're reading this on GitHub for some
reason please make an issue/PR or otherwise reach out if you're interesting in
anything that's  going on at [ericbanisadr.com](https://ericbanisadr.com).

Otherwise, this repo is mostly just me.

## Developer-facing docs (_i.e._ notes to self)

I first made this website with the idea that using mostly  basic HTML/CSS would
prove durable and more maintainable than trying to keep pace with the frontend
flavor of the month. This has certainly proved true with a major caveat: I wish
I had used CSS closer to its original design; cascading from less specific
stylesheets to more specific ones.

Part of the problem was the fact that making something new is a fundamentally
different task than keeping anything current. Half a decade  after the creation
of this website I'm finding out that the classless idea that I initially went
for was a bit misguided. It relies too heavily on nested selectors, which work
perfectly to avoid second-order effects of changes, but doesn't make
maintenance easy.

As I start to become more active in updating this site, I'd like to move toward
a more _✨cascading✨_ approach, where ideas bubble into the top-level
stylesheet.  The vision is that, when I'm making a new page, I can use a
`<style>` tag, possibly in combination with an element type and class name, to
style things for that particular piece of content. Once I find myself wanting to
copy-paste a selector/rule set from another page, say `article p.caption` (which
might soon be an addition) then I'll move it into the site-wide stylesheet.
Hopefully this will allow me to maintain a consistent visual style across the
site without compromising my ability to hack together some specific
functionality for a new page.

Thanks to modern web inspectors, I'm imagining a workflow like:
1. Design how I want the content to look
1. Write it as HTML (or Markdown when possible)
1. Render it and see what happens
1. Fix it using a `<style>` element and semantic class names
1. Run `rg <classname>` and see if I can standardize

Further, I hope to continue using hyphenated custom elements as pseudo
components, keeping their CSS and inner HTML structure in sync due to the copy-paste
bent inherent in the idea of components.
