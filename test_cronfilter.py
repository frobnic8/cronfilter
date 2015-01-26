#!/usr/bin/env python
"""test_cronfilter.py - Unit tests for the cronfilter tool."""

from cronfilter import cronmatch, cronfilter_file
import subprocess
import unittest


# The TestCase class comes with more methods than pylint likes out of the box,
# so we disable that warning message here.
# pylint: disable=R0904


class TestOpassword(unittest.TestCase):
    """Test the methods in the cronfilter module."""

    def test_pep8(self):
        """Test that the code conforms to the style guide.

        """
        files = ('cronfilter.py', 'test_cronfilter.py')
        for name in files:
            subprocess.check_call(["pep8", name])
