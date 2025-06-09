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

#Rota: http://127.0.0.1:5000

# ====================== PRODUTOS ======================

@loja_blueprint.route("/produtos", methods=["GET"]) #Exemplo: http://127.0.0.1:5000/produtos
def listarProdutos():
    return jsonify(produtoService.listarProdutos()), 200

@loja_blueprint.route("/produtos/<int:id>", methods=["GET"]) #Exemplo: http://127.0.0.1:5000/produtos/1
def listarProdutoPorId(id):
    return jsonify(produtoService.listarProdutoPorId(id)), 200

@loja_blueprint.route("/produtos", methods=["POST"])
def inserirProduto():
    produtoService.inserirProduto(request.get_json())
    return "Produto inserido", 201

@loja_blueprint.route("/produtos", methods=["PUT"])
def atualizarProduto():
    produtoService.atualizarProduto(request.get_json())
    return "Produto atualizado", 200

@loja_blueprint.route("/produtos/<int:id>", methods=["DELETE"])
def removerProdutoPorId(id):   
    produtoService.removerProdutoPorId(id)
    return "Produto removido", 200

# ====================== VENDAS ======================

@loja_blueprint.route("/vendas", methods=["GET"])
def listarVendas():
    return jsonify(vendaService.listarVendas()), 200

@loja_blueprint.route("/vendas/<int:id>", methods=["GET"])
def listarVendaPorId(id):
    return jsonify(vendaService.listarVendaPorId(id)), 200

@loja_blueprint.route("/vendas", methods=["POST"])
def inserirVenda():
    vendaService.inserirVenda(request.get_json())
    return "Venda inserida", 201

@loja_blueprint.route("/vendas", methods=["PUT"])
def atualizarVenda():
    vendaService.atualizarVenda(request.get_json())
    return "Venda atualizada", 200

@loja_blueprint.route("/vendas/<int:id>", methods=["DELETE"])
def removerVenda(id):
    vendaService.removerVendaPorId(id)
    return "Venda removida", 200

# ====================== CATEGORIAS ======================

@loja_blueprint.route("/categorias", methods=["GET"])
def listarCategorias():
    return jsonify(categoriaService.listarCategoria()), 200

@loja_blueprint.route("/categorias/<int:id>", methods=["GET"])
def listarCategoriaPorId(id):
    return jsonify(categoriaService.listarCategoriaPorId(id)), 200

@loja_blueprint.route("/categorias", methods=["POST"])
def inserirCategoria():
    categoriaService.inserirCategoria(request.get_json())
    return "Categoria inserida", 201

@loja_blueprint.route("/categorias", methods=["PUT"])
def atualizarCategoria():
    categoriaService.atualizarCategoria(request.get_json())
    return "Categoria atualizada", 200

@loja_blueprint.route("/categorias/<int:id>", methods=["DELETE"])
def removerCategoriaPorId(id):   
    categoriaService.removerCategoriaPorId(id)
    return "Categoria removida", 200

# ====================== ITENS DE VENDA ======================

@loja_blueprint.route("/itens_venda", methods=["GET"])
def listarItensVenda():
    return jsonify(itemVendaService.listarItemVendas()), 200

@loja_blueprint.route("/itens_venda/<int:id>", methods=["GET"])
def listarItemVendaPorId(id):
    return jsonify(itemVendaService.listarItemVendaPorId(id)), 200

@loja_blueprint.route("/itens_venda", methods=["POST"])
def inserirItemVenda():
    itemVendaService.inserirItemVenda(request.get_json())
    return "Item de venda inserido", 201

@loja_blueprint.route("/itens_venda", methods=["PUT"])
def atualizarItemVenda():
    itemVendaService.atualizarItemVenda(request.get_json())
    return "Item de venda atualizado", 200

@loja_blueprint.route("/itens_venda/<int:id>", methods=["DELETE"])
def removerItemVendaPorId(id):   
    itemVendaService.removerItemVendaPorId(id)
    return "Item de venda removido", 200

# ====================== USERS ======================

@loja_blueprint.route("/users", methods=["GET"])
def listarUsers():
    return jsonify(userService.listarUser()), 200

@loja_blueprint.route("/users/<int:id>", methods=["GET"])
def listarUserPorId(id):
    return jsonify(userService.listarUserPorId(id)), 200

@loja_blueprint.route("/users", methods=["POST"])
def inserirUser():
    userService.inserirUser(request.get_json())
    return "Usuário inserido", 201

@loja_blueprint.route("/users", methods=["PUT"])
def atualizarUser():
    userService.atualizarUser(request.get_json())
    return "Usuário atualizado", 200

@loja_blueprint.route("/users/<int:id>", methods=["DELETE"])
def removerUserPorId(id):   
    userService.removerUserPorId(id)
    return "Usuário removido", 200