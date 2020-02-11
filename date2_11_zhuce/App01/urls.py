

from django.urls import path

from App01 import views
app_name='App01'
urlpatterns = [
    path('register/',views.register,name='register')
]
