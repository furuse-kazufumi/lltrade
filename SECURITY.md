# Security Policy

## Reporting a vulnerability

Email: `kazufumi@furuse.work` with subject prefix `[lltrade-security]`.

We aim to acknowledge within 72 hours. **For critical issues** (e.g., paper /
live mode confusion, signal exfiltration, broker credential leakage) please
mark `[lltrade-security-CRITICAL]` for priority routing.

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.0.x   | yes (alpha, paper-only) |
| < 0.0   | no |

## Threat model (v0.0.x)

lltrade processes market data and emits trading **signals** (paper only).
Even in paper mode, the following are in scope:

### Critical (CVSS ≥ 9)

- **paper / live mode confusion** — any code path that bypasses the
  `real_trading=False` guard. This includes monkey-patching, environment
  variable overrides, and broker SDK side-channels.
- **Approval Bus bypass** — emission of any trading signal that did not pass
  through `llive.approval.bus.request()`.

### High (CVSS 7–8)

- **broker credential leakage** — even in paper mode, broker SDK tokens may
  exist in env / config. Treat as secrets.
- **Ledger tampering** — modifications to SQLite Ledger that hide rejected
  signals.

### Medium

- **market data spoofing** — accepting unverified market data that biases
  backtest results.

See [FullSense SECURITY](https://github.com/furuse-kazufumi/fullsense/blob/main/SECURITY.md)
for the umbrella policy.
