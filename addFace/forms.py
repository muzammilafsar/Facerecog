from django import forms


class PhotoForm(forms.Form):

    name = forms.CharField(max_length=20)
    location=forms.CharField(max_length=30)
    photo=forms.ImageField()
    profession = forms.CharField(max_length=20)

