from django.http import Http404
from django.shortcuts import render
from .models import Student, Classe


def index(request):
    all_classes = Classe.objects.all()
    return render(request, 'school/index.html', {'all_classes':  all_classes})


def detail (request, student_id):
   try:
       classes= Student.objects .get(pk=student_id)
   except Student.DoesNotExist:
    raise Http404("Student does not exist")
    return render(request, 'school/detail.html', {'student': student})


