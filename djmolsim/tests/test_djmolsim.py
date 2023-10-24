"""
Unit and regression test for the djmolsim package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import djmolsim


def test_djmolsim_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "djmolsim" in sys.modules
