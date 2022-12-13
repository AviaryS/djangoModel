from django.contrib import admin
from django.urls import path
from engine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_new, name='add'),
    path('all/', views.all_posts, name='all'),
]
