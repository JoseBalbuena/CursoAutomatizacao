#!/usr/bin/python3

import pyeapi
from pprint import pprint

node = pyeapi.connect_to('API-EOS')
output=node.enable('show hostname')
pprint(output)

