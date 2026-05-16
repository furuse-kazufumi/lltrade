---
layout: default
title: "Spec"
nav_order: 2
---

# lltrade — Design Contract (v0.0.x)

## Mission

Make **trading research** (backtest, strategy proposal, risk evaluation)
executable by the FullSense LLM kernel ([llive](https://github.com/furuse-kazufumi/llive))
under strict **paper-only** constraints, with every order-shaped signal gated
by the Approval Bus and recorded in the SQLite Ledger.

## Hard safety pin

`REAL_TRADING = False` is enforced at three layers:

1. `src/lltrade/__init__.py` — module constant + `assert_paper_only()` guard
2. `pyproject.toml` `[tool.lltrade.safety]` block
3. This SPEC

A code path that emits an order-shaped signal MUST call `assert_paper_only()`
before doing so. Bypassing is a CRITICAL security issue (see SECURITY.md).

## Scope

### In-scope (v0.0.x)

- Backtest adapter for **Backtrader**, **vectorbt**, **NautilusTrader**
- Market-data ingestion: **CCXT**, **yfinance**, **Polygon** (read-only)
- Strategy proposal from LLM with constraint enforcement
- Risk metrics: Sharpe, Sortino, max drawdown, Calmar, VaR(95)
- Per-signal HITL review through llove
- Signal + verdict persistence to llive SQLite Ledger

### Out-of-scope (intentionally)

- Live order routing — until v1.0+ with separate audited release
- HFT / market-making — out of scope permanently for this product (different
  trust model, would be a separate product e.g. `llhft`)
- Crypto perps / leveraged — until v1.0+
- Tax / accounting / regulatory reporting — out of product scope; integrate
  with external tools

## llive integration points

| llive axis | lltrade responsibility |
|---|---|
| **RPAR** (Risk-Proportional Autonomy Routing) | Map signal size × volatility × portfolio impact to autonomy tier. Tier 1 = auto-log, Tier 2 = HITL, Tier 3 = block + alert |
| **SIL** (Semantic Integrity Ledger) | Every signal, every parameter, every market data snapshot to SQLite. Reproducibility is the product. |
| **DTKR** (Decision-Theoretic Knowledge Reasoning) | Expected value calculations, position sizing (Kelly variants), regime detection |
| **APO** (Action Policy Optimization) | Stop conditions, profit-taking, drawdown circuit-breakers |
| **KAR** (Knowledge Acquisition & Retention) | Ingest research papers (RAD `finance_quant` corpus), past backtests, market regime patterns |
| **ICP** (Intent-Constraint Propagation) | Carry "max drawdown 10%", "Sharpe > 1.5", "no tobacco sector" down to leaf signals |
| **PM** (Process Memory) | Remember which strategies the reviewer accepted / rejected per regime |
| **TLB** (Tool & Library Binding) | Adapt Backtrader / vectorbt / NautilusTrader / CCXT APIs |

## Public API (planned, not yet implemented)

```python
from lltrade import BacktestSession, RiskBudget, assert_paper_only

assert_paper_only()  # hard guard at top of file

session = BacktestSession(
    llive_backend="ollama:qwen2.5:32b",
    risk_budget=RiskBudget(max_drawdown=0.10, sharpe_target=1.5),
)

# 1. Propose a strategy
strategy_yaml = session.propose_strategy(
    market_view="Tech earnings season, expect dispersion",
    universe=["AAPL", "MSFT", "GOOGL", "META", "AMZN"],
)

# 2. Backtest
result = session.backtest(
    strategy=strategy_yaml,
    start="2023-01-01",
    end="2025-12-31",
    engine="vectorbt",
)

# 3. Submit to HITL review (llove)
verdict = session.submit_for_review(result, reviewer="self")

# All four calls log to SQLite ledger; (3) blocks on Approval Bus.
```

## Competitive positioning

| Capability | QuantConnect Lean | Backtrader | vectorbt | NautilusTrader | Freqtrade | **lltrade** |
|---|---|---|---|---|---|---|
| OSS | yes (CLI) | yes | yes (Pro closed) | yes | yes | **yes** |
| LLM-assisted strategy | no | no | no | no | no | **yes** (on-prem) |
| Approval Bus (per signal) | no | no | no | no | no | **yes** |
| HITL TUI | no | no | no | no | partial | **yes** (llove) |
| Audit Ledger | partial | no | no | partial | partial | **yes** (SQLite) |
| On-prem inference | n/a | n/a | n/a | n/a | n/a | **yes** |
| Hard paper-only pin | no | no | no | no | no | **yes** (v0.x) |

### vs. generic coding agents (Claude Code / Codex CLI / Gemini CLI)

| Capability | Claude Code | Codex CLI | Gemini CLI | **lltrade** |
|---|---|---|---|---|
| General code editing | A (SOTA) | A | A− | not the goal |
| **Risk-aware signal emission** | no | no | no | **yes** (RPAR axis) |
| **Per-signal Approval Bus gate** | warning only | approval mode | approval mode | **yes** (`block_until_decided`) |
| **Hard paper-only safety pin** | no | no | no | **yes** (3-layer pin) |
| **Audit Ledger** (SIL) | no | no | no | **yes** (SQLite, via llive) |
| **On-prem inference** | no (cloud) | no (cloud) | no (cloud) | **yes** (Ollama) |
| **End-to-end OSS** (incl. backend) | no | CLI only | CLI only | **yes** |
| HITL TUI (vs CLI approval) | no | CLI prompt | CLI prompt | **yes** (llove) |
| Backtest engine adapter (built-in) | no | no | no | **yes** (Backtrader/vectorbt/Nautilus) |

**Positioning**: generic coding agents can write a strategy file but cannot
enforce risk constraints, gate signals, or pin themselves to paper-only.
lltrade exists to make those constraints **architectural** rather than
"hope the operator remembered". Use a generic agent for one-off scripts;
use lltrade when the output must survive a compliance review.

See the umbrella comparison: [FullSense Comparison](https://furuse-kazufumi.github.io/fullsense/comparison.html).

## Risk model (v0.0.x)

Even in paper mode, signals are subject to:

1. **Pre-trade**: position size ≤ risk budget; sector cap not breached
2. **Real-time**: rolling drawdown < limit; volatility regime check
3. **Post-trade**: signal + executed-as-if price logged with timestamp + verdict

All three checks are mediated by the llive Approval Bus.

## Versioning

- v0.0.x — alpha skeleton (this revision)
- v0.1.0 — Backtrader adapter + simple strategy proposal
- v0.2.0 — vectorbt adapter + risk metrics suite
- v0.3.0 — NautilusTrader + llove HITL TUI integration
- v0.4.0 — RAD `finance_quant` corpus + market regime detection
- v1.0.0 — **separate live-trading audit release**, PyPI rename to `fullsense-trade`

## References

- [FullSense Spec v1.1](https://github.com/furuse-kazufumi/llive/blob/main/docs/fullsense_spec_eternal.md)
- [feedback_competitor_benchmark](../../../../.claude/projects/C--Users-puruy-raptor/memory/feedback_competitor_benchmark.md) — benchmark methodology
- llive C-1 Approval Bus — `D:/projects/llive/src/llive/approval/bus.py`
