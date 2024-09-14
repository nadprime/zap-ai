from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.index, name='index'),
    path('blog/', views.bloggen, name='bloggen'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('script/', views.script_generator, name='script_generator'),
    path('xpost/', views.xpostgen, name='xpostgen'),
    path('instabio/', views.instabiogen, name='instabiogen'),
    path('articlewrite/', views.articlewriter, name='articlewriter'),
    path('business/', views.businessgen, name='businessgen'),   
    path('copywrite/', views.copywriter, name='copywriter'),   
    path('email/', views.email, name='email'),   
    path('grammar/', views.grammarcheck, name='grammarcheck'),   
    path('instacal/', views.instacal, name='instacal'),   
    path('instapost/', views.instapostgen, name='instapostgen'),   
    path('product/', views.proddesc, name='proddesc'),   
    path('research/', views.research, name='research'),   
    path('ideagen/', views.smidea, name='smidea'),   
    path('tag/', views.taggen, name='taggen'),   
    path('websum/', views.websumm, name='websumm'),   
    path('writestyle/', views.writestyle, name='writestyle'),   
    path('xcal/', views.xcal, name='xcal'),   
    path('ytdesc/', views.ytdesc, name='ytdesc'),  
]