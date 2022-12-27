"""Coach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sicoach.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('profil/', tampilkan_profil, name='profil'),
    path('all/', all, name='all'),
    path('profil/sepakbola', profil_sepakbola, name='profil_sepakbola'),
    path('profil/futsal', profil_futsal, name='profil_futsal'),
    path('profil/badminton', profil_badminton, name='profil_badminton'),
    path('profil/renang', profil_renang, name='profil_renang'),
    path('profil/tambah/', tambah_profil, name='tambah_profil'),
    path('profil/ubah/<int:id_buku>', ubah_profil, name='ubah_profil'),
    path('profil/hapus/<int:id_buku>', hapus_profil, name="hapus_profil"),
    path('auth/masuk/', LoginView.as_view(next_page='all'), name='masuk'),
    path('auth/keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('user/add/', signup, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
