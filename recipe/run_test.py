#!/usr/bin/env python

import pytest
import sys
import importlib
from pathlib import Path

if __name__ == "__main__":
    # Default module to import for determining the test location
    default_module = 'bg_mpl_stylesheets'

    module_name = sys.argv[1] if len(sys.argv) > 1 else default_module

try:
    module = importlib.import_module(module_name)
    module_path = Path(module.__file__).parent
    test_location = module_path / 'tests'

    # Ensure the test location exists
    if not test_location.exists():
        raise FileNotFoundError(f"Test location {test_location} does not exist.")

    exit_code = pytest.main([str(test_location), "-v"])

    # Assert that all tests passed
    assert exit_code == 0, "Tests failed"

    # Exit with the pytest exit code
    sys.exit(exit_code)

except ImportError as e:
    print(f"Error importing module {module_name}: {e}")
    sys.exit(1)
except FileNotFoundError as e:
    print(e)