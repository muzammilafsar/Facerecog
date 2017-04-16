from django.shortcuts import render,redirect
from .forms import *
from .models import Person
import face_recognition

# Create your views here.
def adding_entry_face(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            person=Person()
            person.name=form.cleaned_data['name']
            person.photo=form.cleaned_data['photo']
            person.save()
            # load_img = face_recognition.load_image_file(form.cleaned_data['photo'])
            # face_encoding = face_recognition.face_encodings(load_img)[0]

            return redirect('home')
    else:
        form = PhotoForm()
        #known=Person.objects.get(id=1)
        #load_img = face_recognition.load_image_file(known.photo)
        #face_encoding = face_recognition.face_encodings(load_img)[0]

    return render(request, 'addFace/home.html', {
        'form': form,
        # 'known':known,'face':face_encoding,'img':load_img
    })

