from django.contrib import admin
from django.urls import path, include
from homepage.views import Home, Teste, Saiba, Precos, About, Contato, Restrita, Cadastro, Configuracoes, Ajuda, \
    Privacidade, Termos, ProfileUpdate
from ficha.views import FichaNew, FichaUpdate, FichaPrint, FichaDelete, Tcle, Orcamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('profile_update/<int:pk>', ProfileUpdate.as_view(), name='profile_update'),
    path('saiba/', Saiba.as_view(), name='saiba'),
    path('teste/', Teste.as_view(), name='teste'),
    path('precos/', Precos.as_view(), name='precos'),
    path('about/', About.as_view(), name='about'),
    path('contato/', Contato.as_view(), name='contato'),
    path('restrita/', Restrita.as_view(), name='restrita'),
    path('configuracoes/', Configuracoes.as_view(), name='configuracoes'),
    path('ajuda/', Ajuda.as_view(), name='ajuda'),
    path('termos/', Termos.as_view(), name='termos'),
    path('privacidade/', Privacidade.as_view(), name='privacidade'),
    path('ficha/', FichaNew.as_view(), name='ficha'),
    path('ficha_update/<int:pk>', FichaUpdate.as_view(), name='ficha_update'),
    path('ficha_print/<int:pk>', FichaPrint.as_view(), name='ficha_print'),
    path('ficha_delete/<int:pk>', FichaDelete.as_view(), name='ficha_delete'),
    path('tcle/<int:pk>', Tcle.as_view(), name='tcle'),
    path('orcamento/<int:pk>', Orcamento.as_view(), name='orcamento'),
    path('', include('django.contrib.auth.urls')),
]

admin.site.site_header = "Avaliação Pré-Anestésica"
admin.site.index_title = "Meu Site - admin"
admin.site.site_title = "admin"