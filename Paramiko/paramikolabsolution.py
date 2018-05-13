#!/usr/bin/python

#############################################################
# LABORATORIO 9 - UTILIZANDO PARAMIKO
#############################################################

import paramiko
import time


def sendandreceive(comando,shell):
 output=""
 shell.send(comando)
 time.sleep(1)
 while True:
  if shell.recv_ready():
   outbuf = shell.recv(65535)
   if len(outbuf) == 0:
    raise EOFError("Erro no canal de dados SSH")
   output += outbuf.decode('utf-8','ignore')
  else:
   break
  return output  


#MAIN

R1={'ip':'1.1.1.1','user':'paramiko','pass':'paramiko','secret':'cisco'}

ArquivoSaida = "/home/osboxes/MeusScripts/R1_paramiko.txt"

resultado=""

R1_bgp_config=['enable\n',R1['secret'] + '\n','conf term\n','router bgp 100\n','neighbor 2.2.2.2 remote-as 200\n','neighbor 2.2.2.2 update-source loopback 0\n','network 1.1.1.0 mask 255.255.255.0\n','network 192.168.200.0 mask 255.255.255.0\n','end\n','wr\n','yes\n','exit\n']

#Criando um objeto SSHClient
R1_ssh = paramiko.SSHClient()

#Setando politicas de chave
R1_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Conetando ao roteador
R1_ssh.connect(R1['ip'],username=R1['user'],password=R1['pass'])

#Criando uma shell interativa
R1_shell = R1_ssh.invoke_shell()

#Terminal length para saida nao vir por partes
resultado=sendandreceive('terminal length 0\n',R1_shell)

#Armazenando resultado em um arquivo
resultado=sendandreceive('sh ip int bri \n',R1_shell)

with open(ArquivoSaida,'w') as fh:
 fh.write(resultado)

#Configurando BGP

#resultado=sendandreceive('enable \n',R1_shell)
#resultado=sendandreceive(R1['secret'] + '\n',R1_shell)
#resultado=sendandreceive('conf t',R1_shell)

for command in R1_bgp_config: 
 resultado=sendandreceive(command,R1_shell)
 #print resultado

#Fechando conexao
R1_ssh.close()
