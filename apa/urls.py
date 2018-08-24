from django.contrib import admin
from django.urls import path, include
from homepage.views import Home, Teste, Precos, About, Restrita
from fichateste.views import Fichosa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('teste/', Teste.as_view(), name='teste'),
    path('precos/', Precos.as_view(), name='precos'),
    path('about/', About.as_view(), name='about'),
    path('restrita/', Restrita.as_view(), name='restrita'),
    path('fichosa/', Fichosa.as_view(), name='fichosa'),
    path('', include('django.contrib.auth.urls')),
]
