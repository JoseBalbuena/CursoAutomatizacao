#!/usr/bin/python

from netmiko import ConnectHandler

#R1 eh cisco IOS e R2 e JunOS, em R2 definimos uma senha de secret de nula
#O ideal eh que exista um usuario com privilege 15 em R1
R1={'so':'cisco_ios','hostname':'R1','ip':'1.1.1.1','user':'netmiko','pass':'netmiko','secret':'cisco','command':'show run'}
R2={'so':'juniper','hostname':'R2','ip':'2.2.2.2','user':'netmiko','pass':'netmiko123','secret':'','command':'show configuration'}

#Lista Vazia onde seram armazenados os comandos de configuracao dos arquivos
comandosdeconf=[]

#Lista de diccionarios
MyRouters=[R1,R2]

for router in MyRouters:
 #Definindo Connect Handler
 router_connect=ConnectHandler(device_type=router['so'],ip=router['ip'],username=router['user'],password=router['pass'],secret=router['secret'],timeout=10)

 #Se o roteador eh ios, mudo para enable 
 if router['so'] == 'cisco_ios' :
  router_connect.enable()

 #Envio o comando 
 output=router_connect.send_command(router['command'])  

 #Crio o arquivo e armazeno o resultado
 arquivosaida=router['ip'] + '.txt'
 with open(arquivosaida,'w') as fh:
  fh.write(output)
 
 #Saio do enable se eh Cisco IOS
 if router['so'] == 'cisco_ios' :
  router_connect.exit_enable_mode()

 #Leio o arquivos Rx_bgp.conf
 nomearquivo=router['hostname'] + '_bgp.conf'
 with open(nomearquivo,'r') as fh:
  for line in fh:
   line2=line.strip('\n')
   comandosdeconf.append(line2)
 print("------------------------------------------------------------")
 print("Enviandos os seguintes comandos para %s" % router['hostname'])
 print comandosdeconf 

 #Enviar os comandos de configuracao
 if router['so'] == 'cisco_ios' :
  router_connect.enable()
 router_connect.send_config_set(comandosdeconf)

 if router['so'] == 'cisco_ios' :
  router_connect.send_command('wr')
  #Saio do modo enable
  router_connect.exit_enable_mode()
 else:
  # Se o roteador eh Juniper mando um commit e saiu do configure
  router_connect.commit(and_quit=True)
 
 
 #Fecho a conexao e zero a lista de comandos
 comandosdeconf=[]
 router_connect.disconnect()
  



