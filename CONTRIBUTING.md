# Contributing to lltrade

Thank you for considering a contribution! lltrade is part of the FullSense ™
family — please read the [umbrella CONTRIBUTING](https://github.com/furuse-kazufumi/fullsense/blob/main/CONTRIBUTING.md)
first.

## ⚠️ Special rule: paper / live trading

PRs that **remove, weaken, or bypass** the `real_trading=False` hard-pin will
be rejected on sight. Until v1.0+ with a documented audit, lltrade is paper
only — this rule has no exceptions for "convenience" or "testing".

If you need to test live-trading code paths:

1. Open a discussion issue first (`real-trading-discussion` label)
2. Wait for an explicit greenlight from a maintainer
3. Work in a separate `live-experimental` branch that is never merged to `main`

## Developer Certificate of Origin (DCO)

All commits must be signed off:

```bash
git commit -s -m "your message"
```

See [https://developercertificate.org/](https://developercertificate.org/).

## PR workflow

1. Fork and branch from `main`
2. Add tests under `tests/`. **Tests that simulate live orders are forbidden
   without a maintainer-signed exemption.**
3. Run `pytest` locally and ensure it passes
4. Open the PR with a clear description and linked issue

## Style

- Python 3.11 only (the project pins `>=3.11,<3.12`)
- Format with `ruff format`, lint with `ruff check`
- Type-check with `mypy src/`
- Financial calcs use `decimal.Decimal`, not `float`

## Areas where help is welcome

- Backtrader / vectorbt / NautilusTrader adapter
- Risk metric implementations (Sharpe, Sortino, max drawdown, VaR)
- llove TUI dashboard for backtest results
- llive Approval Bus integration for per-signal HITL
