---
layout: post
title: On vibecoding products
date: Apr 24, 2026
styles:
---
It's 2026 and AI can write code if only you can tell it what to write. It's [no silver bullet](https://worrydream.com/refs/Brooks_1986_-_No_Silver_Bullet.pdf) for software development but it is a way to develop programs in a higher level language: English. I've been practicing for over a year with the goal of having AI write useful software and I think I'm getting close.

My first few projects were unspectacular. After a while the codebase got too large to fit in a context window and 200-line functions confused the model. My workflow improved, the model improved and the hurdle is gone.

I'm very excited to have figured out how to have AI develop a beautiful and usable UI before implementing database schemas and jumping right in. Before, I relied on a tweak-based workflow:
1. tell the AI to do something
2. look at what it made (which doesn't match the product vision)
3. propose updates, AI iterates on the already-written code

Now, I've inverted the sequence:
1. write the idea in Linear
2. tell the AI to design the interface
3. review the design and propose updates (define the product requirements)
4. implementation (matches the product requirements)

This works because defining the product requirements is one the two main human tasks in my workflow[^other].

<figure>
<img src="{{site.url}}/blog/on-vibecoding-products/storybook-first.png" alt="Eric sending a message to Claude Code: now make a storybook flow with entrypoints and full screens" style="max-width: min(99%, 540px); object-fit: scale-down;" />
<figcaption>Now I can have Claude develop UI before functionality</figcaption>
</figure>

I'm building an app ([Chatatouille, an app+agent for home cooks](https://chatatouille.ai); check it out) and found [Storybook](https://storybook.js.org/) to be pretty good for allowing me to build interface before logic. This helps accelerate my specification process so the AI builds the right thing, on the first try, every time. 

Combining Storybook with the ability to use Linear issues as a human-visible, human-editable memory system lets me ensure tasks are well defined before they're implemented. Claude must be sick of hearing me ask "is this task well specified enough for us to proceed to implementation?"

<figure>
<img src="{{site.url}}/blog/on-vibecoding-products/defining-requirements.png" alt="Storybook and Claude Code side-by-side where Eric asks Claude Code to update the location of the shared grocery list badge to be inside the grocery list card. Inset result where the change is made succesfully." style="max-width: min(99%, 540px); object-fit: scale-down;" />
<figcaption>It's far faster to refine product requirements by critiquing a mock</figcaption>
</figure>

Over a decade ago I became a programmer to make software. Apparently, software is built to satisfy product requirements so I switched my career to product management. Man, am I glad I did because it's now given me the language, mindset and workflows to use AI to build an app I'm already using in my day-to-day life.

I invested two months of development and a year of vibecoding practice to get to this point and it's exhilarating.

---

[^other]: The other is QA, which I may write about eventually. My Pareto improvement here has been to explicitly ask the AI to give me a QA test plan.