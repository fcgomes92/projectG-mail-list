page_request = __import__('getPageHtml')
server_request = __import__('serverSTMP')
import mimetypes
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url = 'http://sites.google.com/site/frinhanimd/disciplinas/sit240'
split1 = 'AVISOS</span></b></font> </div><div>'
split2 = '</div></td>'

login = 'ccf230server@gmail.com'
psswrd = 'qwer123ty'
mail_list = ['fcgomes.92@gmail.com','hannderson.arantes@gmail.com','leonardovillela.c@gmail.com',
'mateusff8@gmail.com','vitorsp7@gmail.com','romerafrv@gmail.com',
]

def make_msg():
	import os
	global login, mail_list, msg
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

msg = page_request.getPage(url, split1, split2)
msg = make_msg()
server_request.enviar_email_gmail(login, psswrd, mail_list, 'Teste', msg)