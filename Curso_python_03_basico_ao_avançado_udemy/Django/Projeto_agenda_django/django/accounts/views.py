from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

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

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

