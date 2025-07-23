"""
This script will discover and run all unit tests in the 'tests' directory.
"""

import sys
import unittest

if __name__ == '__main__':
    # Discover and run all tests
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    sys.exit(not runner.run(suite).wasSuccessful())
