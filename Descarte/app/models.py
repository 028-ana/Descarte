from django.db import models

class Usuario(models.Model):
    TIPO_USUARIO = [
        ('comum', 'Comum'),
        ('admin', 'Administrador'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO, default='comum')

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.nome

class PontoColeta(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

from django.db import models

class Substancia(models.Model):
    nome = models.CharField(max_length=100)
    efeitoAmbiental = models.TextField()
    nivel_perigo = models.CharField(max_length=1, choices=[
        ('A', 'Alto'),
        ('M', 'Médio'), 
        ('B', 'Baixo')
    ])
    
    def __str__(self):
        return self.nome

class DispositivoEletronico(models.Model):
    STATUS = [
        ('descartado', 'Descartado'),
        ('coletado', 'Coletado'),
        ('pendente', 'Pendente'),
    ]
    tipo = models.CharField(max_length=100)
    componentes_toxicos = models.ManyToManyField(Substancia, through='ComponenteToxico')
    status = models.CharField(max_length=10, choices=STATUS, default='pendente')

    def __str__(self):
        return self.tipo

class ComponenteToxico(models.Model):
    dispositivo = models.ForeignKey(DispositivoEletronico, on_delete=models.CASCADE)
    substancia = models.ForeignKey(Substancia, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dispositivo} - {self.substancia}"

class Alerta(models.Model):
    descricao = models.TextField()
    data = models.DateField()
    local_afetado = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class ConteudoEducativo(models.Model):
    TIPO_CONTEUDO = [
        ('artigo', 'Artigo'),
        ('video', 'Vídeo'),
        ('imagem', 'Imagem'),
    ]
    titulo = models.CharField(max_length=200)
    tipo_conteudo = models.CharField(max_length=20, choices=TIPO_CONTEUDO)
    descricao = models.TextField()
    url_midia = models.URLField()

    def __str__(self):
        return self.titulo

class UsuarioPontoColeta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ponto_coleta = models.ForeignKey(PontoColeta, on_delete=models.CASCADE)
    data_utilizacao = models.DateField()

    def __str__(self):
        return f"{self.usuario} usou {self.ponto_coleta} em {self.data_utilizacao}"

class RelatorioAmbiental(models.Model):
    data = models.DateField()
    descricao = models.TextField()
    nivel_contaminacao = models.CharField(max_length=100)
    ponto_coleta = models.ForeignKey(PontoColeta, on_delete=models.CASCADE)

    def __str__(self):
        return f"Relatório de {self.data} - {self.ponto_coleta}"
