from classes.models import Class
from django.shortcuts import render
from students.models import Student


# Create your views here.
# Create your views here.


def Classes(request):
    content = {}
    try:
        result = Class.objects.all()
        content = {
            "classes": result
        }
    except OSError as err:
        content =  {}

    return render(request, 'classes/index.html', content)



def oneClass(request, id):
    content = {}
    try:
        students = Student.objects.filter(class_signed=id)
        if students:
            content = {
                "students": students
            }
        else:
            content = {}
    except OSError as err:
        content =  {}

    return render(request, 'classes/details.html', content)
