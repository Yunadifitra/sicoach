from django.forms import ModelForm
from django import forms
from sicoach.models import Profile, Pembayaran

class FormBuku(ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'

    widgets = {
      'user' : forms.NumberInput({'class':'form-control'}),
      'no_hp' : forms.NumberInput({'class':'form-control'}),
      'nama' : forms.TextInput({'class':'form-control'}),
      'asal_kota' : forms.TextInput({'class':'form-control'}),
      'umur' : forms.NumberInput({'class':'form-control'}),
      'kategori_id' : forms.Select({'class':'form-control'}),
    }

class Pembayaran(ModelForm):
  class Meta:
    model = Pembayaran
    fields = '__all__'

    widgets = {
    }