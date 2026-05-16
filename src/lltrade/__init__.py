"""lltrade — trading research for the FullSense ™ LLM family.

PAPER-TRADING ONLY (v0.x).

This package emits trading signals via backtests and LLM-assisted strategy
proposals, all gated by the llive Approval Bus. Until v1.0+, signals are
never routed to a live broker — see ``REAL_TRADING`` below.

See https://furuse-kazufumi.github.io/lltrade/ for the design contract.
"""

# ─── Safety pin ────────────────────────────────────────────────────────────
# v0.x is hard-pinned to paper trading. Changing this requires a separate
# audited release branch — see CONTRIBUTING.md.
REAL_TRADING: bool = False
"""When False, lltrade refuses to route signals to a live broker SDK.
v0.x ships with this set to False; bypasses are a CRITICAL security issue
(see SECURITY.md)."""

__version__ = "0.0.1"
__all__ = ["__version__", "REAL_TRADING"]


def assert_paper_only() -> None:
    """Raise RuntimeError if REAL_TRADING has been mutated to True.

    Call this at the top of any code path that emits an order-shaped signal.
    The check exists so that monkey-patching ``REAL_TRADING = True`` at
    runtime still fails loudly inside the v0.x line.
    """
    if REAL_TRADING:
        raise RuntimeError(
            "lltrade v0.x is paper-only. REAL_TRADING was mutated to True. "
            "See SECURITY.md for the reporting path."
        )
