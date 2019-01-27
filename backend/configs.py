# -*- coding: utf-8 -*-

import sys
import os
from envparse import env

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

TEMP_CAPTURED_DIR = os.path.join(ROOT_DIR, 'captured')

## from dotenv
env.read_envfile(os.path.join(ROOT_DIR, '.env'))
DARKNET_PATH = env.str("DARKNET_PATH", default='')

