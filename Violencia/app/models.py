from django.db import models
from django.utils import timezone

class PessoaAnonima(models.Model):
    identificador_sessao = models.CharField(max_length=100, unique=True, verbose_name="Identificador da Sessão")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    

    def __str__(self):
        return self.identificador_sessao

    class Meta:
        verbose_name = "Pessoa Anônima"
        verbose_name_plural = "Pessoas Anônimas"


class Denuncias(models.Model):
    descricao = models.TextField(verbose_name="Descrição da Denúncia")
    tipo_violencia = models.CharField(max_length=100, verbose_name="Tipo de Violência")
    local_aproximado = models.CharField(max_length=200, verbose_name="Local Aproximado")
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")
    identificador_anonimo = models.ForeignKey(
        PessoaAnonima,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Identificador Anônimo"
    )
    tempo_sessao = models.DurationField(blank=True, null=True, verbose_name="Tempo de Sessão")

    def __str__(self):
        return f"Denúncia {self.id}: {self.tipo_violencia}"

    class Meta:
        verbose_name = "Denúncia"
        verbose_name_plural = "Denúncias"


class ChatApoio(models.Model):
    pessoa_anonima = models.ForeignKey(PessoaAnonima, on_delete=models.CASCADE, verbose_name="Pessoa Anônima")
    mensagem = models.TextField(verbose_name="Mensagem")
    data_mensagem = models.DateTimeField(default=timezone.now, verbose_name="Data da Mensagem")
    respondida = models.BooleanField(default=False, verbose_name="Respondida")

    def __str__(self):
        return f"Chat {self.id} - {self.pessoa_anonima}"

    class Meta:
        verbose_name = "Chat de Apoio"
        verbose_name_plural = "Chats de Apoio"
class Informativo(models.Model):
    descricao = models.TextField(verbose_name="Descrição do conteúdo informativo")
    tipo_conteudo = models.CharField(max_length=100, verbose_name="Tipo de conteúdo")
    link = models.URLField(max_length=255, verbose_name="Link do conteúdo")

    def __str__(self):
        return f"Informativo: {self.descricao[:50]}..."

    class Meta:
        verbose_name = "Informativo"
        verbose_name_plural = "Informativos"

class LocalApoio(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do local")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone")
    tipo_local = models.CharField(max_length=100, verbose_name="Tipo de local")
    distancia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Distância")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Local de Apoio"
        verbose_name_plural = "Locais de Apoio"

class GrupoApoio(models.Model):
    nome_grupo = models.CharField(max_length=255, verbose_name="Nome do grupo")
    moderador = models.CharField(max_length=255, verbose_name="Moderador")
    participantes_anonimos = models.TextField(blank=True, null=True, verbose_name="Participantes anônimos")

    def __str__(self):
        return self.nome_grupo

    class Meta:
        verbose_name = "Grupo de Apoio"
        verbose_name_plural = "Grupos de Apoio"

class Localizacao(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    consentimento = models.BooleanField(verbose_name="Consentimento para localização")

    def __str__(self):
        return f"Lat: {self.latitude}, Long: {self.longitude}"

    class Meta:
        verbose_name = "Localização"
        verbose_name_plural = "Localizações"

class Voluntaria(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome da voluntária")
    idade = models.IntegerField(verbose_name="Idade")
    especialidade = models.CharField(max_length=255, verbose_name="Especialidade")
    cidade = models.CharField(max_length=255, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Voluntária"
        verbose_name_plural = "Voluntárias"

class HistoriaSuperacao(models.Model):
    texto = models.TextField(max_length=300, verbose_name="Texto da história")
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name="Data de envio")
    status = models.CharField(max_length=20, default="pendente", verbose_name="Status")
    data_publicacao = models.DateTimeField(null=True, blank=True, verbose_name="Data de publicação")
    visualizacoes = models.IntegerField(default=0, verbose_name="Visualizações")

    def __str__(self):
        return self.texto[:50] + ("..." if len(self.texto) > 50 else "")

    class Meta:
        verbose_name = "História de Superação"
        verbose_name_plural = "Histórias de Superação"