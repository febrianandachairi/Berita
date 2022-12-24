from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name="login_view"),
    path('register/', register_view, name="register_view"),
    path('add-berita/', add_berita, name="add_berita"),
    path('berita-detail/<str:id>', berita_detail, name="berita_detail"),
    path('see-berita/', see_berita, name="see_berita"),
    path('berita-delete/<str:id>', berita_delete, name="berita_delete"),
    path('berita-update/<str:id>', berita_update, name="berita_update"),
    path('logout-view/', logout_view, name="logout_view"),
    path('verify/<token>/', verify, name="verify"),
    path('dashboard/', dashboard, name="dashboard"),
    path('post/', post, name="post"),
    path('news/', news, name="news"),
    path('tabel-akun/', tabel_akun, name="tabel_akun"),
    path('tabel-berita-api/', tabel_berita_api, name="tabel_berita_api"),
    path('berita_api_baru/', berita_api_baru, name="berita_api_baru"),
    path('about_us/', about_us, name="about_us"),
    path('user-delete/<str:id>', user_delete, name="user_delete"),
]
