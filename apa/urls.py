from django.contrib import admin
from django.urls import path, include
from homepage.views import Home, Teste, Precos, About, Restrita, Cadastro
from ficha.views import FichaNew, FichaUpdate, FichaDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('teste/', Teste.as_view(), name='teste'),
    path('precos/', Precos.as_view(), name='precos'),
    path('about/', About.as_view(), name='about'),
    path('restrita/', Restrita.as_view(), name='restrita'),
    path('ficha_update/<int:pk>', FichaUpdate.as_view(), name='ficha_update'),
    path('ficha_delete/<int:pk>', FichaDelete.as_view(), name='ficha_delete'),
    path('ficha/', FichaNew.as_view(), name='ficha'),
    path('', include('django.contrib.auth.urls')),
]

admin.site.site_header = "Avaliação Pré-Anestésica"
admin.site.index_title = "Meu Site - admin"
admin.site.site_title = "admin"