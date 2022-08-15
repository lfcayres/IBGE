#importando biblioteca
import requests

#definindo variáveis
url_localidade = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
url_dados = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes'
r_localidade = requests.get(url_localidade)
r_dados = requests.get(url_dados)

#imprimindo teste id
print(r_localidade.status_code)
print(r_dados.status_code)