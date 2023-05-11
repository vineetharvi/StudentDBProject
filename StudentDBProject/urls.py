from django.contrib import admin
from django.urls import path
from django.urls import re_path
from StudentDBApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studenthomepage/', views.student_homepage),

    re_path('^.*$', views.student_homepage),
]
