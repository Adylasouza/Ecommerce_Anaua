from flask import Flask

from services.ProdutoService import ProdutoService
from services.VendaService import VendaService

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

if __name__ == '__main__':
    app.run(port=int(port))
