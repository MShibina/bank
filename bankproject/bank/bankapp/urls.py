from django.urls import path
from .import views
app_name = 'bankapp'
urlpatterns =[
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('form/', views.form, name='form'),
    path('application/', views.application,name='application'),
    path('logout/',views.logout, name='logout'),
]
