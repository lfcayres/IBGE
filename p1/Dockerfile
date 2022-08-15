#criar dockerfile
FROM python:3.9.12

ADD dados_pessoa.py localidade.py testes.py .

RUN pip install request mysql.connector

CMD ["python" dados_pessoa.py"]

