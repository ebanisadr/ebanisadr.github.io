---
layout: post
title: Impossible outputs
date: May 18, 2025
styles:
---
No chatbot can successfully output all the digits of π. It's obviously impossible for a variety of reasons, not least that π doesn't terminate. So, we can be confident that there are some outputs a chatbot can't produce.

For any finite output, the opposite is true. A "repeat after me" style prompt can almost certainly produce any desired response.[^1] So, it seems AI _can_ produce anything.

More interesting than pure possibility, though, is how effectively the model can incorporate new information that's not directly contained in the user prompt. In some cases the new info comes from the vast amount of information encoded in the model's weights. In others it comes from external sources incorporated via RAG/MCP. In the case of π, at least a couple thousand digits exist somewhere in the model's weights; this can be demonstrated empirically.[^2] To get even more digits of π accurately, one might instruct the model to write and run code that calculates the digits. By writing a prompt that guides the model toward a tool-use process for generating the digits of π we can get a theoretically infinite number of accurate digits.

Well-written prompts allow us to extract more information from GPT+MCP than is encoded in the prompt, or even in the model itself. Such prompts are far more valuable than the trivial case of providing a bunch of digits and asking the model to repeat them because they allow us users to extend our existing knowledge by leveraging the chatbot.

## how much non-input information can we get?

I'm not equipped with the analytical tools to rigorously quantify exactly how many bits or "ideas" worth of non-input information are contained in a given response, but I *can* identify a first principle at play here: more is better. We want chatbots to provide us with information we don't already have.

<figure>
<img src="{{site.url}}/blog/impossible-outputs/ai-value.png" alt="user value = log(output information / user-input information)" style="max-width: min(99%, 540px); border-radius: 1em; object-fit: scale-down;" />
<figcaption>The utility of AI can be measured simply</figcaption>
</figure>

Instead of rigorous analysis, I've been working through this question by example.

* Can I tell a chatbot to write _War and Peace_? *Yes.*
- Will it? *No.*[^3]
- It certainly can't (yet...?) write a novel of equivalent quality.

I guess it's reassuring that the human condition can't yet be represented in a matrix of model weights. (Maybe that's simply because we haven't figured out how to write it down in its entirety so we can train on it, though 😅.) Let's call _War and Peace_ our upper boundary.

We can also lower bound the amount of novel information produced in response to a well-written prompt. If you ask Cursor to write a simple web app, it will produce a lot of information beyond what you provide. It might generate a sensible interface, a color palette and a bunch of CSS, even without specific direction to do so from the user. Let's call "a lot" our lower boundary.

Now we can start to answer the question of possibility, in a practical sense. Models can clearly integrate a significant amount of information to the point of being quite useful. But there are practical limits and a model can't read your mind or generate the output you're hoping for in every scenario.

We've made progress on this with reinforcement learning but maximizing useful output information with minimal input information is far from a solved problem. I expect this to be a key area of base model R&D and progress in the coming years. If nothing else, it's a helpful mental model for me to improve my ability to get useful information from AI, in particular because I've worked at this long enough to have some innate sense of when I'm asking for too much at once. After crossing a certain complexity threshold, today it's impossible to get the output I want.[^5]

## role of the system prompt + model harness

In my earlier example of using Cursor to generate a web app, Cursor produces quite a bit of novel styling information (try it, you'll see). Unsurprisingly, this is not by accident. It's specifically written into the system prompt that the output should contain ample styling.[^4] I'm sure this is incredibly useful to Cursor (the business) for live demos and sales calls, but it almost certainly contributes to the agents proclivity for randomly restyling things while attempting an unrelated task.

- Is getting an agent to stay on task impossible? *No.*
- Is getting Cursor to add functionality to a basic webapp without making unnecessary styling changes impossible? *Also no.* It just requires a user prompt that "overrides" the tendencies introduced by the system prompt.
- Do prompts to Cursor sometimes require more information than strictly necessary in the user prompt due to a somewhat-flawed system prompt? *Yeah.*
- Do I find this super lame and annoying? *100%* 🫠

When working with AI it's currently extremely helpful to develop an intuition about exactly how much information needs to go into the system prompt to generate the desired output. Too little, and you're going to find the desired output impossible to generate. Too much and you're wasting time prompt engineering.

Similarly, when building with AI it's important to build a system that maximizes the ratio of user-input information in to novel, useful information out. That's the foundation of why we'd want to use AI-powered tools and also a good way to avoid annoying your users. That's how to make a user's desired output possible with minimal effort (information in) on the user's part. Some techniques for doing this include well-written system prompts and useful MCP tools.

[^1]: Sure, there exist some "adversarial" desired outputs where this strategy won't work, but we'll ignore them for now. Maybe they can be produced by a different style of prompt. There are also unimportant caveats about the length of the context window and such.

[^2]: Here's a [chat with Claude 3.7](https://claude.ai/share/f6410775-3647-4d91-a147-b76a62a12bb8) that produces 7004 digits of π correctly before making a mistake (4 characters after my "keep going" prompt, which probably means something).

[^3]: [Grok 3's attempt to produce the text of _War and Peace_ (with some encouragment).](https://grok.com/share/c2hhcmQtMg%3D%3D_5d86aba5-d3c7-4186-b42d-139d99418fce) It stops faithfully reproducing the text and starts "summarizing" from "memory" by Chapter 2. Claude did better but "copyright filtered" the output even though the novel and its translation are in the public domain 🤷‍♀️.

[^5]: [Write a webserver that serves hello world pages in brainfuck](https://claude.ai/share/b389ae30-a71e-4fcb-a80a-a5bcdd54e2ba) is an example of an impossible output, for now. If you could figure out how to do it and encode that in the prompt, the model might have a chance. Unfortunately that would defeat the *more output info than input info* purpose of using AI (or to use my formula, provide negative user value).

[^4]: Here's one source for the "Cursor system prompt" that indicates [the model is specifically asked to produce styling information.](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/421b73c2cc2170210f7a3acdf25d30ebeb39fec6/Cursor%20Prompts/Agent%20Prompt.txt#L24)