from django.urls import path
from django.contrib import admin
from app.views import DeletarUsuarioView
from app.views import *  # Substitua 'app' pelo nome correto do seu app
from app.views import CriarPontoColetaView
from app.views import CriarSubstanciaView
from app import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('usuarios/editar/<int:pk>/', EditarUsuarioView.as_view(), name='editar_usuario'),
     path('usuarios/deletar/<int:pk>/', DeletarUsuarioView.as_view(), name='deletar_usuario'),
    path('usuarios/novo/', CriarUsuarioView.as_view(), name='criar_usuario'),
    path('usuarios/', UsuarioView.as_view(), name='usuarios'),
    path('pontos_coleta/', PontoColetaView.as_view(), name='pontos_coleta'),
      path('pontos_coleta/criar/', CriarPontoColetaView.as_view(), name='criar_ponto_coleta'),
    path('dispositivos/', DispositivoView.as_view(), name='dispositivos'),
    path('substancias/', SubstanciaView.as_view(), name='substancias'),
     path('substancias/criar/', CriarSubstanciaView.as_view(), name='criar_substancia'),
    path('componentes_toxicos/', ComponenteToxicoView.as_view(), name='componentes_toxicos'),
    path('alertas/', AlertaView.as_view(), name='alertas'),
    path('alertas/novo/', views.CriarAlertaView.as_view(), name='criar_alerta'),
    path('caminho/para/criar/', views.CriarConteudoView.as_view(), name='criar_conteudo'),
    path('educativos/', ConteudoEducativoView.as_view(), name='educativos'),
    path('usuarios_ponto/', UsuarioPontoColetaView.as_view(), name='usuarios_ponto'),
    path('relatorios/', RelatorioAmbientalView.as_view(), name='relatorios'),
]
