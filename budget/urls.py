from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('budget/', views.budget_list, name='list'), 
    path('budget/add/', views.budget_add, name='add'),
    path('budget/<int:budget_index>/', views.budget_detail, name='detail'),
    path('budget/update/<int:budget_index>/', views.budget_update, name='update'),
    path('budget/delete/<int:budget_index>/', views.budget_delete, name='delete'),
    path('budget/search/', views.search, name='search'),
]



