from django import forms


class PhotoForm(forms.Form):

    name = forms.CharField(max_length=20)
    photo=forms.ImageField()
