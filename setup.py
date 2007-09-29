#!/usr/bin/env python

import sys
from distutils.core import setup
from googlecalsync import __version__

setup(name='googlecalendarsync',
      version=__version__,
      description="Google Calendar Synchronizer",
      author="Andrea Righi",
      author_email="righiandr@users.sf.net",
      scripts=['googlecalsync.py'],
      packages=None
      )

