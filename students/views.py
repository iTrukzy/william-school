from students.models import Student
from django.shortcuts import render

# Create your views here.
# Create your views here.


def Students(request):
    content = {}
    try:
        students = Student.objects.all()
        if students:
            content = {
                'students': students
            }
        else:
            content = {}
    except OSError as err:
        content = {}

    return render(request, 'students/index.html', content)