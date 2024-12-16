"""
URL configuration for Demo1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from App1 import views as app1_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("add/", app1_views.add_data),
    path("app1/test1/", app1_views.test1),
    path("app1/task2", app1_views.task2),
    path("app1/task3", app1_views.task3),
    path("app1/task3_2", app1_views.task3_2),
    path("app1/task1_u", app1_views.task1_u),
    
    path("app1/add_books", app1_views.add_books),
]
