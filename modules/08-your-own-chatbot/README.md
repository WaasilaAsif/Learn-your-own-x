---
status: proposed
proposed-by: Waasila Asif
domain: AI/ML (All)
type: build-your-own
---

# 08: Build your own chatbot (PROPOSAL)

> **This is a module proposal, not a finished module.** No `starter/` code exists yet.
> Approve the scope here and the starter sandbox + checker get built next, in the
> same format as modules 00–03. See the **Build plan** at the bottom.

**You'll build:** a chatbot with a personality of your choosing — a system prompt, a memory of the conversation, and one simple "tool" it can call — running against a free LLM endpoint
**You'll understand:** what a chatbot *is* underneath (a loop, a list of messages, and a prompt), why the system prompt is the whole personality, and where "it made that up" comes from
**Time:** one workshop (about 2 hours) plus a weekend
**Format:** self-paced or in person, bring a laptop

## Why this module (the other crossover one)

Two audiences, one project. **Non-technical** students shape the bot's persona, write and A/B its system prompt, and design what it should refuse — real work that needs no code. **Technical** students wire the API loop, add conversation memory, and give it a tool to call. Both ship the same artifact and both learn the thing people most misunderstand right now: the model isn't magic, it's a prompt and a message list.

It sits one rung below module 03 on the AI ladder: **08 shapes a model's behavior with prompts; 03 extends it with real tools over MCP.** Finishing 08 makes 03 click.

## Prerequisites

- **Python 3.10+**; `pip install` a small OpenAI-compatible client (or just `requests`).
- A **free** model endpoint — the module defaults to local [Ollama](https://ollama.com/) and documents a free hosted option (e.g. Groq's free tier) via env vars. **No paid Claude/OpenAI subscription required** (same approach as module 03's `host.py`).

## Draft checkpoints

1. **One turn.** Send a single message to the endpoint and print the reply. *Check it:* you get a coherent response back; the checker confirms the client is configured and reachable (and prints clear setup help if not).
2. **Give it a personality.** Add a system prompt; make the same question answered in two different personas. *Check it:* swapping the system prompt visibly changes the tone for the same user input.
3. **Memory.** Keep the running message list so it remembers what you said three turns ago. *Check it:* tell it your name, ask two unrelated things, then ask "what's my name?" — it recalls it.
4. **One tool.** Let it call a single local function (e.g. `get_time()` or a dice roll) when asked. *Check it:* asking "roll a d20" triggers the tool and the bot reports the actual rolled number, not a hallucinated one.

## Build plan (what ships when approved)

- `starter/bot.py` — the endpoint client and REPL loop done for you; `build_messages()` (system + memory) and the tool-dispatch branch left as `TODO`s.
- `starter/personas/` — a couple of example system prompts to remix.
- `starter/check.py` — a **deterministic, offline** checker: it mocks the LLM call so checkpoints 2–4 (message assembly, memory, tool-dispatch logic) verify without a live model or network; a separate `--live` smoke test exercises the real endpoint. Fails on the skeleton, passes when complete.
- Keeps the free/local-first stance of module 03; ASCII-only output. MCP spec note from module 03 does **not** apply here — this is plain chat completions, not MCP.

## Going further

- Add a second tool and let the bot decide which to call.
- Stream the reply token-by-token instead of waiting for the whole thing.
- Add a cheap "guardrail": a refusal rule in the system prompt, then try to talk it past one — see how brittle prompt-only safety is.
- Graduate to module 03 and expose your tool over MCP instead of a hard-coded branch.

## Further reading

- [Anthropic: Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — why the system prompt carries so much.
- [OpenAI chat completions format](https://platform.openai.com/docs/guides/text-generation) — the message-list shape every endpoint copies.
- Module [03: MCP server](../03-mcp-server/) — the real-tools next step.

## Open questions for review

- Default endpoint: local Ollama (works offline, matches module 03) vs a hosted free tier (zero install)? Recommended: document both, default to whichever the cohort already set up for module 03.
- Overlap with module 03 is intentional (shape → extend). Confirm we want both in the catalog rather than merging — recommended to keep separate; different audiences.
