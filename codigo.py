import os
import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Processar dados e salvar em um arquivo Excel
caminho = 'bases'
arquivos = os.listdir(caminho)

tabela_consolidada = pd.DataFrame()

for nome_arquivo in arquivos:
    tabela_vendas = pd.read_csv(os.path.join(caminho, nome_arquivo))
    tabela_vendas['Datas de Venda'] = pd.to_datetime('01/01/1900') + pd.to_timedelta(tabela_vendas['Data de Venda'],
                                                                                     unit='d')
    tabela_consolidada = pd.concat([tabela_consolidada, tabela_vendas])

tabela_consolidada = tabela_consolidada.sort_values(by='Data de Venda')
tabela_consolidada = tabela_consolidada.reset_index(drop=True)
nome_arquivo_excel = 'Vendas.xlsx'
tabela_consolidada.to_excel(nome_arquivo_excel, index=False)

# Enviar e-mail com anexo
def enviar_email():
    data_hoje = datetime.today().strftime('%d/%m/%Y')
    corpo_email = f"""
    <p>Prezados,</p>
    <p>Segue em anexo o Relatório de Vendas de {data_hoje} atualizado.</p>
    <p>Qualquer coisa estou à disposição.</p>
    <p>Abs,</p>
    <p><b>Daniel Augusto Pinto Pereira Junior</b></p>
    """

    # Configurar o objeto MIME para o e-mail
    msg = MIMEMultipart()
    msg['Subject'] = f"Relatório de Vendas {data_hoje}"
    msg['From'] = 'seu email'
    msg['To'] = ', '.join(['sua@dfdfd.com', 'lista@hfdd.com', 'de@gfgofgf.com' , 'e-mail@gfkfjf.com'])  # Fix here
    msg.attach(MIMEText(corpo_email, 'html'))

    # Anexar o arquivo Excel
    caminho_anexo = os.path.join(os.getcwd(), nome_arquivo_excel)
    with open(caminho_anexo, 'rb') as anexo:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(anexo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(caminho_anexo)}')
        msg.attach(parte)

    # Configurar o SMTP e enviar o e-mail
    senha = 'senha gerada no google'
    with smtplib.SMTP('smtp.gmail.com:587') as s:
        s.starttls()
        s.login(msg['From'], senha)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    print('E-mail enviado')

enviar_email()
