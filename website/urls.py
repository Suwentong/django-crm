from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Клиенты
    path('customer/', views.customer, name='customer'),
    path('customer/<int:pk>', views.customer_info, name='customer'),
    path('delete_customer/<int:pk>', views.delete_customer, name='delete_customer'),
    path('update_customer/<int:pk>', views.update_customer, name='update_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),

    # Обращения
    path('record/', views.record, name='record'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('add_record/', views.add_record, name='add_record'),

    # Жалобы
    path('complaint/', views.complaint, name='complaint'),
    path('complaint/<int:pk>', views.customer_complaint, name='complaint'),
    path('delete_complaint/<int:pk>', views.delete_complaint, name='delete_complaint'),
    path('update_complaint/<int:pk>', views.update_complaint, name='update_complaint'),
    path('add_complaint/', views.add_complaint, name='add_complaint'),
]
