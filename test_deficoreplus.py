# test_deficoreplus.py
"""
Tests for DeFiCorePlus module.
"""

import unittest
from deficoreplus import DeFiCorePlus

class TestDeFiCorePlus(unittest.TestCase):
    """Test cases for DeFiCorePlus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeFiCorePlus()
        self.assertIsInstance(instance, DeFiCorePlus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeFiCorePlus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
