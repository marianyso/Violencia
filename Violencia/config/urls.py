from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexView.as_view(), name="index"),

    path("denuncias/", DenunciasView.as_view(), name="denuncias"),

    path("informativos/", InformativoView.as_view(), name="informativos"),

    path("chat/", ChatApoioView.as_view(), name="chat"),

    path("locais/", LocalApoioView.as_view(), name="locais"),

    path("grupos/", GrupoApoioView.as_view(), name="grupo"),

    path("localizacoes/", LocalizacaoView.as_view(), name="localizacao"),

    path("voluntarias/", VoluntariasView.as_view(), name="voluntarias"),

    path("HistoriaSuperacao/", HistoriaSuperacaoView.as_view(), name="historiasuperacao"),

]
