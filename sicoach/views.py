from django.shortcuts import render, redirect, HttpResponse
from sicoach.models import Profile
from sicoach.forms import FormBuku, Pembayaran
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def home(request):
    template = 'index.html'
    return render(request, template)

def select(request):
    template = 'select-role.html'
    return render(request, template)

def base(request):
    template = 'base.html'
    return render(request, template)

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('masuk')
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
def ubah_profil(request):
    current_user = request.user
    id = current_user.id
    buku = Profile.objects.get(user=id)
    template = 'change_profile.html'
    data = {
        'user' : buku.user,
        'nama' : buku.nama,
        "umur" : buku.umur,
        "asal_kota" : buku.asal_kota,
        "no_hp" : buku.no_hp,
        "kategori_id" : buku.kategori_id,
    }
    form = FormBuku(request.POST, initial=data ,instance=buku)
    if request.POST:
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('all')
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def tampilkan_profil(request, profile_id):
    current_user = request.user
    id = current_user.id
    books = Profile.objects.filter(id = profile_id)

    konteks = {
        'books': books,
    }
    return render(request, 'view-profile.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def all(request):
    books = Profile.objects.all()

    konteks = {
        'judul': "Semua Kategori",
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_sepakbola(request):
    books = Profile.objects.filter(kategori_id__nama = 'Sepakbola')

    konteks = {
        'judul': "Sepak Bola",
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_badminton(request):
    books = Profile.objects.filter(kategori_id__nama = 'Badminton')

    konteks = {
        'judul': "Badminton",
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_futsal(request):
    books = Profile.objects.filter(kategori_id__nama = 'Futsal')

    konteks = {
        'judul': "Futsal",
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_renang(request):
    books = Profile.objects.filter(kategori_id__nama = 'Renang')

    konteks = {
        'judul': "Renang",
        'books': books,
    }
    return render(request, 'sports-category.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def all_atlit(request):
    books = Profile.objects.all()

    konteks = {
        'judul': "Semua Kategori",
        'books': books,
    }
    return render(request, 'sports-category-copy.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_sepakbola_atlit(request):
    books = Profile.objects.filter(kategori_id__nama = 'Sepakbola')

    konteks = {
        'judul': "Sepak Bola",
        'books': books,
    }
    return render(request, 'sports-category-copy.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_badminton_atlit(request):
    books = Profile.objects.filter(kategori_id__nama = 'Badminton')

    konteks = {
        'judul': "Badminton",
        'books': books,
    }
    return render(request, 'sports-category-copy.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_futsal_atlit(request):
    books = Profile.objects.filter(kategori_id__nama = 'Futsal')

    konteks = {
        'judul': "Futsal",
        'books': books,
    }
    return render(request, 'sports-category-copy.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def profil_renang_atlit(request):
    books = Profile.objects.filter(kategori_id__nama = 'Renang')

    konteks = {
        'judul': "Renang",
        'books': books,
    }
    return render(request, 'sports-category-copy.html', konteks)

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
            return redirect('pembayaran')
    else:
        form = FormBuku()

        konteks = {
            'form': form,
        }

    return render(request, 'coach-profile.html', konteks)

def pembayaran(request):
    if request.POST:
        form = Pembayaran(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = Pembayaran()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'coach-payment.html', konteks)
            
    else:
        form = Pembayaran()

        konteks = {
            'form': form,
        }

    return render(request, 'coach-payment.html', konteks)