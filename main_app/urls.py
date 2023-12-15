from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('babys/', views.babies_index, name='index'),
    path('babys/<int:baby_id>/', views.babies_detail, name='detail'),
    path('babys/create/', views.BabyCreate.as_view(), name="baby_create"),
    path('babys/<int:pk>/update/', views.BabyUpdate.as_view(), name='baby_update'),
    path('babys/<int:pk>/delete/', views.BabyDelete.as_view(), name='baby_delete'),
    
]