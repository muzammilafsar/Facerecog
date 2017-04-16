from django.shortcuts import render
from addFace.models import *
from .forms import UnkownPhoto
from.models import SearchHistory
from PIL import Image
# Create your views here.
import face_recognition
def searchdb(request):
    if request.method == 'POST':
        form = UnkownPhoto(request.POST, request.FILES)
        if form.is_valid():
            person=SearchHistory()

            person.photo=form.cleaned_data['photo']
            person.save()
            load_img = face_recognition.load_image_file(person.photo)

            # face_encoding = face_recognition.face_encodings(load_img)[0]

            unknown_face_encoding = face_recognition.face_encodings(load_img)[0]
            faces=Person.objects.all()
            known_faces=[]
            for x in faces:
                load_img = face_recognition.load_image_file(x.photo)
                face_encoding = face_recognition.face_encodings(load_img)[0]
                known_faces.append(face_encoding)

            results = face_recognition.compare_faces(known_faces,unknown_face_encoding)
            for r in results:
                if r==True:
                    # pass
                    print(results.index(r))
                    # print(faces[results.index(r)])
            print(person.photo.url)



            return render(request,'searchindb/search.html',{'pic':person.photo.url,'pic2':faces[2]})
    else:
        form=UnkownPhoto()
    return render(request,'searchindb/search.html',{'form':form})
