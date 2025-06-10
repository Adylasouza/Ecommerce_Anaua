from flask import Blueprint, request, jsonify
from services.ProdutoService import ProdutoService
from services.VendaService import VendaService
from services.CategoriaService import CategoriaService
from services.ItemVendaService import ItemVendaService
from services.UserService import UserService

# Cria o Blueprint para as rotas da loja
loja_blueprint = Blueprint('loja', __name__)

# Inicializa os serviços
produtoService = ProdutoService()
vendaService = VendaService()
categoriaService = CategoriaService()
itemVendaService = ItemVendaService()
userService = UserService()

@loja_blueprint.route("/")
def hello_world():
    return "<p>Hello, World!</p>", 200

# ====================== PRODUTOS ======================

@loja_blueprint.route("/produtos", methods=["GET"])
def listarProdutos():
    """
    Lista todos os produtos
    ---
    tags:
      - Produtos
    responses:
      200:
        description: Lista de produtos
        examples:
          application/json: [
            {
              "id": 1,
              "nome": "Produto Exemplo",
              "preco": 100.0,
              "estoque": 10,
              "categoria_id": 1
            }
          ]
    """
    return jsonify(produtoService.listarProdutos()), 200
    
@loja_blueprint.route("/produtos/<int:id>", methods=["GET"])
def listarProdutoPorId(id):
    """
    Retorna um produto específico pelo ID
    ---
    tags:
      - Produtos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: Produto encontrado
        content:
          application/json:
            example:
              {
                "id": 1,
                "nome": "Produto Exemplo",
                "descricao": "Descrição",
                "preco": 100.0,
                "estoque": 10,
                "foto_url": "http://...",
                "categoria_id": 1
              }
      404:
        description: Produto não encontrado
    """
    return jsonify(produtoService.listarProdutoPorId(id)), 200

@loja_blueprint.route("/produtos", methods=["POST"])
def inserirProduto():
    """
    Cria um novo produto
    ---
    tags:
      - Produtos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: Produto
          required:
            - nome
            - preco
            - categoria_id
          properties:
            nome:
              type: string
              example: "Tênis Esportivo"
            descricao:
              type: string
              example: "Tênis confortável para corrida"
            preco:
              type: number
              format: float
              example: 199.90
            estoque:
              type: integer
              example: 20
            foto_url:
              type: string
              example: "http://example.com/imagem.jpg"
            categoria_id:
              type: integer
              example: 1
    responses:
      201:
        description: Produto criado com sucesso
    """
    produtoService.inserirProduto(request.get_json())
    return "Produto inserido", 201

@loja_blueprint.route("/produtos/<int:id>", methods=["PUT"])
def atualizarProduto(id):
    """
    Atualiza um produto existente
    ---
    tags:
      - Produtos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do produto a ser atualizado
      - in: body
        name: body
        required: true
        schema:
          id: Produto
          required:
            - nome
            - preco
            - categoria_id
          properties:
            nome:
              type: string
              example: "Produto Atualizado"
            descricao:
              type: string
              example: "Nova descrição"
            preco:
              type: number
              format: float
              example: 250.00
            estoque:
              type: integer
              example: 15
            foto_url:
              type: string
              example: "http://example.com/atualizado.jpg"
            categoria_id:
              type: integer
              example: 1
    responses:
      200:
        description: Produto atualizado com sucesso
    """
    produtoService.atualizarProduto(id, request.get_json())
    return "Produto atualizado", 200

@loja_blueprint.route("/produtos/<int:id>", methods=["DELETE"])
def removerProdutoPorId(id): 
    """
    Deleta um produto pelo ID
    ---
    tags:
      - Produtos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do produto
    responses:
      200:
        description: Produto deletado com sucesso
        content:
          application/json:
            example:
              { "mensagem": "Produto deletado" }
      404:
        description: Produto não encontrado
    """
    produtoService.removerProdutoPorId(id)
    return "Produto removido", 200

# ====================== VENDAS ======================

