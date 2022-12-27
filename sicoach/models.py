from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
  nama = models.CharField(max_length=9)
  keterangan = models.TextField()

  def __str__(self):
    return self.nama

class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  no_hp = models.CharField(max_length=40)
  nama = models.CharField(max_length=50)
  asal_kota = models.CharField(max_length=40)
  umur = models.IntegerField(null=True)
  kategori_id = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
  cover = models.ImageField(upload_to='cover/', null=True)
  tanggal = models.DateTimeField(blank=True, auto_now_add=True, null=True)

  def __str__(self):
    return self.nama