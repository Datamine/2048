# -*- coding: utf-8 -*-
"""
tests for game2048.py
John Loeber | July 12 2016 | Python 2.7.6 | contact@johnloeber.com
"""

import unittest
import game2048

BOARD_1 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
BOARD_2 = ['2', '4', '8', '16', '2', '4', '8', '32', '256', '8', '8', '2', '2', '2', '', '']
BOARD_3 = ['16', '8', '8', '8', '4', '4', '4', '32', '12', '8', '8', '2', '2', '2', '', '']
BOARD_4 = ['1024', '1024', '1024', '1024', '4', '8', '', '8', '16', '', '', '', '4', '4', '', '4']
BOARD_5 = ['', '', '', '4', '', '4', '', '8', '16', '', '2', '', '2', '2', '', '4']
BOARD_6 = ['8', '', '8', '', '', '4', '', '4', '16', '', '16', '', '2', '2', '2', '2']

class ContactsTests(unittest.TestCase):
    """
    Tests for contacts_rank.py
    """
    def test_newboard(self):
        self.assertEqual(game2048.newboard(BOARD_1, "up"), BOARD_1)
        self.assertEqual(game2048.newboard(BOARD_1, "down"), BOARD_1)
        self.assertEqual(game2048.newboard(BOARD_1, "left"), BOARD_1)
        self.assertEqual(game2048.newboard(BOARD_1, "right"), BOARD_1)

        self.assertEqual(game2048.newboard(BOARD_2, "up"), ['4', '8', '16', '16', '256', '8', '8', '32', '2', '2', '', '2', '', '', '', ''])
        self.assertEqual(game2048.newboard(BOARD_2, "down"), ['', '', '', '', '4', '8', '', '16', '256', '8', '8', '32', '2', '2', '16', '2'])
        self.assertEqual(game2048.newboard(BOARD_2, "left"), ['2', '4', '8', '16', '2', '4', '8', '32', '256', '16', '2', '', '4', '', '', ''])
        self.assertEqual(game2048.newboard(BOARD_2, "right"), ['2', '4', '8', '16', '2', '4', '8', '32', '', '256', '16', '2', '', '', '', '4'])

        self.assertEqual(game2048.newboard(BOARD_3, "up"), ['16', '8', '8', '8', '4', '4', '4', '32', '12', '8', '8', '2', '2', '2', '', ''])
        self.assertEqual(game2048.newboard(BOARD_3, "down"), ['16', '8', '', '', '4', '4', '8', '8', '12', '8', '4', '32', '2', '2', '8', '2'])
        self.assertEqual(game2048.newboard(BOARD_3, "left"), ['16', '16', '8', '', '8', '4', '32', '', '12', '16', '2', '', '4', '', '', ''])
        self.assertEqual(game2048.newboard(BOARD_3, "right"), ['', '16', '8', '16', '', '4', '8', '32', '', '12', '16', '2', '', '', '', '4'])

        self.assertEqual(game2048.newboard(BOARD_4, "up"),  ['1024', '1024', '1024', '1024', '4', '8', '', '8', '16', '4', '', '4', '4', '', '', ''])
        self.assertEqual(game2048.newboard(BOARD_4, "down"), ['1024', '', '', '', '4', '1024', '', '1024', '16', '8', '', '8', '4', '4', '1024', '4'])
        self.assertEqual(game2048.newboard(BOARD_4, "left"), ['2048', '2048', '', '', '4', '16', '', '', '16', '', '', '', '8', '4', '', ''])
        self.assertEqual(game2048.newboard(BOARD_4, "right"), ['', '', '2048', '2048', '', '', '4', '16', '', '', '', '16', '', '', '4', '8'])

        self.assertEqual(game2048.newboard(BOARD_5, "up"), ['16', '4', '2', '4', '2', '2', '', '8', '', '', '', '4', '', '', '', ''])
        self.assertEqual(game2048.newboard(BOARD_5, "down"), ['', '', '', '', '', '', '', '4', '16', '4', '', '8', '2', '2', '2', '4'])
        self.assertEqual(game2048.newboard(BOARD_5, "left"), ['4', '', '', '', '4', '8', '', '', '16', '2', '', '', '4', '4', '', ''])
        self.assertEqual(game2048.newboard(BOARD_5, "right"), ['', '', '', '4', '', '', '4', '8', '', '', '16', '2', '', '', '4', '4'])

        self.assertEqual(game2048.newboard(BOARD_6, "up"), ['8', '4', '8', '4', '16', '2', '16', '2', '2', '', '2', '', '', '', '', ''])
        self.assertEqual(game2048.newboard(BOARD_6, "down"), ['', '', '', '', '8', '', '8', '', '16', '4', '16', '4', '2', '2', '2', '2'])
        self.assertEqual(game2048.newboard(BOARD_6, "left"), ['16', '', '', '', '8', '', '', '', '32', '', '', '', '4', '4', '', ''])
        self.assertEqual(game2048.newboard(BOARD_6, "right"), ['', '', '', '16', '', '', '', '8', '', '', '', '32', '', '', '4', '4'])

if __name__=='__main__':
    unittest.main()
