---
layout: default
title: "Progress"
nav_order: 90
---

# lltrade — Progress

## 2026-05-16 — Bootstrap (v0.0.1)

Skeleton landed:

- `README.md`, `LICENSE` (Apache-2.0), `NOTICE`, `SECURITY.md`, `CONTRIBUTING.md`
- `pyproject.toml` — name `llmesh-lltrade`, Python 3.11, with
  `[tool.lltrade.safety] real_trading = false` hard-pin
- `src/lltrade/__init__.py` — `REAL_TRADING = False` constant +
  `assert_paper_only()` guard function
- `docs/` — Jekyll just-the-docs skeleton with Mermaid 10.9
- `tests/test_smoke.py` — version + paper-only guard tests

No public API implementations yet; only `__version__`, `REAL_TRADING`, and
`assert_paper_only` are exported.

### Context

Created in the 2026-05-16 session as part of the FullSense umbrella expansion.
lltrade is the second of two new products spun up alongside `lldesign` to
stress-test [llive](https://github.com/furuse-kazufumi/llive) on **risk
axes** (RPAR, SIL, DTKR, APO) that lldesign cannot exercise (design tasks
rarely have monetary risk).

### Open items

- [ ] Open the GitHub repo (`furuse-kazufumi/lltrade`, public)
- [ ] Enable GitHub Pages (Settings → Pages → `main` / `/docs`)
- [ ] Implement v0.1.0 Backtrader adapter (`BacktestSession.backtest`)
- [ ] Simple strategy proposal API (`propose_strategy`)
- [ ] llive Approval Bus integration on the signal emission path

### Parked

- Live-trading branch — until v1.0+ with separate audit, **never on main**
- HFT / market-making — out of product scope (would be a separate `llhft`)

### Hard rule reminder

Any PR that removes / weakens / bypasses the `REAL_TRADING = False` guard is
**rejected on sight**. See CONTRIBUTING.md.
