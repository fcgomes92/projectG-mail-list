#!/usr/env python
''' 
	@author: @fcgomes92
	@date: 2015-02-23
'''
import smtplib
import mimetypes
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
'''.format(', '.join(mail_list),
	login,
	subj,
	msg,
	).encode('utf-8')

	try:
		server.sendmail(login,mail_list,send_msg)
		print ("Email enviado com sucesso!")
	except Exception as e:
   		print ("Falha no envio de email.")
   		print (e)

	server.quit()

def make_msg(login, mail_list, msg):
	import os
	subtype = 'octet-stream'
	# Create the enclosing (outer) message
	outer = MIMEMultipart()
	outer['Subject'] = 'Teste'
	outer['To'] = ', '.join(mail_list)
	outer['From'] = login
	outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

	# Encapsulate the plain and HTML versions of the message body in an
	# 'alternative' part, so message agents can decide which they want to display.
	msgAlt = MIMEMultipart('alternative')
	outer.attach(msgAlt)

	# Coloca texto HTML no MIME
	msg = MIMEText('<h1>AVISOS</h1>'+
		msg+
		'<h1>FIM DOS AVISOS</h1>'+
		'<h2>Olha que fofura!</h2>'+
		'<img src="cid:ornitorrinco">'+
		'<img src="cid:koala">'
		,'html')
	msgAlt.attach(msg)

	# Coloca foto 1 no MIME geral
	fp = open(os.getcwd()+'/img/ornitorrinco.jpg', 'rb')
	msg = MIMEImage(fp.read())
	fp.close()
	msg.add_header('Content-ID', '<ornitorrinco>')
	outer.attach(msg)

    # Coloca foto 2 no MIME geral
	fp = open(os.getcwd()+'/img/koala.jpg','rb')
	msg = MIMEImage(fp.read())
	fp.close()
	msg.add_header('Content-ID', '<koala>')
	outer.attach(msg)

	return outer.as_string()