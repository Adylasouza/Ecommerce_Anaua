# Anauá E-commerce

Este é um projeto web desenvolvido com [Flask](https://flask.palletsprojects.com/) que serve como base para um sistema de e-commerce.

## 🚀 Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) — Framework web leve e flexível em Python
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) — ORM para integração com bancos de dados
- [Flasgger](https://github.com/flasgger/flasgger) — Geração de documentação Swagger para APIs
- [SQLite](https://sqlite.org/) — Banco de dados leve usado para testes
- [Jinja2](https://jinja.palletsprojects.com/) — Engine de templates usada pelo Flask

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/anaua_ecommerce.git
   cd anaua_ecommerce
   ```

2. Crie um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o projeto:

    Para iniciar o servidor Flask em modo de desenvolvimento:

    ```bash
    python run.py
    ```

5. Acesse no navegador:

    A aplicação será iniciada em:

    ```bash
    http://127.0.0.1:5000/
    ```

6. Documentação Swagger (auto-gerada):

    ```bash
    http://127.0.0.1:5000/apidocs
    ```

## 📁 Estrutura Básica

```
anaua_ecommerce/
│
├── app/
│   ├── __init__.py          # Criação da app Flask + Swagger
│   ├── models/              # Modelos do banco (Produto, Venda, etc.)
│   ├── services/            # Lógica de negócios isolada (ProdutoService, VendaService...)
│   └── routes/              # Rotas e endpoints organizados
│
├── migrations/              # Controle de migrações do banco
├── run.py                   # Arquivo principal para iniciar a aplicação
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo
```

## ✅ Funcionalidades Implementadas

✔️ Cadastro e listagem de Produtos
✔️ Cadastro e consulta de Categorias
✔️ Vendas e controle de Itens por Venda
✔️ Gestão de Usuários (cadastro, edição, exclusão)
✔️ Integração Swagger (via Flasgger) para testes de API
✔️ Banco de dados SQLite pronto para uso
✔️ Separação real das camadas (MVC)

## 📝 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT). Sinta-se livre para usá-lo, modificá-lo e distribuí-lo.

## 🔌 Endpoints da API REST

#### `/produto`
| Método | Rota                | Descrição                   |
|--------|---------------------|-----------------------------|
| GET    | `/`                 | Lista todos os produtos     |
| GET    | `/<int:produto_id>` | Busca um produto específico |
| POST   | `/`                 | Cria um novo produto        |
| PUT    | `/<int:produto_id>` | Atualiza um produto         |
| DELETE | `/<int:produto_id>` | Remove um produto           |

✔️ Campos obrigatórios: nome, preco, categoria_id
✔️ Suporta estoque, foto_url, descrição.

#### `/users`
| Método | Rota          | Descrição                     |
|--------|---------------|-------------------------------|
| GET    | `/`           | Lista todos os usuários       |
| GET    | `/<int:id>`   | Busca um usuário específico   |
| POST   | `/`           | Cria um novo usuário          |
| PUT    | `/<int:id>`   | Atualiza dados do usuário     |
| DELETE | `/<int:id>`   | Remove um usuário             |

✔️ Campos obrigatórios: username, password
✔️ Campos opcionais: name

#### `/venda`
| Método | Rota          | Descrição                   |
|--------|---------------|-----------------------------|
| GET    | `/`           | Lista todas as vendas       |
| GET    | `/<int:id>`   | Busca uma venda específica  |
| POST   | `/`           | Cria uma nova venda         |
| PUT    | `/<int:id>`   | Atualiza uma venda          |
| DELETE | `/<int:id>`   | Remove uma venda            |

✔️ Campos obrigatórios: usuario_id, valor_total, forma_pagamento

#### `/categoria`
| Método | Rota            | Descrição                      |
|--------|-----------------|--------------------------------|
| GET    | `/`             | Lista todas as categorias      |
| GET    | `/<int:id>`     | Busca uma categoria específica |
| POST   | `/`             | Cria uma nova categoria        |
| PUT    | `/<int:id>`     | Atualiza uma categoria         |
| DELETE | `/<int:id>`     | Remove uma categoria           |

✔️ Campos obrigatórios: nome, codigo

#### `/itens-venda`
| Método | Rota            | Descrição                           |
|--------|-----------------|-------------------------------------|
| GET    | `/`             | Lista todos os itens de venda       |
| GET    | `/<int:id>`     | Retorna um item de venda específico |
| POST   | `/`             | Cria um novo item de venda          |
| PUT    | `/<int:id>`     |Atualiza um item de venda existente  |
| DELETE | `/<int:id>`     | Remove um item de venda             |

✔️ Campos obrigatórios: venda_id, produto_id, quantidade, preco_unitario

📌 Observações

Para alterar o banco, edite o arquivo de configuração em app/__init__.py.

Documentação Swagger acessível em http://127.0.0.1:5000/apidocs

Testado com Python 3.12+ e Flask 3.1+

