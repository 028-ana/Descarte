from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Usuario
from .forms import UsuarioForm  # crie esse formulário

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

class PontoColetaView(View):
    def get(self, request):
        pontos = PontoColeta.objects.all()
        return render(request, 'pontos_coleta.html', {'pontos': pontos})

class DispositivoView(View):
    def get(self, request):
        dispositivos = DispositivoEletronico.objects.all()
        return render(request, 'dispositivos.html', {'dispositivos': dispositivos})

class SubstanciaView(View):
    def get(self, request):
        substancias = SubstanciaToxica.objects.all()
        return render(request, 'substancias.html', {'substancias': substancias})

class ComponenteToxicoView(View):
    def get(self, request):
        componentes = ComponenteToxico.objects.all()
        return render(request, 'componentes_toxicos.html', {'componentes': componentes})

class AlertaView(View):
    def get(self, request):
        alertas = Alerta.objects.all()
        return render(request, 'alertas.html', {'alertas': alertas})

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
