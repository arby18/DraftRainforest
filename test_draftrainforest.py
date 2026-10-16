# test_draftrainforest.py
"""
Tests for DraftRainforest module.
"""

import unittest
from draftrainforest import DraftRainforest

class TestDraftRainforest(unittest.TestCase):
    """Test cases for DraftRainforest class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftRainforest()
        self.assertIsInstance(instance, DraftRainforest)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftRainforest()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
