from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('babies/', views.babies_index, name='index'),
    path('babies/<int:baby_id>/', views.babies_detail, name='detail'),
    path('babies/create/', views.BabyCreate.as_view(), name="baby_create"),
    path('babies/<int:pk>/update/', views.BabyUpdate.as_view(), name='baby_update'),
    path('babies/<int:pk>/delete/', views.BabyDelete.as_view(), name='baby_delete'),
    path('playdates/', views.PlayDateList.as_view(), name="playdates_index"),
    path('playdates/<int:pk>/', views.PlayDateDetail.as_view(), name="playdates_detail"),
    path('playdates/create/', views.PlayDateCreate.as_view(), name="playdates_create"),
    path('playdates/<int:pk>/update', views.PlayDateUpdate.as_view(), name="playdates_update"),
    path('playdates/<int:pk>/delete/', views.PlayDateDelete.as_view(), name="playdates_delete"),
    path('babies/<int:baby_id>/assoc_playdate/<int:playdate_id>/', views.assoc_playdate, name="assoc_playdate"),
    path('babies/<int:baby_id>/add_feeding', views.add_feeding, name="add_feeding"),
    path('babies/<int:baby_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/signup/', views.signup, name="signup"),

]