@loja_blueprint.route("/vendas", methods=["GET"])
def listarVendas():
    """
    Lista todas as vendas
    ---
    tags:
      - Vendas
    responses:
      200:
        description: Lista de vendas
        content:
          application/json:
            example: [
              {
                "id": 1,
                "usuario_id": 2,
                "data": "2024-06-01T14:35:22",
                "valor_total": 250.75,
                "forma_pagamento": "Cartão de Crédito"
              }
            ]
    """
    return jsonify(vendaService.listarVendas()), 200

@loja_blueprint.route("/vendas/<int:id>", methods=["GET"])
def listarVendaPorId(id):
    """
    Retorna uma venda específica pelo ID
    ---
    tags:
      - Vendas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da venda
    responses:
      200:
        description: Venda encontrada
        content:
          application/json:
            example:
              {
                "id": 1,
                "usuario_id": 2,
                "data": "2024-06-01T14:35:22",
                "valor_total": 250.75,
                "forma_pagamento": "Cartão de Crédito"
              }
      404:
        description: Venda não encontrada
    """
    return jsonify(vendaService.listarVendaPorId(id)), 200

@loja_blueprint.route("/vendas", methods=["POST"])
def inserirVenda():
    """
    Cria uma nova venda
    ---
    tags:
      - Vendas
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: Venda
          required:
            - usuario_id
            - valor_total
            - forma_pagamento
          properties:
            usuario_id:
              type: integer
              example: 2
            valor_total:
              type: number
              format: float
              example: 250.75
            forma_pagamento:
              type: string
              example: "Cartão de Crédito"
    responses:
      201:
        description: Venda criada com sucesso
    """
    vendaService.inserirVenda(request.get_json())
    return "Venda inserida", 201

@loja_blueprint.route("/vendas/<int:id>", methods=["PUT"])
def atualizarVenda(id):
    """
    Atualiza uma venda existente
    ---
    tags:
      - Vendas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da venda
      - in: body
        name: body
        required: true
        schema:
          id: Venda
          required:
            - usuario_id
            - valor_total
            - forma_pagamento
          properties:
            usuario_id:
              type: integer
              example: 2
            valor_total:
              type: number
              format: float
              example: 280.00
            forma_pagamento:
              type: string
              example: "Pix"
    responses:
      200:
        description: Venda atualizada com sucesso
    """
    vendaService.atualizarVenda(id, request.get_json())
    return "Venda atualizada", 200

@loja_blueprint.route("/vendas/<int:id>", methods=["DELETE"])
def removerVenda(id):
    """
    Deleta uma venda pelo ID
    ---
    tags:
      - Vendas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da venda
    responses:
      200:
        description: Venda deletada com sucesso
        content:
          application/json:
            example:
              { "deleted": true }
      404:
        description: Venda não encontrada
    """
    vendaService.removerVendaPorId(id)
    return "Venda removida", 200

# ====================== CATEGORIAS ======================

@loja_blueprint.route("/categorias", methods=["GET"])
def listarCategorias():
    """
    Lista todas as categorias
    ---
    tags:
      - Categorias
    responses:
      200:
        description: Lista de categorias
        examples:
          application/json: [
            {
              "id": 1,
              "nome": "Eletrônicos",
              "descricao": "Dispositivos eletrônicos",
              "codigo": "ELEC"
            }
          ]
    """
    return jsonify(categoriaService.listarCategoria()), 200

@loja_blueprint.route("/categorias/<int:id>", methods=["GET"])
def listarCategoriaPorId(id):
    """
    Retorna uma categoria específica pelo ID
    ---
    tags:
      - Categorias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
    responses:
      200:
        description: Categoria encontrada
        content:
          application/json:
            example:
              {
                "id": 1,
                "nome": "Eletrônicos",
                "descricao": "Dispositivos eletrônicos",
                "codigo": "ELEC"
              }
      404:
        description: Categoria não encontrada
    """
    return jsonify(categoriaService.listarCategoriaPorId(id)), 200

