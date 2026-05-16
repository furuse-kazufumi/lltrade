"""Smoke tests — package import, version string, and paper-only guard."""

import re

import pytest

import lltrade


def test_version_string() -> None:
    assert isinstance(lltrade.__version__, str)
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:[ab.+\-]\w+)?", lltrade.__version__), (
        f"unexpected version format: {lltrade.__version__!r}"
    )


def test_real_trading_is_pinned_false() -> None:
    """The v0.x hard-pin must hold on import."""
    assert lltrade.REAL_TRADING is False, (
        "REAL_TRADING must be False on a fresh import (v0.x paper-only pin)"
    )


def test_assert_paper_only_passes_in_default_state() -> None:
    """The guard returns None silently when REAL_TRADING is False."""
    lltrade.assert_paper_only()  # must not raise


def test_assert_paper_only_raises_if_mutated() -> None:
    """The guard catches monkey-patching."""
    original = lltrade.REAL_TRADING
    lltrade.REAL_TRADING = True
    try:
        with pytest.raises(RuntimeError, match="paper-only"):
            lltrade.assert_paper_only()
    finally:
        lltrade.REAL_TRADING = original


def test_public_api_minimal() -> None:
    assert set(lltrade.__all__) == {"__version__", "REAL_TRADING"}
