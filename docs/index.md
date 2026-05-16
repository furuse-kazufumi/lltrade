---
layout: default
title: "lltrade"
description: "Trading research for the FullSense LLM family — paper trading only"
nav_order: 1
---

# lltrade

> **Trading research for the FullSense ™ family.**
> **PAPER-TRADING ONLY (v0.x).** LLM-assisted backtest, strategy proposal,
> and risk-aware execution — gated by the llive Approval Bus.

Part of the [FullSense ™](https://furuse-kazufumi.github.io/fullsense/) family.

## ⚠️ Safety pin

`REAL_TRADING = False` is hard-pinned in `src/lltrade/__init__.py`,
`pyproject.toml` (`[tool.lltrade.safety]`), and the SPEC. v0.x **never**
routes orders to a real broker. Live trading is planned for v1.0+ behind
a separate audited release process.

This is **research / educational software, not financial advice.**

## What it does

- **Backtest** strategies on historical market data (Backtrader / vectorbt /
  NautilusTrader adapters)
- **Propose** strategies from an LLM brief with hard constraints (max drawdown,
  Sharpe target, sector caps)
- **Evaluate risk** before any signal emission — every signal must pass through
  the llive Approval Bus (RPAR axis)
- **Persist** every signal + reviewer verdict to the llive SQLite Ledger (SIL axis)
- **Review** through llove TUI, with paper-only execution sandbox

## Status

**v0.0.1 alpha (skeleton)** — public API will change. See
[PROGRESS]({{ '/PROGRESS' | relative_url }}) for the live changelog and
[SPEC]({{ '/SPEC' | relative_url }}) for the design contract.

## Install

```bash
pip install llmesh-lltrade           # core (paper only)
pip install "llmesh-lltrade[llive]"  # with llive integration
```

## Why this and not QuantConnect / Backtrader / vectorbt?

- **LLM-assisted strategy proposal, on-prem** — strategies emerge from the
  llive kernel running against your own Ollama / LM Studio backend
- **Per-signal HITL** — every order-shaped signal lands in llove for human
  review before being recorded as an "intent"
- **Audit Ledger** — SQLite-backed log of every signal, every verdict, every
  parameter for reproducibility
- **Hard safety pin** — v0.x refuses to be coerced into live trading even by
  monkey-patching

See the full comparison: [FullSense Comparison](https://furuse-kazufumi.github.io/fullsense/comparison.html).

## Disclaimer

lltrade is research software. Past performance of any strategy expressed in
its DSL does not guarantee future performance. The maintainers accept no
liability for losses arising from use of this software. **Consult a licensed
financial advisor** before acting on any signal.

## Links

- [GitHub repo](https://github.com/furuse-kazufumi/lltrade)
- [FullSense umbrella](https://furuse-kazufumi.github.io/fullsense/)
- [llive](https://furuse-kazufumi.github.io/llive/) · [llove](https://furuse-kazufumi.github.io/llove/) · [llmesh](https://furuse-kazufumi.github.io/llmesh/)

---

*lltrade ™ is a trademark of Kazufumi Furuse. Code under Apache-2.0.*
