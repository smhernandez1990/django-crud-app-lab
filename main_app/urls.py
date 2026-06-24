from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('releases/', views.ReleaseList.as_view(), name='record-index'),
    path('releases/<int:pk>/', views.ReleaseDetail.as_view(), name='record-detail'),
    path('releases/create/', views.ReleaseCreate.as_view(), name='record-create'),
    path('releases/<int:pk>/update/', views.ReleaseUpdate.as_view(), name='record-update'),
    path('releases/<int:pk>/delete/', views.ReleaseDelete.as_view(), name='record-delete'),
    path('artists/', views.ArtistIndex.as_view(), name='artist-index'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artist-detail'),
    path('artists/create/', views.ArtistCreate.as_view(), name='artist-create'),
    path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artist-update'),
    path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artist-delete'),
    path('accounts/signup/', views.signup, name='signup')
]