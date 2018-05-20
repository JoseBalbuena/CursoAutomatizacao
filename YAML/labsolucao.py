#!/usr/bin/python

import yaml
from jinja2 import Environment,FileSystemLoader
from pprint import pprint


YAMFILE="/home/jose/labsolucao.yml"

config = yaml.load(open(YAMFILE)) 

pprint(config)
