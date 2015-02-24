import urllib.request

def getPage(url='', split1='', split2=''):
	# Request do código HTML da página
	req = urllib.request.urlopen(url)

	# Decode página para string
	the_page = req.read().decode()

	a = the_page.split(split1)
	b = a[1].split(split2)
	
	return b[0]