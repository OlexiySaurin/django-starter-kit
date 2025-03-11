from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/profile/', views.profile_page, name='profile'),
    path('accounts/send-verification/', views.send_verification, name='send-verification'),
]

htmx_urlpatterns = [
    path('check-username/', views.check_username, name='check-username'),
    path('check-password/', views.check_password, name='check-password'),
    path('search/', views.search, name='search'),
]

urlpatterns += htmx_urlpatterns