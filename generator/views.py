from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone

import google.generativeai as genai
import os
import markdown

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def index(request):
    return render(request, 'index.html')


def blog_maker(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # if not request.user.is_authenticated:
    #     return redirect('login')
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=markdown.markdown(response.text), created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'blog_maker.html', {'chats': chats})


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

