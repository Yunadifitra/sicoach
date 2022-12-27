from django.shortcuts import render, redirect, HttpResponse
from sicoach.models import Profile
from sicoach.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def home(request):
    template = 'index.html'
    return render(request, template)

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
    return render(request, 'register.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_profil(request):
    current_user = request.user
    id = current_user.id
    buku = Profile.objects.filter(user=id)
    buku.delete()

    messages.success(request, "Data Berhasil dihapus!")
    return redirect('all')

@login_required(login_url=settings.LOGIN_URL)
def ubah_profil(request, id_profile):
    current_user = request.user
    id = current_user.id
    buku = Profile.objects.get(user=id)
    template = 'change_profile.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_profil', id_profile = id_profile)
    else:
        form = FormBuku(instance=Profile)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def tampilkan_profil(request):
    current_user = request.user
    id = current_user.id
    books = Profile.objects.filter(user = id)

    konteks = {
        'books': books,
    }
    return render(request, 'view-profile.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def all(request):
    books = Profile.objects.all()

    konteks = {
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_sepakbola(request):
    books = Profile.objects.filter(kategori_id__nama = 'Sepakbola')

    konteks = {
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_badminton(request):
    books = Profile.objects.filter(kategori_id__nama = 'Badminton')

    konteks = {
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_futsal(request):
    books = Profile.objects.filter(kategori_id__nama = 'Futsal')

    konteks = {
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_renang(request):
    books = Profile.objects.filter(kategori_id__nama = 'Renang')

    konteks = {
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

def tambah_profil(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'coach-profile.html', konteks)
    else:
        form = FormBuku()

        konteks = {
            'form': form,
        }

    return render(request, 'coach-profile.html', konteks)