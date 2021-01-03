import urllib
import urllib.request

try:
    url = urllib.request.urlopen('http://pudim.com.br/')
except(urllib.error.URLError):
    print("O site Pudim não está acessivel no momento. Verifique sua conexão.")
else:
    print("Tudo ok.")    
    print(url.getcode())