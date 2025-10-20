from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class DenunciasView(View):
    def get(self, request, *args, **kwargs):
        denuncias = Denuncias.objects.all()
        return render(request, 'denuncias.html', {'denuncias': denuncias})

class InformativoView(View):
    def get(self, request, *args, **kwargs):
        informativos = Informativo.objects.all()
        return render(request, 'informativos.html', {'informativos': informativos})

class ChatApoioView(View):
    def get(self, request, *args, **kwargs):
        chats = ChatApoio.objects.all()
        return render(request, 'chat.html', {'chats': chats})

class LocalApoioView(View):
    def get(self, request, *args, **kwargs):
        locais = LocalApoio.objects.all()
        return render(request, 'locais.html', {'locais': locais})

class GrupoApoioView(View):
    def get(self, request, *args, **kwargs):
        grupos = GrupoApoio.objects.all()
        return render(request, 'grupos.html', {'grupos': grupos})

class LocalizacaoView(View):
    def get(self, request, *args, **kwargs):
        localizacoes = Localizacao.objects.all()
        return render(request, 'localizacao.html', {'localizacoes': localizacoes})

class VoluntariasView(View):
    def get(self, request, *args, **kwargs):
        voluntarias = Voluntaria.objects.all()
        return render(request, 'voluntarias.html', {'voluntarias': voluntarias})
    
class HistoriaSuperacaoView(View):
    def get(self, request, *args, **kwargs):
        historias = HistoriaSuperacao.objects.all()
        return render(request, 'historias.html', {'historias': historias})