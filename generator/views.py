from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def ai_suggestions(request):
    return render(request, 'ai_suggestions.html')

def analytics(request):
    return render(request, 'analytics.html')

def content_calender(request):
    return render(request, 'content_calendar.html')

def create_content(request):
    return render(request, 'create_content.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def help_center(request):
    return render(request, 'help_center.html')

def monetization_insights(request):
    return render(request, 'monetization_insights.html')

def real_time_feedback(request):
    return render(request, 'real_time_feedback.html')

def settings(request):
    return render(request, 'settings.html')

def team_collaboration(request):
    return render(request, 'team_collaboration.html')

