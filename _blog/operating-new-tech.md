---
layout: post
title: Operating new tech
date: May 8, 2025
styles: |-
  .h-right {
      text-align: right;
      color: var(--text-muted)
  }
---
After years on the fence, I'm now convinced modern generative AI represents something legitimately new and valuable. Like everyone else though, there's still a huge question on my mind: what's it good for? Many eager nerds like myself will doubtlessly try very hard in the next few years to provide even a sliver of an answer to that question.

For now, the answer seemed to be simple---AI isn't useful for much. <abbr title="Generative pre-trained transformers">GPTs</abbr> producing text in isolated environments can't access up-to-date information about the world. They certainly can't reach beyond their prompt to understand the context of a given request or system. They can't do anything other than produce text; not call an API nor rename a file.

## context stuffing

But wait, there's ~~<abbr title="retrieval augmented generation">RAG</abbr>~~ <abbr title="model context protocol">MCP</abbr>. It turns out that a huge step toward making <abbr title="large language models">LLMs</abbr> useful consists of asking them to do less. We can build systems to feed relevant information into the context window of an LLM along with a user's request, and let the LLM do what it does best: synthesize a response based on the tokens in its context. RAG did this first by having the system pull the additional context before invoking the model. MCP reverses the order, and lets the model pull the addtional context itself.
<figure>
<img src="{{site.url}}/blog/operating-new-tech/cursor.png" alt="Cursor AI using MCP to identify how my python tests are structured" />
<figcaption>Cursor adds tools (and a ✨special system prompt✨) to help LLMs succeed at under-specified tasks</figcaption>
</figure>

This strategy is awesome. To anthropomorphize a bit, it lets us give models digital tools to help them work better within a given context and environment. Making everything into a text-based interface (provided by an MCP server) makes it accessible to LLMs.

This strategy has the intentional side-effect of exploding the possibility space of model behavior. For us users, that means it's no longer enough to have a rough understanding of a model's training data to predict its behavior; now we need to know what tools the model has access to as well. Had I sent the above message to a standard-issue chatbot using the same underlying model it would predictably [not run anything](https://claude.ai/share/91e37994-8241-4ae2-ad88-6e8f4dcfd7eb).

In particular, some---but not all---AI systems can:

* Operate on images (read, understand, OCR, etc.)
* Read PDFs
* Execute commands
* Open a support ticket with a company
* Work in various languages
* Operate on audio (input or output, streams or files)
* Run a vector retrieval query (for later use in output generation)
* Search the web
* Operate a web browser like a human

Unfortunately, no system will have all possible capabilities for the foreseeable future. Not only do models struggle to use tools well when they're given too many (>20 or so, I'm told), tools are also server-sided and some important implementations will likely be kept secret. No wonder Grok is the only model that will search Twitter/X for me. There's even more complexity introduced by custom weights/fine-tuning, few-shot learning prompts, context window length, reasoning and other techniques to tweak model behavior.

This is the latest challenge in keeping up with the state of the art of "things AI is useful for." There are more possible capabilities and AI products can be far more differentiated. Since AI products' unique features so far are usually only somewhat discoverable at best, users are regularly getting lost in the sauce.

## the dba

A skilled AI user today works a lot like the <abbr title="database administrator">DBA</abbr> of eras past. They work within a (semi-)corporate system, using tools with fairly steep learning curves. Most tasks are accomplished manually, but sufficiently common ones can be automated to the point of triviality with moderate investment.

This shouldn't be surprising. As secretaries were introduced to typewriters before their bosses, so too were databases (mainframes) managed by people with specialized skills at first. In college I volunteered as a DBA for a club for years. Users would email me "can you reset my password" and I'd figure out how to retrigger the password generation flow (yes, we generated passwords and emailed them to users, it was a perl system from before I was born). Sometimes I'd get "the list of current club members seems wrong" and I'd figure out how to adjust the query to account for a new membership tier which repurposed an old one from a decade earlier.

At work, AI must serve people but it's not yet easily accessible to them. My coworkers want to ask our internal chatbot "how many widgets did we sell last week?" but it needs to be told "generate and run a SQL query against the events.widget_transaction table to count the number of widgets we sold each week starting on monday since the start of May. here's a copy of the column definitions: transaction_type: enum ['bought', 'returned'], user_id: ..."

