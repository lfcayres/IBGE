#importando bibliotecas
import requests
import mysql.connector

#conectando no banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abacatee1!",
    database="ibge"
)

#criando cursor e inserindo dados na tabela
cursor = mydb.cursor()
sql = ("INSERT INTO localidade "
               "(mun_id, mun_nome, uf_id, uf_sigla,uf_nome,regiao_id,regiao_nome)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

#def variáveis API
url_localidade = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
r_localidade = requests.get(url_localidade)
localidade_json = r_localidade.json()

for i_localidade in localidade_json:
    val = (i_localidade['id'],
           i_localidade['nome'],
           i_localidade['municipio']['microrregiao']['mesorregiao']['UF']['id'],
           i_localidade['municipio']['microrregiao']['mesorregiao']['UF']['sigla'],
           i_localidade['municipio']['microrregiao']['mesorregiao']['UF']['nome'],
           i_localidade['municipio']['microrregiao']['mesorregiao']['UF']['regiao']['id'],
           i_localidade['municipio']['microrregiao']['mesorregiao']['UF']['regiao']['nome'],
           )
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
cursor.close()



