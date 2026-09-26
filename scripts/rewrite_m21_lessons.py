#!/usr/bin/env python3
"""Thin wrapper: rewrite only M21 lessons."""
import runpy
import sys
from pathlib import Path

sys.argv = [sys.argv[0], "--only", "m21"]
runpy.run_path(str(Path(__file__).with_name("rewrite_m21_m26_lessons.py")), run_name="__main__")
