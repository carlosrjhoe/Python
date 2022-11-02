from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    
    contatos = Contato.objects.order_by('id').filter()
    paginator = Paginator(contatos, 5)
    
    paginas = request.GET.get('paginas')
    contatos = paginator.get_page(paginas)
    
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    """Responsável por mostrar os contatos"""
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)
    
    # if not contato.mostrar:
    #     raise Http404()
    
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
    
def busca(request):
    """Responsável por fazer uma busca pelo nome e sobrenome"""
    termo = request.GET.get('termo')
    
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'Campo termo não pode ficar vazio.')
        # messages.add_message(request, messages.SUCCESS, 'Messagem de sucesso.')
        return redirect('index')
    
    contatos = Contato.objects.order_by('id').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
        mostrar=True
    )
    
    paginator = Paginator(contatos, 5)
    
    paginas = request.GET.get('paginas')
    
    contatos = paginator.get_page(paginas)
    
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })