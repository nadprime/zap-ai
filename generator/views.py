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
    return render(request, 'generator/index.html')

@login_required
def bloggen(request):
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
    return render(request, 'generator/bloggen.html', {'chats': chats})


@login_required
def script_generator(request):
    return render(request, 'generator/script_generator.html')

@login_required
def xpostgen(request):
    return render(request, 'generator/xpostgen.html')

@login_required
def instabiogen(request):
    return render(request, 'generator/instabiogen.html')


@login_required
def articlewriter(request):
    return render(request, 'generator/articlewriter.html')


@login_required
def businessgen(request):
    return render(request, 'generator/businessgen.html')


@login_required
def copywriter(request):
    return render(request, 'generator/copywriter.html')

@login_required
def email(request):
    return render(request, 'generator/email.html')

@login_required
def grammarcheck(request):
    return render(request, 'generator/grammarcheck.html')

@login_required
def instacal(request):
    return render(request, 'generator/instacal.html')

@login_required
def instapostgen(request):
    return render(request, 'generator/instapostgen.html')

@login_required
def proddesc(request):
    return render(request, 'generator/proddesc.html')

@login_required
def research(request):
    return render(request, 'generator/research.html')

@login_required
def smidea(request):
    return render(request, 'generator/smidea.html')

@login_required
def taggen(request):
    return render(request, 'generator/taggen.html')

@login_required
def websumm(request):
    return render(request, 'generator/websumm.html')

@login_required
def writestyle(request):
    return render(request, 'generator/writestyle.html')

@login_required
def xcal(request):
    return render(request, 'generator/xcal.html')

@login_required
def ytdesc(request):
    return render(request, 'generator/ytdesc.html')

def landing_page(request):
    return render(request, 'generator/landing_page.html')

def about(request):
    return render(request, 'generator/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})