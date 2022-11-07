from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContatos

# Create your views here.
def login(request):
    """Se nada for postado, irá exibir o formulário."""
    if request.method != 'POST':
        # messages.error(request, 'Usuário e senha inválidos.')
        return render(request, 'accounts/login.html')
    
    """Pegar usuário e senha"""
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha1')
    
    """Vai checar se o usuario vai autenticar"""
    user = auth.authenticate(request, username=usuario, password=senha)
    
    if not user:
        """Caso o usuário não log"""
        messages.error(request, 'Usuário inválido.')
        return render(request, 'accounts/login.html')
    
    else:
        """Se o usuário logar"""
        auth.login(request, user)
        messages.success(request, 'Usuário logado.')
        return redirect('dashboard') # Quando o usuário logar, ele será redirecionar para dashboard
        
def logout(request):
    """Quando deslogado, será redirecionado para página do index.html"""
    # return render(request, 'accounts/logout.html')
    auth.logout(request)
    return redirect('index')

def cadastro(request):
    # messages.success(request, 'Por favor realizar cadastro.') Serve para mostrar mensagens
    if request.method != 'POST':
        """Validação do POST"""
        return render(request, 'accounts/cadastro.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha1 = request.POST.get('senha1')
    senha2 = request.POST.get('senha2')
    
    if not nome or not sobrenome or not usuario or not email or not senha1 or not senha2:
        """Validação de campos, se nunhum está vazio."""
        messages.error(request, 'Nenhum campo dode ficar vazio.')
        return render(request, 'accounts/cadastro.html')
    
    if len(usuario) < 6:
        """Validação do usuário"""
        messages.error(request, 'Usuario tem que ter mais que 6 caracteres.')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        """Validação para saber se usuário já existe"""
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/cadastro.html')
    
    try:
        """Validação de email"""
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(email=email).exists():
        """Validação para saber se email já existe"""
        messages.error(request, 'E-mail já existe.')
        return render(request, 'accounts/cadastro.html')
    
    if len(senha1) < 6:
        """Validação do tamanho da senha"""
        messages.error(request, 'Senha não pode ter menos que 6 caracteres.')
        return render(request, 'accounts/cadastro.html')
    
    if senha1 != senha2:
        """Validação da senhas"""
        messages.error(request, 'Senhas com divergências.')
        return render(request, 'accounts/cadastro.html')
            
    messages.success(request, 'Registrado com sucesso! Agora faça login.')
    """Registrar usuario cadastrado no banco de dados"""
    user = User.objects.create_user(
        username=usuario,
        email=email,
        password=senha1,
        first_name=nome,
        last_name=sobrenome)
    user.save()
    
    return redirect('login')

@login_required(redirect_field_name='login') # Se o usuário não logar, ele será redirécionado para login.html
def dashboard(request):
    """Se o usuário logar, ele será direcionado para dashboard.html"""
    formulario = FormContatos()
    return render(request, 'accounts/dashboard.html', { 'form': formulario })

