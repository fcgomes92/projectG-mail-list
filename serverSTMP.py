#!/usr/env python
''' 
	@author: @fcgomes92
	@date: 2015-02-23
'''
import smtplib

def enviar_email_gmail(login='',psswrd='',mail_list=[], subj='Server mail', msg=''):

	server = smtplib.SMTP('smtp.gmail.com', 587) 
	
	server.ehlo() 
	
	server.starttls()

	# Login no email que irá enviar a msg original
	server.login(login,psswrd)

	# Compõe a msg
	send_msg = '''To: <{}>
From: <{}>
Subject: [{}]
{}
'''.format(login,
	mail_list.__str__().replace('[','').replace(']',''),
	subj,
	msg
	).encode('utf-8')

	try:
		server.sendmail(login,mail_list,send_msg)
		print ("Email enviado com sucesso!")
	except Exception as e:
   		print ("Falha no envio de email.")
   		print (e)

	server.quit()