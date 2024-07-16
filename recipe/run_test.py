#!/usr/bin/env python

import pytest
import sys
import importlib
from pathlib import Path

if __name__ == "__main__":
    # Default module to import for determining the test location

    exit_code = pytest.main(["-v", "bg_mpl_stylesheets/tests"])
    assert exit_code == 0, "Tests failed"
    sys.exit(exit_code)
