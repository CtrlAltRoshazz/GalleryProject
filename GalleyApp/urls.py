from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name="home"),
    path('register/', views.register_view, name="register"),
    path('gallery/', views.gallery_view, name="gallery"),
    path('signout/', views.signout_view, name="signout"),
    path('addimage/', views.addimage_view, name="addimage"),
    path("category/<int:id>/", views.category_view, name="category"),
]