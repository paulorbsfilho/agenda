from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.contacts_list, name='contacts_list'),
    path('contact/<int:pk>/', views.contacts_detail, name='contact_detail'),
    path('contact/new/', views.contact_new, name='contact_new'),
    path('contact/<int:pk>/edit/', views.contact_edit, name='contact_edit'),
    path('contact/<int:pk>/delete/', views.contact_delete, name='contact_delete'),

    path('groups/', views.groups_list, name='groups_list'),
    path('groups/<int:pk>/', views.group_detail, name='group_detail'),
    path('group/new/', views.group_new, name='group_new'),
    path('group/<int:pk>/edit/', views.group_edit, name='group_edit'),
    path('group/<int:pk>/delete/', views.group_delete, name='group_delete'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)