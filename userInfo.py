page_request = __import__('getPageHtml')
server_request = __import__('serverSTMP')

url = 'http://sites.google.com/site/frinhanimd/disciplinas/sit240'
split1 = 'AVISOS</span></b></font> </div><div>'
split2 = '</div></td>'

msg = page_request.getPage(url, split1, split2)

login = 'ccf230server@gmail.com'
psswrd = 'qwer123ty'
mail_list = ['fcgomes.92@gmail.com',]

server_request.enviar_email_gmail(login, psswrd, mail_list, 'Teste', msg)