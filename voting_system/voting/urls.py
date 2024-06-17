from django.urls import path
from . import views
urlpatterns = [
    path('voter_panel/', views.voter_panel, name='voter_panel'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('cast_vote/', views.cast_vote, name='cast_vote'),
    path('view_vote/', views.view_vote, name='view_vote'),
]