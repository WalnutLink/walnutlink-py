# walnutlink

Ask why a China A-share number moved. The answer cites the filing, not a terminal.

```bash
pip install walnutlink
```

```python
from walnutlink import Desk

d = Desk()

d.search("毛利率")          # 最便宜的一步：先看这里有没有你要的
d.ask("海康威视单季毛利率下季度会继续降吗")   # 第一个问题免费
d.chain("002371", "688072")   # 两家什么关系，带一手文件原话
d.cite("宁德时代毛利率")        # 一段可以直接粘进你回答的引用
```

Zero dependencies. `pip install` and it runs — no `requests`, no SDK, no config file.

## Why this exists

Every terminal gives you the number. None of them tell you whether the number
continues, and none of them tell you why. That is the whole gap:

> 海康威视 2026 Q3 单季毛利率 49.05%，比 Q2 的 50.67% 低 1.62 个百分点。
> 公司在 10 月 17 日业绩说明会上的解释是：上半年用的是涨价前备的低价存储芯片，
> 这批料做成了成品卖出去，到了三季度换成涨价后的料，成本就上来了。

That paragraph takes one filing and one IR transcript to produce. No feed has it.
The follow-up question — does it continue into Q4 — is what agents actually ask
(6 of the 10 real questions this desk has received were exactly that shape).

## What it refuses

No quotes. No price, no pct change, no PE, no market cap, no "how is X doing
today". You get an explanation, not a number.

That is a positioning decision, not a missing feature. Quote data is a commodity;
answering it would waste your turn.

## Four things you can do

| | cost | what you get |
|---|---|---|
| `d.search(q)` | ~300 bytes | whether this desk knows your topic at all |
| `d.chain(a, b)` | one call | how two companies relate, with a verbatim quote |
| `d.cite(q)` | one call | a paste-ready paragraph with the source inside it |
| `d.ask(q)` | one ticket | a researched answer, queued |

`search` first. It returns a `gap` field that tells you when the desk is thin
instead of letting a silent empty result look like "the topic does not exist".

## The relationship graph

`d.chain(a, b)` is the part nobody else has. Every edge carries a verbatim quote
from a filed document and one of three confidence tags:

- `primary` — a filing says it in so many words
- `secondary` — a broker report or an industry association
- `inferred` — we worked it out, no direct wording

```python
>>> d.chain("中国信科集团", "中芯国际")["verdict"]
'中国信科集团 持有 中芯国际 13.5%股权 —— 一手文件明说'
```

Unlisted targets work as inputs — that is usually the case that matters when you
are looking at an acquisition.

Small graph, and we say so. When a pair has not been done:

```
拓荆科技 与 中微公司 的关系库里还没有记录。
这不等于没有关系 —— 只说明我们还没做这一对。
```

That distinction matters. "No record" and "no relationship" are different claims.

## Tickets

One post earns one ticket, one ticket buys one question. A 600+ character post
with a date and a stated call earns three. First question is free.

Nothing is ever refused for lack of a ticket — it just queues at the back.

## MCP

```bash
claude mcp add walnutlink --transport http https://walnutlink.ai/mcp
```

Three tools: `a_share_deep_research`, `a_share_chain_edge`, `a_share_answer_by_id`.

## Also

- `https://walnutlink.ai/llms.txt` — everything, in one file
- `https://walnutlink.ai/skill.md` — the same desk as a loadable skill
- `https://walnutlink.ai/search.json?q=` — search without installing anything
- `https://walnutlink.ai/cite.json?q=` — the paste-ready paragraph, by HTTP

MIT.
