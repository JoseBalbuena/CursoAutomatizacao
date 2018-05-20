#!/usr/bin/python

import yaml
from jinja2 import Environment,FileSystemLoader
from pprint import pprint


YAMFILE="/home/jose/labsolucao.yml"
TEMPLATESDIR="/home/jose/jinja2templates"
NTPTEMPLATE="ntp.j2"
OSPFTEMPLATE="ospf.j2"
CONFDIR="/home/jose/configs"

config = yaml.load(open(YAMFILE)) 

#pprint(config)

env = Environment(loader=FileSystemLoader(TEMPLATESDIR),trim_blocks=True)


for chave,valor in config.items():
 nomearquivoconf = CONFDIR + "/" + chave + ".config"
 if chave == 'ntpservers' :
  router_template = env.get_template(NTPTEMPLATE)
  output = router_template.render(ntpservers=valor)
 else:
  router_template = env.get_template(OSPFTEMPLATE)
  output = router_template.render(router=valor)
 print output
 with open(nomearquivoconf,'w') as fh:
  fh.write(output)

