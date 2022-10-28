from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q

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
    contatos = Contato.objects.order_by('id').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),
        mostrar=True
    )
    
    paginator = Paginator(contatos, 5)
    paginas = request.GET.get('paginas')
    contatos = paginator.get_page(paginas)
    
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })