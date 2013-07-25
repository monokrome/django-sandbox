#!/usr/bin/env python

from importd import d
import json
import sys

@d('/')
def index(request):
  return d.HttpResponse('Hello, world.')

