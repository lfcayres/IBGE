#importando biblioteca
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
sql = ("INSERT INTO dados_pessoa "
               "(nome_pessoa, regiao, freq)"
               "VALUES (%s, %s, %s)")

# #definindo variaveis API
url_nome = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes'
r_dados_pessoa = requests.get(url_nome)
dados_json = r_dados_pessoa.json()



for i_dados in dados_json:
    val1 = (i_dados['nome'],
           i_dados['regiao'],
           i_dados['freq']
           )
    cursor.execute(sql, val1)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
cursor.close()


