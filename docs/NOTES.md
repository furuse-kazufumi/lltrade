---
layout: default
title: "Notes"
nav_order: 91
---

# lltrade — Design Notes

## Decisions

### Why a separate "lltrade", not a submodule of llive?

llive is a kernel; lltrade is a domain application that *uses* the kernel.
Same separation pattern as llove / lldesign. Lets users install llive without
pulling in market-data dependencies, and lets lltrade rev independently.

### Why paper-only in v0.x?

Live trading requires:

1. A separate audited release process (security, code review, key handling)
2. Broker SDK integration with each broker's TOS / regulatory acceptance
3. Operator-side risk policy that lltrade cannot infer

None of those exist yet, so v0.x is hard-pinned to paper. The pin lives in
**three places** (init, pyproject, SPEC) so a single-file edit cannot lift it
silently.

### Why three backtest engines (Backtrader / vectorbt / NautilusTrader)?

- **Backtrader** — most pedagogical, slow but readable, good for strategy
  prototyping with the LLM
- **vectorbt** — fast vectorised; needed once strategies survive Backtrader
- **NautilusTrader** — production-grade, needed for the v1.0+ live audit branch

Implementing one adapter at a time (v0.1 = Backtrader → v0.2 = vectorbt → v0.3 =
NautilusTrader) keeps the surface area small per release.

### Why Approval Bus on EVERY signal, not just risky ones?

Two reasons:

1. **Audit completeness** — partial logging is worse than no logging because it
   creates a false sense of coverage.
2. **Reviewer training** — the reviewer (human, via llove) needs to see "boring"
   signals too to calibrate intuition. If we only show risky ones, the reviewer
   loses context.

The Approval Bus tier system (Tier 1 = auto-log, Tier 2 = HITL, Tier 3 = block)
keeps the volume manageable.

## Competitive landscape observed (2026-05-16)

| Product | OSS? | LLM-assisted? | HITL? | Audit log? |
|---|---|---|---|---|
| **QuantConnect Lean** | CLI yes, cloud no | no | no | partial (cloud only) |
| **Backtrader** | yes | no | no | no |
| **vectorbt** | community yes, Pro no | no | no | no |
| **NautilusTrader** | yes | no | no | partial |
| **Freqtrade** | yes | no | partial (Telegram) | partial |
| **TradingView Pine** | no | no | no | no |
| **Composer / QuantStats** | yes (research) | no | no | no |

→ **No competitor combines OSS + LLM + HITL + on-prem + Audit Ledger.** That's
the gap lltrade fills.

## Deferred

- **Multi-asset portfolio optimisation** — v0.5+
- **Options Greeks** — v0.6+ (needs separate audit for derivative complexity)
- **Live broker SDK adapter** — v1.0+ only, separate branch
- **Tax-loss harvesting** — out of product scope

## Pitfalls to anticipate

- **Look-ahead bias** in backtests — vectorbt is fast precisely because it
  vectorises; easy to leak future info. Adapter must use only point-in-time data.
- **Survivorship bias** in universe selection — when ingesting historical
  tickers, include delisted ones.
- **LLM hallucinating tickers** — strategy proposal must validate ticker
  existence against the universe before serialising.

Captured globally in [`feedback_webpage_research_first`](../../../../.claude/projects/C--Users-puruy-raptor/memory/feedback_webpage_research_first.md)
(general principle: knowledge-dense domains need research before implementation).
