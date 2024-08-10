from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('generator/', views.index, name='index'),
    path('suggestions/', views.ai_suggestions, name='ai_suggestions'),
    path('analytics/', views.analytics, name='analytics'),
    path('calender/', views.content_calender, name='content_calender'),
    path('content/', views.create_content, name='create_content'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('help/', views.help_center, name='help_center'),
    path('insights/', views.monetization_insights, name='monetization_insights'),
    path('feedback/', views.real_time_feedback, name='real_time_feedback'),
    path('settings/', views.settings, name='settings'),
    path('collaboration/', views.team_collaboration, name='team_collaboration'),
]