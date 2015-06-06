from flask import Flask
import os
import sys

MAX_SEARCH_RESULTS = 50
WHOOSH_BASE = os.path.join(basedir, 'search.db')