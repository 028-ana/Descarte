from django.urls import path
from app.views import *  # Substitua 'app' pelo nome correto do seu app

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('usuarios/novo/', CriarUsuarioView.as_view(), name='criar_usuario'),
    path('usuarios/', UsuarioView.as_view(), name='usuarios'),
    path('pontos_coleta/', PontoColetaView.as_view(), name='pontos_coleta'),
    path('dispositivos/', DispositivoView.as_view(), name='dispositivos'),
    path('substancias/', SubstanciaView.as_view(), name='substancias'),
    path('componentes_toxicos/', ComponenteToxicoView.as_view(), name='componentes_toxicos'),
    path('alertas/', AlertaView.as_view(), name='alertas'),
    path('educativos/', ConteudoEducativoView.as_view(), name='educativos'),
    path('usuarios_ponto/', UsuarioPontoColetaView.as_view(), name='usuarios_ponto'),
    path('relatorios/', RelatorioAmbientalView.as_view(), name='relatorios'),
]
