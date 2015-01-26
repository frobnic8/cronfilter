#!/usr/bin/env python
"""cronfilter.py - Filter a list of dates based on a cron expression

"""

import sys
from croniter import croniter
from datetime import datetime
from logging import warning

__author__ = 'erskin@eldritch.org'
__version__ = '1.0.0'


def _usage(command):
    return 'usage: ' + command + ' "cron expression" [filename ...]'


def cronmatch(expression, date):
    """Return True if the date given would be executed by the cron expression
    given.

    """
    return croniter(expression, date).get_next(datetime) == date


def cronfilter(expression, dates):
    """Returns an iterable of dates which fall in the cron expression.

    literally:

        return [date for date in dates if cronmatch(expression, date)]

    """
    return [date for date in dates if cronmatch(expression, date)]


def cronfilter_file(expression, filehandle):
    """Return a list of dates from a file which match the expression."""
    results = []
    for line in filehandle:
        line = line.strip()
        date = datetime.strptime(line, "%Y-%m-%dT%H:%M:%SZ")
        if cronmatch(expression, date):
            results.append(date)
    return results


def main(args=sys.argv):
    """Filter a list of dates based on a cron expression."""

    matched = False
    filenames = []

    # If there were no arguments, we have no cron expression
    # which is required
    if len(args) < 2:
        print _usage(args[0])
        sys.exit(2)
    elif args[1] in ('-H', '-h', '-?', '--help'):
        print _usage(args[0])
        sys.exit()
    # Otherwise consider the command line arguments after the first
    # as filenames to read.
    else:
        expression = args[1]
        if len(args) == 2:
            filenames += ['-']
        for filename in filenames:
            # Support the convention of using '-' to refer to standard input.
            if filename == '-':
                failures += cronfilter_file(expression, sys.stdin)
            # Skip any file names that don't actually exists.
            elif not os.path.isfile(filename):
                warning('Skipping non-file ' + filename)
            # Process the lines in the file.
            else:
                with open(filename) as input_file:
                    failures += cronfilter_file(expression, input_file)

    if matched:
        sys.exit(0)
    else:
        sys.exit(1)


# Allow direct command line execution, just to be nice.
if __name__ == '__main__':
    main(sys.argv)
