# Pegho Recrutamento

Projeto de sistema de recrutamento feito com Django, onde candidatos podem enviar informações como dados pessoais, contato, experiência profissional e formação acadêmica para serem avaliados pela equipe de recrutamento da empresa Pegho.

## Funcionalidades

- Cadastro de dados pessoais
- Cadastro de experiência profissional e formação acadêmica
- Adição dinâmica de múltiplas experiências e formações
- Gerenciamento das informações pelo Django Admin

## Tecnologias Utilizadas

- **Django** 5.1.2
- **SQLite** (banco de dados padrão do Django)
- **Bootstrap** (para estilização básica)
- **HTML/CSS** para templates front-end

## Pré-requisitos

Certifique-se de ter o Python e o Git instalados no seu sistema.

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/pegho-recrutamento.git
   cd pegho-recrutamento
    ```
2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
    ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
    ```
4. **Configuração do ambiente:**
- Crie um arquivo .env na raiz do projeto e adicione as variáveis de ambiente necessárias
5. **Realize as migrações do banco de dados:**
  ```bash
  python manage.py migrate
   ```
  
## Uso

1. **Página Principal:**  
   O candidato pode preencher o formulário de recrutamento diretamente na página inicial.

2. **Administração:**  
   Para acessar o Django Admin e gerenciar os dados cadastrados:
   - Crie um superusuário com o comando: 
     ```bash
     python manage.py createsuperuser
     ```
   - Acesse [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) usando as credenciais do superusuário.

### Apagando Cadastros em Massa
Para apagar todos os dados de uma vez no Django Admin:
- Navegue até a seção de dados desejada (como Experiência Profissional ou Formação Acadêmica).
- Selecione todos os itens utilizando a caixa de seleção.
- No menu de ações, escolha "Excluir selecionados" e confirme a exclusão.

## Estrutura de Arquivos

- `dados/` - Aplicação principal do Django para o formulário de recrutamento.
- `templates/` - Contém os templates HTML para renderização das páginas.
- `static/` - Arquivos estáticos como CSS e imagens para o front-end.
- `manage.py` - Script de comando para interações com o projeto Django.

## Dependências

As dependências principais do projeto estão listadas no arquivo `requirements.txt`. As principais incluem:

- `Django==5.1.2`
- `python-dotenv==1.0.1` (para configuração de variáveis de ambiente)
- `sqlparse==0.5.1` (usado pelo Django para consultas SQL)
