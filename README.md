# lltrade

> **Trading research for the FullSense ™ family.** **PAPER-TRADING ONLY** for v0.x. LLM-assisted backtest, strategy proposal, and risk-aware execution — gated by the llive Approval Bus.

Part of [FullSense ™](https://furuse-kazufumi.github.io/fullsense/) — Apache-2.0 OSS family for self-evolving, on-prem, audit-friendly LLM systems.

## ⚠️ Safety pin

`real_trading = false` is **hard-pinned** in `pyproject.toml`, the package
`__init__.py`, and the SPEC. v0.x will **never** route an order to a real
broker. Live trading requires a separate audited release branch (planned for
v1.0+), explicit reviewer approval, and a written risk policy.

## Scope (v0.0.x — alpha)

- Backtest engine wrappers (Backtrader / vectorbt / NautilusTrader adapters)
- Market-data ingestion (CCXT / yfinance / Polygon — read-only)
- Strategy proposal from LLM with **constraint enforcement** (max drawdown,
  Sharpe target, sector caps)
- Risk evaluation prior to *any* signal emission (RPAR axis)
- Persistence of every signal + reviewer verdict to llive SQLite Ledger (SIL axis)
- HITL review through llove TUI

## Out of scope

- Live order routing (until v1.0+ with separate audit)
- HFT / market-making
- Crypto perps / leveraged products (until v1.0+)
- Tax / accounting / regulatory reporting

## Install

```bash
pip install llmesh-lltrade           # core (paper only)
pip install "llmesh-lltrade[llive]"  # with llive integration
```

## Competitive positioning

| Capability | QuantConnect | Backtrader | vectorbt | Freqtrade | **lltrade** |
|---|---|---|---|---|---|
| OSS backtest | yes | yes | yes (Pro closed) | yes | **yes** |
| **LLM-assisted strategy** | no | no | no | no | **yes** (on-prem) |
| **Approval Bus (per signal)** | no | no | no | no | **yes** (llive) |
| **HITL TUI review** | no | no | no | partial (Telegram) | **yes** (llove) |
| **Audit Ledger** (SIL) | partial | no | no | partial | **yes** (SQLite) |
| On-prem inference | n/a | n/a | n/a | n/a | **yes** (Ollama) |

## Related

- [llmesh](https://github.com/furuse-kazufumi/llmesh) — secure LLM hub
- [llive](https://github.com/furuse-kazufumi/llive) — memory + execution kernel
- [llove](https://github.com/furuse-kazufumi/llove) — TUI workbench

## License

Code: **Apache-2.0**. Commercial license available. **No warranty for trading
losses** — this is research software, not financial advice.

*lltrade ™ is a trademark of Kazufumi Furuse, part of the FullSense ™ family.*