@loja_blueprint.route("/categorias", methods=["POST"])
def inserirCategoria():
    """
    Cria uma nova categoria
    ---
    tags:
      - Categorias
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: Categoria
          required:
            - nome
            - codigo
          properties:
            nome:
              type: string
              example: "Livros"
            descricao:
              type: string
              example: "Livros e revistas"
            codigo:
              type: string
              example: "LIVR"
    responses:
      201:
        description: Categoria criada com sucesso
        content:
          application/json:
            example:
              {
                "id": 2,
                "nome": "Livros",
                "descricao": "Livros e revistas",
                "codigo": "LIVR"
              }
    """
    categoriaService.inserirCategoria(request.get_json())
    return "Categoria inserida", 201

@loja_blueprint.route("/categorias/<int:id>", methods=["PUT"])
def atualizarCategoria(id):
    """
    Atualiza uma categoria existente
    ---
    tags:
      - Categorias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
      - in: body
        name: body
        required: true
        schema:
          id: Categoria
          required:
            - nome
            - codigo
          properties:
            nome:
              type: string
              example: "Eletrônicos e Gadgets"
            descricao:
              type: string
              example: "Atualizado"
            codigo:
              type: string
              example: "ELECGAD"
    responses:
      200:
        description: Categoria atualizada com sucesso
        content:
          application/json:
            example:
              {
                "id": 1,
                "nome": "Eletrônicos e Gadgets",
                "descricao": "Atualizado",
                "codigo": "ELECGAD"
              }
      404:
        description: Categoria não encontrada
    """
    categoriaService.atualizarCategoria(id, request.get_json())
    return "Categoria atualizada", 200

@loja_blueprint.route("/categorias/<int:id>", methods=["DELETE"])
def removerCategoriaPorId(id):
    """
    Deleta uma categoria pelo ID
    ---
    tags:
      - Categorias
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da categoria
    responses:
      200:
        description: Categoria deletada com sucesso
        content:
          application/json:
            example:
              { "deleted": true }
      404:
        description: Categoria não encontrada
    """
    categoriaService.removerCategoriaPorId(id)
    return "Categoria removida", 200

# ====================== ITENS DE VENDA ======================

@loja_blueprint.route("/itens-venda", methods=["GET"])
def listarItensVenda():
    """
    Lista todos os itens de venda
    ---
    tags:
      - Itens de Venda
    responses:
      200:
        description: Lista de itens de venda
        examples:
          application/json: [
            {
              "id": 1,
              "venda_id": 3,
              "produto_id": 5,
              "quantidade": 2,
              "preco_unitario": 50.0
            }
          ]
    """
    return jsonify(itemVendaService.listarItemVendas()), 200

@loja_blueprint.route("/itens-venda/<int:id>", methods=["GET"])
def listarItemVendaPorId(id):
    """
    Retorna um item de venda específico pelo ID
    ---
    tags:
      - Itens de Venda
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do item de venda
    responses:
      200:
        description: Item de venda encontrado
        content:
          application/json:
            example:
              {
                "id": 1,
                "venda_id": 3,
                "produto_id": 5,
                "quantidade": 2,
                "preco_unitario": 50.0
              }
      404:
        description: Item de venda não encontrado
    """
    return jsonify(itemVendaService.listarItemVendaPorId(id)), 200

@loja_blueprint.route("/itens-venda", methods=["POST"])
def inserirItemVenda():
    """
    Cria um novo item de venda
    ---
    tags:
      - Itens de Venda
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: ItemVenda
          required:
            - venda_id
            - produto_id
            - quantidade
            - preco_unitario
          properties:
            venda_id:
              type: integer
              example: 3
            produto_id:
              type: integer
              example: 5
            quantidade:
              type: integer
              example: 2
            preco_unitario:
              type: number
              format: float
              example: 50.0
    responses:
      201:
        description: Item de venda criado com sucesso
        content:
          application/json:
            example:
              {
                "id": 7,
                "venda_id": 3,
                "produto_id": 5,
                "quantidade": 2,
                "preco_unitario": 50.0
              }
    """
    itemVendaService.inserirItemVenda(request.get_json())
    return "Item de venda inserido", 201

