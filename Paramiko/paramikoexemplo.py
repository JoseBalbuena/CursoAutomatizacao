#!/usr/bin/python

#------------------------------------------------------------
#CODIGO EXEMPLO UTILIZACAO PARAMIKO PARA COLETA DE INFORMACAO
#------------------------------------------------------------

import paramiko
import time


#Funcao que vai enviar o comando e printar a saida

def enviecomandoeprintaresultado(command,client_shell):
 output=""
 #Envia Comando 
 client_shell.send(command)

 #Espera os dados comecarem a chegar
 time.sleep(2)

 #Loop para receber todos os dados do canal
 while True:
  #Se temos dados recebidos envia eles para variavel outbuf
  if client_shell.recv_ready():
   #Recebe dados
   outbuf=client_shell.recv(65535)
   if len(outbuf) == 0:
    raise EOFError("Canal fechado pelo dispositivo remoto")
   #Concatena os dados 
   output += outbuf.decode('utf-8','ignore')
  #Caso nao tenhamos mais dados para receber quebra o laco
  else:
   break

 #Imprime saida 
 print output 


#MAIN

#Definicao dos parametros de conexao do roteador
R1={'ip':'192.168.200.1','user':'automatizacao','pass':'automatizacao'}

#Instancia um ojeto SSH
client_ssh=paramiko.SSHClient()

#Seta politica de autenticacao
client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#Coneta ao roteador R1
client_ssh.connect(R1['ip'],username=R1['user'],password=R1['pass'])

#Invocamos uma shell interativa
client_shell=client_ssh.invoke_shell()

#Enviamos comandos 
command="terminal length 0\n"
enviecomandoeprintaresultado(command,client_shell)
command="sh run\n"
enviecomandoeprintaresultado(command,client_shell)

#Fecha Conexao
client_ssh.close()
