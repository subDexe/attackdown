from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import request
from django.contrib.auth.decorators import login_required

from .models import Produto
from .forms import ProdutoForm
from carrinho.forms import CarrinhoAddProdutoForm

# Create your views here.
@login_required(login_url='/accounts/login')
def novo_produto(request):
    context = {}
    produto_form = ProdutoForm(request.POST or None)
    if produto_form.is_valid():
        produto = produto_form.save()
        produto.save()
        produto_form = Produto()
        return redirect("/produto/lista")
    context['produto_form'] = produto_form
    return render(request, 'produto.html', context)

@login_required(login_url='/accounts/login')
def lista_produtos(request):
    queryset = Produto.objects.all()
    context = {
        'produtos':queryset,
        'form':CarrinhoAddProdutoForm(),
    }
    print(queryset)
    return render(request, 'lista-produtos.html', context)

@login_required(login_url='/accounts/login')
def editar_produto(request, id_produto):
    context = {}
    produto = get_object_or_404(Produto, produto_id=id_produto)
    if request.POST:
        editar_form = ProdutoForm(request.POST, instance=produto)
        if editar_form.is_valid():
            produto = editar_form.save()
            produto.save()
            return redirect("/produto/lista")
    else:
        editar_form = ProdutoForm(instance=produto)
        context['produto'] = editar_form
    return render(request, 'editar-produto.html', context)