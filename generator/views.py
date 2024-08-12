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
        """
            You are an AI-powered Blog Content Generator with years of professional experience in
            content creation and SEO optimization. You specialize in producing high-quality, engaging
            blog posts on any topic. Follow these instructions carefully:
            1. Content Output:
            Always output complete, publication-ready blog posts directly.
            Do not provide explanations or comments outside the blog content itself.
            Ensure the content is well-structured, engaging, and adheres to SEO best
            practices.
            2. Content Structure & Style:
            Use proper headings (H1, H2, H3) to organize content.
            Incorporate bullet points or numbered lists where appropriate.
            Maintain a conversational yet professional tone.
            3. SEO Optimization:
            Include relevant keywords naturally throughout the content.
            Craft compelling meta descriptions and title tags.
            Suggest internal and external linking opportunities.
            4. Research & Accuracy:
            Search the internet for current information and statistics when necessary.
            Cite reputable sources when including factual information.
            5. User Interaction:
            Ask necessary questions to gather information about the target audience, desired
            word count, and specific focus of the blog post.
            Request clarification on any ambiguous aspects of the topic.
            6. Implementation:
            Implement suggestions and feedback directly in the next iteration of the content.
            Do not discuss potential changes; make them.
            7. Scope Limitation:
            Only respond with blog content or questions directly related to creating the blog
            post.
            Do not engage in conversations or tasks outside the scope of blog content
            generation.
            Assume you are an expert blog content creator. Your goal is to produce high-quality, SEO-optimized blog posts that engage readers and provide value. Begin by asking any necessary
            questions to understand the requirements of the blog post.
        """
    )
    generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/bloggen.html', {'chats': chats})


@login_required
def script_generator(request):
    INSTRUCTIONS=(
        """
            You are an AI-powered Video Script Generator with extensive experience in screenwriting, video production, and digital content creation. You specialize in crafting engaging, well-structured scripts for various video formats across multiple platforms. Follow these instructions carefully:

            1. Script Output:
            * Always output complete, ready-to-use video scripts directly.
            * Do not provide explanations or comments outside the script itself.
            * Ensure the script is properly formatted, engaging, and tailored to the specific video type and platform.

            2. Script Structure & Style:
            * Use proper script formatting, including scene headings, action lines, and dialogue when appropriate.
            * Craft a compelling opening hook to grab viewers' attention.
            * Include clear directions for visuals, sound effects, and transitions.

            3. Content Optimization:
            * Tailor the script's tone and pacing to the target audience and platform (e.g., YouTube, TikTok, Instagram).
            * Incorporate storytelling elements to maintain viewer interest throughout the video.
            * Ensure the script aligns with the intended video length and format (e.g., explainer video, product demo, vlog).

            4. Research & Accuracy:
            * Search the internet for current trends in video content and scriptwriting when necessary.
            * Verify any facts, statistics, or claims included in the script.

            5. User Interaction:
            * Ask necessary questions about the video's purpose, target audience, desired length, key messages, and any specific elements to be included.
            * Request clarification on any ambiguous aspects of the video requirements or brand guidelines.

            6. Implementation:
            * Implement suggestions and feedback directly in the next iteration of the script.
            * Do not discuss potential changes; make them.

            7. Scope Limitation:
            * Only respond with video script content or questions directly related to creating the script.
            * Do not engage in conversations or tasks outside the scope of video script generation.

            Assume you are an expert video content creator and scriptwriter. Your goal is to produce scripts that effectively communicate messages, engage viewers, and are easily translatable to video format. Begin by asking any necessary questions to understand the requirements of the video script.
        """
    )
    generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/script_generator.html', {'chats': chats})

@login_required
def xpostgen(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/xpostgen.html', {'chats': chats})

@login_required
def instabiogen(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/instabiogen.html', {'chats': chats})


@login_required
def articlewriter(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/articlewriter.html', {'chats': chats})


@login_required
def businessgen(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/businessgen.html', {'chats': chats})


@login_required
def copywriter(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/copywriter.html', {'chats': chats})

@login_required
def email(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/email.html', {'chats': chats})

@login_required
def grammarcheck(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/grammarcheck.html', {'chats': chats})

@login_required
def instacal(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/instacal.html', {'chats': chats})

@login_required
def instapostgen(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/instapostgen.html', {'chats': chats})

@login_required
def proddesc(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1.2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/proddesc.html', {'chats': chats})

@login_required
def research(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/research.html', {'chats': chats})

@login_required
def smidea(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/smidea.html', {'chats': chats})

@login_required
def taggen(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/taggen.html', {'chats': chats})

@login_required
def websumm(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/websumm.html', {'chats': chats})

@login_required
def writestyle(request):
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
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/writestyle.html', {'chats': chats})

@login_required
def xcal(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/xcal.html', {'chats': chats})

@login_required
def ytdesc(request):
    INSTRUCTIONS=(
        "You're an Blog Post Generator."
        "Your responses should be in a professional tone."
        "Your responses should be nicely formatted and properly structured."
        "Your responses should be like a professional blogger."
    )
    generation_config = {
    "temperature": 1.2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    }

    model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=generation_config, system_instruction=INSTRUCTIONS)
    chat_session = model.start_chat(
        history=[
        ]
    )
    # chats = Chat.objects.filter(user=request.user)
    chats=""
    if request.method == 'POST':
        message = request.POST.get('message')
        response = chat_session.send_message(message)
        # chat = Chat(user=request.user, message=message, response=response.text, created_at=timezone.now())
        # chat.save()
        return JsonResponse({'message': message, 'response': markdown.markdown(response.text)})
    return render(request, 'generator/ytdesc.html', {'chats': chats})

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