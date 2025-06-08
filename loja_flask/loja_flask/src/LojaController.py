from flask import Flask

from services.ProdutoService import ProdutoService
from services.VendaService import VendaService
from services.CategoriaService import CategoriaService
from services.ItemVendaService import ItemVendaService
from services.Userservice import UserService

app = Flask(__name__)
port = "5000"

produtoService = ProdutoService()
vendaService = VendaService()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>", 201

@app.route ("/produto") #GET http://url/produto
def listarProdutos ():
    listResp = produtoService.listarProdutos ()
    return str(listResp), 200

@app.route ("/produto/int:id") #GET http://url/produto/id
def listarProdutoPorId (request):
    resp = produtoService.listarProdutoPorId (request.id)
    return str(resp), 200

@app.route ("/produto", methods = ["POST"])
def inserirProduto (request):
    produtoService.inserirProduto(request.body)
    return "ok", 200

@app.route ("/produto", methods = ["PUT"])
def atualizarProduto (request):
    produtoService.atualizarProduto (request.body)
    return "ok", 200

@app.route ("/produto/int:id", methods = ["DELETE"])
def removerProdutoPorId (request):   
    produtoService.removerProdutoPorId (request.id)
    return "ok", 200
#_______________________________________________________________________________

@app.route ("/venda") #GET http://url/produto
def listarVendas ():
    listResp = vendaService.listarVendas ()
    return str(listResp), 200

@app.route ("/venda/int:id") #GET http://url/produto/id
def listarVendaPorId (request):
    resp = vendaService.listarVendaPorId (request.id)
    return str(resp), 200

@app.route ("/venda", methods = ["POST"])
def inserirVenda (request):
    vendaService.inserirVenda(request.body)
    return "ok", 200

@app.route ("/venda", methods = ["PUT"])
def atualizarVenda (request):
    vendaService.atualizarVenda (request.body)
    return "ok", 200

@app.route ("/venda/int:id", methods = ["DELETE"])
def removerVenda (request):
    vendaService.removerVendaPorId (request.id)
    return "ok", 200
#_______________________________________________________________________________

@app.route ("/categorias") #GET http://url/categoria
def listarCategoria ():
    listResp = CategoriaService.listarCategoria ()
    return str(listResp), 200

@app.route ("/categorias/int:id") #GET http://url/categorias/id
def listarCategoriaPorId (request):
    resp = CategoriaService.listarCategoriaPorId (request.id)
    return str(resp), 200

@app.route ("/", methods = ["POST"])
def inserirCategoria (request):
    CategoriaService.inserirCategoria(request.body)
    return "ok", 200

@app.route ("/categorias", methods = ["PUT"])
def atualizarCategoria (request):
    CategoriaService.atualizarCategoria (request.body)
    return "ok", 200

@app.route ("/categorias/int:id", methods = ["DELETE"])
def removerCategoriaPorId (request):   
    CategoriaService.removerCategoriaPorId (request.id)
    return "ok", 200
#_______________________________________________________________________________

@app.route ("/item_venda") #GET http://url/item_venda
def listarItemVenda ():
    listResp = ItemVendaService.listarItemVendas ()
    return str(listResp), 200

@app.route ("/item_venda/int:id") #GET http://url/item_venda/id
def listarItemVendaPorId (request):
    resp = ItemVendaService.listarItemVendaPorId (request.id)
    return str(resp), 200

@app.route ("/item_venda", methods = ["POST"])
def inserirItemVenda (request):
    ItemVendaService.inserirItemVenda(request.body)
    return "ok", 200

@app.route ("/item_venda", methods = ["PUT"])
def atualizarItemVenda (request):
    ItemVendaService.atualizarItemVenda (request.body)
    return "ok", 200

@app.route ("/item_venda/int:id", methods = ["DELETE"])
def removerItemVendaPorId (request):   
    ItemVendaService.removerItemVendaPorId (request.id)
    return "ok", 200
#_______________________________________________________________________________

@app.route ("/user") #GET http://url/user
def listarUser ():
    listResp = UserService.listarUser ()
    return str(listResp), 200

@app.route ("/user/int:id") #GET http://url/user/id
def listarUserPorId (request):
    resp = UserService.listarUserPorId(request.id)
    return str(resp), 200

@app.route ("/user", methods = ["POST"])
def inserirUser (request):
    UserService.inserirUser(request.body)
    return "ok", 200

@app.route ("/user", methods = ["PUT"])
def atualizarUser (request):
    UserService.atualizarUser (request.body)
    return "ok", 200

@app.route ("/user/int:id", methods = ["DELETE"])
def removerUserPorId (request):   
    UserService.removerUserPorId (request.id)
    return "ok", 200
#_______________________________________________________________________________
if __name__ == '__main__':
    app.run(port=int(port))
