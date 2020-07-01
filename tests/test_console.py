#!/usr/bin/python3
"""
    TestConsole module
"""
import unittest
import sys
from io import StringIO
import re
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
        TestConsole class
    """
    def test_help_console_cmd(self):
        """
        Test <help>
        """
        expected="""
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(expected, f.getvalue())

    def test_help_quit_console_cmd(self):
        """
        Tests <help quit>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertRegex(f.getvalue(), '^Quit command')

    def test_help_EOF_console_cmd(self):
        """
        Tests <help EOF>
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertRegex(f.getvalue(), '^EOF command')