@loja_blueprint.route("/itens-venda/<int:id>", methods=["PUT"])
def atualizarItemVenda(id):
    """
    Atualiza um item de venda existente
    ---
    tags:
      - Itens de Venda
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do item de venda
      - in: body
        name: body
        required: true
        schema:
          id: ItemVenda
          required:
            - venda_id
            - produto_id
            - quantidade
            - preco_unitario
          properties:
            venda_id:
              type: integer
              example: 3
            produto_id:
              type: integer
              example: 5
            quantidade:
              type: integer
              example: 3
            preco_unitario:
              type: number
              format: float
              example: 55.0
    responses:
      200:
        description: Item de venda atualizado com sucesso
        content:
          application/json:
            example:
              {
                "id": 1,
                "venda_id": 3,
                "produto_id": 5,
                "quantidade": 3,
                "preco_unitario": 55.0
              }
      404:
        description: Item de venda não encontrado
    """
    itemVendaService.atualizarItemVenda(id, request.get_json())
    return "Item de venda atualizado", 200

@loja_blueprint.route("/itens-venda/<int:id>", methods=["DELETE"])
def removerItemVendaPorId(id):
    """
    Deleta um item de venda pelo ID
    ---
    tags:
      - Itens de Venda
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do item de venda
    responses:
      200:
        description: Item de venda deletado com sucesso
        content:
          application/json:
            example:
              { "deleted": True }
      404:
        description: Item de venda não encontrado
    """
    itemVendaService.removerItemVendaPorId(id)
    return "Item de venda removido", 200

# ====================== USERS ======================

@loja_blueprint.route("/users", methods=["GET"])
def listarUsers():
    """
    Lista todos os usuários.
    ---
    tags:
      - Usuários
    responses:
      200:
        description: Lista de usuários retornada com sucesso
        content:
          application/json:
            example: [
              {
                "id": 1,
                "username": "joao123",
                "name": "João da Silva"
              }
            ]
    """
    return jsonify(userService.listarUsers()), 200

@loja_blueprint.route("/users/<int:id>", methods=["GET"])
def listarUserPorId(id):
    """
    Lista um usuário pelo ID.
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário encontrado
        content:
          application/json:
            example:
              {
                "id": 1,
                "username": "joao123",
                "name": "João da Silva"
              }
      404:
        description: Usuário não encontrado
    """
    return jsonify(userService.listarUserPorId(id)), 200

@loja_blueprint.route("/users", methods=["POST"])
def inserirUser():
    """
    Insere um novo usuário.
    ---
    tags:
      - Usuários
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: Usuario
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: "joao123"
            password:
              type: string
              example: "123456"
            name:
              type: string
              example: "João da Silva"
    responses:
      201:
        description: Usuário criado com sucesso
    """
    userService.inserirUser(request.get_json())
    return "Usuário inserido", 201

@loja_blueprint.route("/users/<int:id>", methods=["PUT"])
def atualizarUser(id):
    """
    Atualiza um usuário existente.
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          id: Usuario
          properties:
            username:
              type: string
              example: "joao123"
            password:
              type: string
              example: "novaSenha"
            name:
              type: string
              example: "João Atualizado"
    responses:
      200:
        description: Usuário atualizado com sucesso
      404:
        description: Usuário não encontrado
    """
    userService.atualizarUser(id, request.get_json())
    return "Usuário atualizado", 200

@loja_blueprint.route("/users/<int:id>", methods=["DELETE"])
def removerUserPorId(id):
    """
    Remove um usuário pelo ID.
    ---
    tags:
      - Usuários
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do usuário
    responses:
      200:
        description: Usuário removido com sucesso
      404:
        description: Usuário não encontrado
    """
    userService.removerUserPorId(id)
    return "Usuário removido", 200