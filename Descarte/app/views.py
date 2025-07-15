from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .models import Usuario
from .models import Substancia
from .forms import UsuarioForm  # crie esse formulário
from .models import Alerta
from .models import ConteudoEducativo


class CriarConteudoView(CreateView):
    model = ConteudoEducativo
    template_name = 'criar_conteudo.html'
    fields = ['titulo', 'descricao']  # coloque os campos do seu modelo
    success_url = reverse_lazy('nome_da_pagina_que_redireciona')
    
class DeletarUsuarioView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios')  # nome da lista de usuários
    template_name = 'confirmar_delecao.html'

class EditarUsuarioView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'editar_usuario.html'
    success_url = reverse_lazy('usuarios')

class CriarUsuarioView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'criar_usuario.html'
    success_url = reverse_lazy('usuarios')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class UsuarioView(View):
    def get(self, request):
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios.html', {'usuarios': usuarios})
class CriarPontoColetaView(CreateView):
    model = PontoColeta
    fields = ['nome', 'endereco']  # ou os campos que desejar
    template_name = 'criar_ponto.html'
    success_url = reverse_lazy('pontos_coleta')


class PontoColetaView(View):
    def get(self, request):
        pontos = PontoColeta.objects.all()
        return render(request, 'pontos_coleta.html', {'pontos': pontos})

class DispositivoView(View):
    def get(self, request):
        dispositivos = DispositivoEletronico.objects.all()
        return render(request, 'dispositivos.html', {'dispositivos': dispositivos})

class CriarSubstanciaView(CreateView):
    model = Substancia
    fields = ['nome', 'descricao', 'toxicidade']  # ajuste conforme seu modelo
    template_name = 'criar_substancia.html'
    success_url = reverse_lazy('listar_substancias')  # ou onde quiser redirecionar depois

class SubstanciaView(View):
    def get(self, request):
        substancias = Substancia.objects.all()
        return render(request, 'substancias.html', {'substancias': substancias})

class ComponenteToxicoView(View):
    def get(self, request):
        componentes = ComponenteToxico.objects.all()
        return render(request, 'componentes_toxicos.html', {'componentes': componentes})

class AlertaView(View):
    def get(self, request):
        alertas = Alerta.objects.all()
        return render(request, 'alertas.html', {'alertas': alertas})
    

class CriarAlertaView(CreateView):
    model = Alerta
    fields = ['titulo', 'descricao', 'nivel']
    template_name = 'criar_alerta.html'
    success_url = '/alertas/'  # ou use reverse_lazy('nome_da_view')

class ConteudoEducativoView(View):
    def get(self, request):
        conteudos = ConteudoEducativo.objects.all()
        return render(request, 'educativos.html', {'conteudos': conteudos})

class ConteudoEducativoView(View):
    def get(self, request):
        conteudos = ConteudoEducativo.objects.all()
        return render(request, 'educativos.html', {'conteudos': conteudos})

class UsuarioPontoColetaView(View):
    def get(self, request):
        relacoes = UsuarioPontoColeta.objects.all()
        return render(request, 'usuarios_ponto.html', {'relacoes': relacoes})

class RelatorioAmbientalView(View):
    def get(self, request):
        relatorios = RelatorioAmbiental.objects.all()
        return render(request, 'relatorios.html', {'relatorios': relatorios})
