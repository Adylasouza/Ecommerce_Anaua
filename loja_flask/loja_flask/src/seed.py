from datetime import datetime
from os import path

from services.ProdutoService import ProdutoService
from models.Produto import Produto

from services.VendaService import VendaService
from models.Venda import Venda

def initial_seed (): 
    produtoService = ProdutoService ()
    vendaService = VendaService ()

    produtoNovo = Produto ()
    produtoNovo.nome = "hamburguer"
    produtoNovo.quantidade = 8
    produtoNovo.descricao = "lanche imporvisado"
    produtoNovo.preco = 1.00

    produtoService.inserirProduto (produtoNovo)

    vendaNova = Venda ()
    vendaNova.data_venda = datetime.now()
    vendaNova.produto_id = 1
    vendaNova.quantidade = 4

    vendaService.inserirVenda (vendaNova)
    
initial_seed()