In the hands of power users, AI is surprisingly powerful already, turning prohibitively tedious manual processes into fairly short chats. For now, the devil is in the details of the prompt.

One arena where this is particularly apparent is Leetcode. A friend of mine is interviewing now and complained to me that AI isn't helpful at solving Leetcode questions. I thought the problem was more likely between the keyboard and chair, so I tried it out.

<h4 class="h-right">base case</h4>

If you just ask an off-the-shelf chatbot to solve a Leetcode question, it does indeed go poorly (at least for [#2484](https://leetcode.com/problems/count-palindromic-subsequences/description/)). I fired up ChatGPT, said "Solve this leetcode problem in python" and pasted the problem. I had to edit the output code a bit to get it running (Leetcode does not support type hints, and the interface is slightly different). Then, the output code passed 8/63 test cases 🤷‍♀️.

<h4 class="h-right">detailed prompt+reasoning</h4>

To help the AI do better I tried to have it follow something like my own process for passing such tests. The prompt was [waaay longer](https://chatgpt.com/share/681d5238-13e0-8000-851a-1df67284dff1) and I turned on reasoning so it could have time to follow the steps. The output code was clear enough, passed all 63 test cases, beat 86% of Leetcode respondents on runtime, 57% on memory usage, and did not require manual reformatting.

<h4 class="h-right">specialized system (or even better prompt?)</h4>

Then there's [this dev on reddit](https://www.reddit.com/r/leetcode/comments/194fpfo/i_made_a_gpt_to_help_you_study_leetcode/) who made a ChatGPT app that does the same thing: solve Leetcode questions. It was able to answer my question even when I only gave it [an extremely simple set of prompts](https://chatgpt.com/share/681d542d-d338-8000-bf69-679365454cb7): I pasted the problem, saw that response did not contain a solution, wrote "solve it" and the solution worked great (beat 86% on time and 71% on space). It was structured slightly better than the one from my verbose prompt too.

## toward valuable ai

By now it's clear that the utility of AI for a given task is highly dependent on both the quality of the input and the quality of the harness around the model. For example, Claude produced an equivalent quality Leetcode solution to ChatGPT, but reasoned for 4 minutes instead of ChatGPT's 22 seconds. This represents a surprising difference in compute cost for similar output, attributable entirely to the harness I can't change.

To get value out of AI today one can become an expert. Learn the models and their relative strengths. Be aware of which tools are available where. Provide context the models can't gather themselves. Spend time writing high-quality prompts and keep track of your favorite techniques for next time. Learn the intricacies of the system without being able to change it. Copy paste intermediate representations between chatbots to use the tools you need. Be useful.

That's the DBA way.

However, DBAs have somewhat gone the way of the dodo. When a user needs their password reset, my company has self-service flows online. When they want documents updated in our databases, they can contact support and support can also use web-based flows to perform the updates without (directly) running INSERT queries in prod.

For a company to build valuable AI products for internal users, they'll need to spiritually automate out the DBA again. Build MCP servers to open access to internal data. Write (or generate 😈) knowledge bases that describe what's available from various internal systems. Curate a library of prompts that direct models on how to best use these new tools, then make them available in a user-friendly, discoverable way.

I haven't thought about B2C AI as much because it seems like tech companies, midsize and up, are best positioned to be early adopters of the latest AI advancements. They have large amounts of internal documentation available to operate on (think about all those historical PRDs that need searching). They can invest technical know-how in building the specialized context-augmentation tools needed to get the most utility from LLMs. They can train employees on how to use imperfect systems. These factors alone are enough to make AI at work extremely promising.

But AI can't do my job. If you work behind a desk, AI probably can't do yours. (If you don't, it definitely cant.) But soon I expect to see AI starting to leak in on the margins. Certain tasks will be drastically simplified by purpose-built AI systems, especially textual ones. Whoever makes the first Slack bot that can answer questions well using data from Jira, Google Docs, Slack, Git(Hub), data lakes, etc. will find customers quite easy to acquire, even if it only works 50% of the time.

Today though, AI is most useful if you invest the time in learning how to use it well. Like the Leetcode example, a simple prompt may not work but a careful choreography of models and tools might. Even better is the special-purpose AI system that doesn't require informed prompting.

I, for one, am excited to see some disruption return to the tech industry as AI becomes more accessible. It's not ready to displace much of anything today but the ingredients are there and it's time for us enthusiasts to get in the kitchen and start cooking.