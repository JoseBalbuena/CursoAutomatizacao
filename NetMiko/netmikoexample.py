#!/usr/bin/python3

from netmiko import ConnectHandler

#R1 eh cisco IOS e R2 e JunOS, em R2 definimos uma senha de secret de nula
#O ideal eh que exista um usuario com privilege 15 em R1

R1={'so':'cisco_ios','ip':'1.1.1.1','user':'netmiko','pass':'netmiko','secret':'cisco','configure':['int lo1','ip address 11.11.11.11 255.255.255.0']}
R2={'so':'juniper','ip':'2.2.2.2','user':'netmiko','pass':'netmiko123','secret':'','configure':['set interfaces lo0 unit 0 family inet address 22.22.22.22/24']}

#R1_commands=['int lo1','ip address 11.11.11.11 255.255.255.0']
#R2_commands=['set interfaces lo1 unit 0 family inet address 22.22.22.22/24']


#Lista de diccionarios
MyRouters=[R1,R2]

for router in MyRouters:
 #Definindo Connect Handler
 router_connect=ConnectHandler(device_type=router['so'],ip=router['ip'],username=router['user'],password=router['pass'],secret=router['secret'],timeout=10)
 #Se o roteador eh ios, mudo para enable 
 if router['so'] == 'cisco_ios' :
  router_connect.enable()
 #Envio o comando 
 output=router_connect.send_command('sh version')  
 #Crio o arquivo e armazeno o resultado
 arquivosaida=router['ip'] + '_show_version.txt'
 with open(arquivosaida,'w') as fh:
  fh.write(output)
 #Configurando os roteadores e imprime a saida da configuracao
 output=router_connect.send_config_set(router['configure'])
 print(output)
 #Saio do enable se o roteador eh ios
 if router['so'] == 'cisco_ios' :
  output=router_connect.send_command('wr')
  print(output)
  #Saio do modo enable
  router_connect.exit_enable_mode()
 else:
  # Se o roteador eh Juniper mando um commit
  output=router_connect.commit(and_quit=True)
  print(output)

 #Fecho a conexao
 router_connect.disconnect()
  


