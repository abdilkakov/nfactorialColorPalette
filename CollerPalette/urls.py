from django.urls import path
from palette.views import save_color, save_color1
from .views import register, profile_view, color_box_view, color_box_view1, \
    generate_new_color, color_mix, index
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('signup/', register, name='register'),
    path('profile/', profile_view, name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('choose/', color_box_view, name='choose'),
    path('saved/', save_color, name='saved'),
    path('asd/', color_box_view1, name='color_list'),
    path('asd/<int:pk>/', generate_new_color, name='color_generate'),
    path('color_mix/', color_mix, name='color_mix'),
    path('saved1/', save_color1, name='saved1')
]
