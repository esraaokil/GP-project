"""covido URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from data import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #GET  from governorates_get
    path('governorates_get/', views.governorates_get),

    # #GET from city_get
    path('city_get/', views.city_get),

    #GET from Specialization_get
    path('Specialization_get/', views.Specialization_get),
    
    #GET POST from profile_Post
    path('profile_create/', views.profile_create),


    #GET POST from doctor_create
    path('doctor_create/', views.doctor_create),
     #GET PUT DELETE from doctor_edit
    path('doctor_edit/<uuid:pk>', views.doctor_edit),

    #GET POST from patient_create
    path('patient_create/', views.patient_create),
     #GET PUT DELETE from patient_edit
    path('patient_edit/<uuid:pk>', views.patient_edit),

    #GET POST from chest_create
    path('chest_create/', views.chest_create),
     #GET PUT DELETE from chest_edit
    #path('chest_edit/<uuid:pk>', views.chest_edit),

    #GET POST from review_create
    path('review_create/', views.review_create),
     #GET PUT DELETE from review_edit
    path('review_edit/<uuid:pk>', views.review_edit),

    #GET POST from diseases_create
    path('diseases_create/', views.diseases_create),
     #GET PUT DELETE from diseases_edit
    #path('diseases_edit/<uuid:pk>', views.diseases_edit),

    #GET POST from patient_diseases_create
    path('patient_diseases_create/', views.patient_diseases_create),
     #GET PUT DELETE from patient_diseases_edit
    path('patient_diseases_edit/<int:pk>', views.patient_diseases_edit),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
