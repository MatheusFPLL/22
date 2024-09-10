from django.shortcuts import render, redirect
from .models import Skill, UsuarioSkill, Permissao
from django.contrib.auth.decorators import login_required

@login_required
def listar_skills(request):
    # Pega todas as skills cadastradas
    skills = Skill.objects.all()
    return render(request, 'skills/listar_skills.html', {'skills': skills})

@login_required
def adicionar_skill(request):
    # Verifica se o usuário tem a permissão para editar/adicionar skills
    if not hasattr(request.user, 'permissao') or not request.user.permissao.pode_editar:
        # Redireciona para a lista de skills se o usuário não tiver permissão
        return redirect('listar_skills')

    if request.method == 'POST':
        # Lógica para adicionar skill
        nome_skill = request.POST.get('name')
        descricao_skill = request.POST.get('description')

        # Cria e salva a nova skill no banco de dados
        nova_skill = Skill(name=nome_skill, description=descricao_skill)
        nova_skill.save()

        # Redireciona para a lista de skills após adicionar
        return redirect('listar_skills')

    # Renderiza o formulário para adicionar uma nova skill
    return render(request, 'skills/adicionar_skill.html')

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')









