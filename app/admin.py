from django.contrib import admin
from .models import (
    Usuario, Cidade, Estado, PontoColeta, Substancia,
    DispositivoEletronico, ComponenteToxico, Alerta,
    ConteudoEducativo, UsuarioPontoColeta, RelatorioAmbiental
)

class ComponenteToxicoInline(admin.TabularInline):
    model = ComponenteToxico
    extra = 1

class UsuarioPontoColetaInline(admin.TabularInline):
    model = UsuarioPontoColeta
    extra = 1

class RelatorioAmbientalInline(admin.TabularInline):
    model = RelatorioAmbiental
    extra = 1


@admin.register(DispositivoEletronico)
class DispositivoEletronicoAdmin(admin.ModelAdmin):
    list_display = ("tipo", "status")
    inlines = [ComponenteToxicoInline]


@admin.register(PontoColeta)
class PontoColetaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade", "uf", "telefone", "ativo")
    inlines = [UsuarioPontoColetaInline, RelatorioAmbientalInline]


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "tipo_usuario")
    inlines = [UsuarioPontoColetaInline]


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "uf")


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ("nome", "uf")


@admin.register(Substancia)
class SubstanciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "nivel_perigo")


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ("descricao", "data", "local_afetado")


@admin.register(ConteudoEducativo)
class ConteudoEducativoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo_conteudo")


@admin.register(UsuarioPontoColeta)
class UsuarioPontoColetaAdmin(admin.ModelAdmin):
    list_display = ("usuario", "ponto_coleta", "data_utilizacao")


@admin.register(GerenciarColota)
class GerenciarColotaAdmin(admin.ModelAdmin):
    list_display = ("data", "nivel_contaminacao", "ponto_coleta")
