#!/usr/bin/env python

from importd import d

import settings
import json
import sys


d(**settings.defaults)


@d('/')
def index(request):
  return d.HttpResponse('Hello, world.')
