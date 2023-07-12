from application import views
from django.urls import path
from .views import login_view
from .views import signup

app_name = 'application'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.calender, name='calender'),
    path('', views.test),
    path('', views.master),
    path('', views.shop, name='shop'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
]