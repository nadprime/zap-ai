from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from .forms import UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from django.utils import timezone

import google.generativeai as genai
import os
import markdown

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
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


@login_required
def script_generator(request):
    return render(request, 'script_generator.html')

@login_required
def xpostgen(request):
    return render(request, 'xpostgen.html')

@login_required
def instabiogen(request):
    return render(request, 'instabiogen.html')

def landing_page(request):
    return render(request, 'landing_page.html')

def about(request):
    return render(request, 'about.html')

@login_required
def ai_suggestions(request):
    return render(request, 'ai_suggestions.html')

@login_required
def analytics(request):
    return render(request, 'analytics.html')

@login_required
def content_calender(request):
    return render(request, 'content_calendar.html')

@login_required
def create_content(request):
    return render(request, 'create_content.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def help_center(request):
    return render(request, 'help_center.html')

@login_required
def monetization_insights(request):
    return render(request, 'monetization_insights.html')

@login_required
def real_time_feedback(request):
    return render(request, 'real_time_feedback.html')

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def team_collaboration(request):
    return render(request, 'team_collaboration.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('landing_page')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})