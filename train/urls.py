from django.urls import path
from train import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('detail/<str:pk>', views.Details.as_view(), name='detail'),
    path('add', views.CrForm.as_view(), name='add'),
    path('update/<str:pk>', views.UpdateCiti.as_view(), name='update'),
    path('delete/<str:pk>', views.DeleteCiti.as_view(), name='delete'),
]
