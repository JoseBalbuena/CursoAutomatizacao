#!/usr/bin/python3

#####################################################
# NAPALM EXEMPLO DE USO
#####################################################

import napalm


#MAIN

#Credenciais de Acesso
R1={'ip':'1.1.1.1','hostname':'R1','user':'napalm','pass':'napalm','so':'ios'}
R2={'ip':'2.2.2.2','hostname':'R2','user':'napalm','pass':'napalm123','so':'junos'}

#Lista de diccionarios
MyRouters=[R1,R2]

#Laco de iteracao
for router in MyRouters:
 #Escolhendo o driver
 driver = napalm.get_network_driver(router['so'])

 #Inserindo as credencias de acesso
 device = driver(hostname=router['ip'],username=router['user'],password=router['pass'])

 #Abrindo canal de comunicacao com o device
 device.open()

 #Coletando configuracao
 #get_config() devolve um diccionario com 3 chaves , "candidate", "running", "startup"...vamos utilizar a chave "running"
 output = device.get_config()

 #Salvo a configuraco em um arquivo
 nomearquivo=router['hostname'] + "_config.txt"
 with open(nomearquivo,'w') as fh:
  fh.write(output['running'])

 #Atualizando configuracaco com snmp
 updatefile=router['hostname'] + "_snmp.conf"
 device.load_merge_candidate(filename=updatefile)

 #Verifica as Diferencas
 output=device.compare_config()
 print("--------------------------------------")
 print("Diferencas em %s" % router['hostname'])
 print("--------------------------------------")
 print(output)

 #Aplicas as modificacoes
 device.commit_config()

 #Salvo as novas configuracoeso em um arquivo com extensao _config_new.txt
 #output=device.get_config()
 #newarquivo=router['hostname'] + "_config_new.txt"
 #with open(newarquivo,'w') as fh:
 # fh.write(output['running'])

 #Faco rollback
 #device.rollback() 

 #Fecho conexao
 device.close() 



#END






