import requests

cabecalho = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36", 
             "Cookie": "cf_clearance=VzKib_rP.4fDO6o5iNI6Q9_YyzlVBNF2BLiSJ6lKf.M-1684853800-0-250"}

dados = {"user": "admin", "password": "senhafoda"}

resposta = requests.get("http://www.bancocn.com", headers=cabecalho)
html_get = resposta.text
print(html_get)

resposta = requests.post("http://www.bancocn.com/admin/index.php", headers=cabecalho, data=dados)
html_post = resposta.text
print(html_post)