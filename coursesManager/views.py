from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages #used for messages



def index(request):
    context = {
        'courses' : course.objects.all()
    }
    return render(request, 'index.html', context)

def remove(request, courseId):
    currentCourse = course.objects.get(id=courseId)
    context = {
        'currentCourse':currentCourse
    }
    return render(request, 'destroy.html', context)


def newShow(request):
    errors = course.objects.descripVal(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        courseDescription = description.objects.create(
            desc = request.POST['descrip'])

        currentCourse = course.objects.create(
            name = request.POST['name'])
        currentCourse.descrip = courseDescription
        currentCourse.save()
        #currentCourse.descrip.add(courseDescription)
        #probably doesnt work since its a one to one relatioship
    return redirect('/')


    
def deleteCourse(request, courseId):
    courseDelete = course.objects.get(id = courseId)
    courseDelete.delete()
    return redirect('/')