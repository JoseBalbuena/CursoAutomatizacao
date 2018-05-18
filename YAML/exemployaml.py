#!/usr/bin/python
import yaml
from pprint import pprint

#Carregando arquivo YAML na variavel dicionario config
config = yaml.load(open('exemployaml.yml'))
pprint(config)


