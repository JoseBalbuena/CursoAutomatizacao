#!/usr/bin/python

import yaml
from pprint import pprint

YAMFILE="/home/jose/labsolucao.yml"

config = yaml.load(open(YAMFILE)) 


#for ntpserver in config['ntpservers']:
# print("ntp server %s" % ntpserver['ntpserver'])
# print("!")


#print("router ospf 1")
#for interface in config['R1']['ospf']['interfaces']:
# print("!")
# print("interface %s" % interface['interface'])
# print("ip ospf 1 area %s" % interface['area'])
# print("!")

#print("router ospf 1")
#for interface in config['R2']['ospf']['interfaces']:
# print("!")
# print("interface %s" % interface['interface'])
# print("ip ospf 1 area %s" % interface['area'])
# print("!")




print("Criando as nossas conf a partir do arquivo YAML")
for item,valor in config.items():
 #item pode ser R1,R2 ou ntpservers
 nomearquivo=item + ".config" 
 with open(nomearquivo,'w') as fh:
  if item == 'ntpservers':
   for ntpserver in valor:
    line="ntp server " + ntpserver['ntpserver'] + "\n"
    fh.write(line)
  else:
   for interface in valor['ospf']['interfaces']:
    fh.write("!\n")
    line="interface " + interface['interface'] + "\n"
    fh.write(line)
    line="ip ospf 1 area " + str(interface['area']) + "\n"
    fh.write(line)
    fh.write("!\n")
