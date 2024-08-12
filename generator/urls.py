from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('generator/', views.index, name='index'),
    path('blog_maker/', views.blog_maker, name='blog_maker'),
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
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('script/', views.script_generator, name='script_generator'),
    path('xpost/', views.xpostgen, name='xpostgen'),
    path('instabio/', views.instabiogen, name='instabiogen'),
]