# test_blockledger.py
"""
Tests for BlockLedger module.
"""

import unittest
from blockledger import BlockLedger

class TestBlockLedger(unittest.TestCase):
    """Test cases for BlockLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockLedger()
        self.assertIsInstance(instance, BlockLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
