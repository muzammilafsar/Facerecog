from django import forms

class UnkownPhoto(forms.Form):
    photo=forms.ImageField()

