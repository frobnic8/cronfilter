#!/usr/bin/env python
"""test_cronfilter.py - Unit tests for the cronfilter tool."""

from cronfilter import cronmatch, cronfilter_file
import pep8
import unittest


# The TestCase class comes with more methods than pylint likes out of the box,
# so we disable that warning message here.
# pylint: disable=R0904


class TestCronfilter(unittest.TestCase):
    """Test the methods in the cronfilter module."""

    def test_style(self):
        """Test that the code conforms to the style guide.

        """
        guide = pep8.StyleGuide()
        report = guide.init_report()
        report.start()
        files = ('cronfilter.py', 'test_cronfilter.py')
        for name in files:
            guide.input_file(name)
        report.stop()
        self.assertEqual(report.total_errors, 0,
                         "Found %i code style errors (and warnings)." %
                         report.total_errors)
