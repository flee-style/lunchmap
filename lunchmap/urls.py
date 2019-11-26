from django.urls import path
from . import views

app_name = 'lunchmap'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>',views.ShopDetailView.as_view(),name='detail'),

    path('create',views.ShopCreateView.as_view(),name='create'),
    path('<int:pk>/update',views.ShopUpdateView.as_view(),name="update"),
    path('<int:pk>/delete',views.ShopDeleteView.as_view(),name="delete"),
]