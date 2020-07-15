from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('newShow', views.newShow),
    path('courses/remove/<int:courseId>', views.remove),
    path('courses/delete/<int:courseId>', views.deleteCourse)
]
 