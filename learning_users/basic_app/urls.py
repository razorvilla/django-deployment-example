from django.contrib import admin
from django.urls import path,include
from basic_app import views

# TEMPLATE URLS
app_name = 'basic_app'

urlpatterns = [
    #path('',views.index,name="index"),
    path('register',views.register,name="register"),
    #path('admin/', admin.site.urls),
    path('user_login',views.user_login,name='user_login'),
]
