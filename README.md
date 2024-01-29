<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sales Data Processing and Email Automation</title>
</head>
<body>

<h1>Processamento Automático de Dados de Vendas e Automação de E-mails</h1>

<h2>Visão Geral</h2>

<p>Este script em Python automatiza o processo de consolidação de dados de vendas de arquivos CSV, gera um relatório abrangente em Excel e envia uma notificação por e-mail com o relatório de vendas atualizado anexado. O script utiliza a biblioteca Pandas para manipulação de dados e o módulo smtplib para funcionalidades de e-mail.</p>

<h2>Índice</h2>

<ul>
  <li><a href="#utilizacao">Utilização</a></li>
  <li><a href="#configuracao">Configuração</a></li>
  <li><a href="#consideracoes-de-seguranca">Considerações de Segurança</a></li>
  <li><a href="#contribuicoes">Contribuições</a></li>
  <li><a href="#licenca">Licença</a></li>
</ul>

<h2 id="utilizacao">Utilização</h2>

<ol>
  <li><strong>Clonar o Repositório:</strong>
    <pre><code>git clone https://github.com/UnderClany/Automacao_Com_Planilhas_e_Email_SMTP.git
cd Automacao_Com_Planilhas_e_Email_SMTP</code></pre>
  </li>
  
  <li><strong>Instalar Dependências:</strong>
    <pre><code>pip install pandas</code></pre>
  </li>
  
  <li><strong>Configurar o E-mail:</strong>
    <ul>
      <li>Atualize o endereço do remetente do e-mail (<code>msg['From']</code>) no script.</li>
      <li>Defina os endereços de destinatários de e-mail na lista <code>msg['To']</code>.</li>
    </ul>
  </li>
  
  <li><strong>Definir Senha do Gmail:</strong>
    <ul>
      <li>Configure a senha do Gmail de forma segura usando uma variável de ambiente (<code>GMAIL_PASSWORD</code>).
        <pre><code>export GMAIL_PASSWORD=sua_senha_do_gmail</code></pre>
        <strong>Observação:</strong> Por motivos de segurança, não inclua informações confidenciais diretamente no código.
      </li>
    </ul>
  </li>
  
  <li><strong>Executar o Script:</strong>
    <pre><code>python script_name.py</code></pre>
  </li>
  
  <li><strong>Verificar Saída:</strong>
    <ul>
      <li>Os dados consolidados de vendas serão salvos como 'Vendas.xlsx' no diretório de trabalho atual.</li>
      <li>Uma notificação por e-mail será enviada aos destinatários especificados.</li>
    </ul>
  </li>
</ol>

<h2 id="configuracao">Configuração</h2>

<ul>
  <li><strong>Configuração de E-mail:</strong>
    <ul>
      <li>Atualize o endereço do remetente do e-mail (<code>msg['From']</code>).</li>
      <li>Especifique os endereços de destinatários de e-mail na lista <code>msg['To']</code>.</li>
    </ul>
  </li>
  
  <li><strong>Senha do Gmail:</strong>
    <ul>
      <li>Configure a senha do Gmail de forma segura usando uma variável de ambiente (<code>GMAIL_PASSWORD</code>).
        <pre><code>export GMAIL_PASSWORD=sua_senha_do_gmail</code></pre>
        <strong>Observação:</strong> Por motivos de segurança, não inclua informações confidenciais diretamente no código.
      </li>
    </ul>
  </li>
</ul>

<h2 id="consideracoes-de-seguranca">Considerações de Segurança</h2>

<ul>
  <li><strong>Informações Sensíveis:</strong>
    <ul>
      <li>Não inclua informações sensíveis (por exemplo, senhas) diretamente no script.</li>
      <li>Utilize variáveis de ambiente ou um método de configuração seguro.</li>
    </ul>
  </li>
  
  <li><strong>Configurações do Gmail:</strong>
    <ul>
      <li>Ative o "Acesso a apps menos seguros" para a conta do Gmail usada no script.</li>
      <li>Se estiver usando autenticação de dois fatores, gere uma "Senha de Aplicativo" e configure-a de forma segura.</li>
    </ul>
  </li>
</ul>

<h2 id="contribuicoes">Contribuições</h2>

<p>Sinta-se à vontade para contribuir para o projeto abrindo problemas ou enviando solicitações de pull. Seu feedback e melhorias são bem-vindos!</p>

<h2 id="licenca">Licença</h2>

<p>Este projeto está licenciado sob a <a href="LICENSE">Licença MIT</a>.</p>

</body>
</html>
