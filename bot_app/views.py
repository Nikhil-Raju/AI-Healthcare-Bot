import os
import urllib.parse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from openai import OpenAI
from dotenv import load_dotenv
from .models import SearchHistory

# Load variables from the .env file
load_dotenv()

# Securely fetch key from environment
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def signup_view(request):
    if request.method == "POST":
        u, p = request.POST.get('username'), request.POST.get('password')
        if User.objects.filter(username=u).exists():
            messages.error(request, "Username already exists!")
        else:
            User.objects.create_user(username=u, password=p)
            messages.success(request, "Account created! Please log in.")
            return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        u, p = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('chat')
        messages.error(request, "Invalid Credentials")
    return render(request, 'login.html')

def chat_view(request):
    if not request.user.is_authenticated: 
        return redirect('login')
    history = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'index.html', {'history': history})

def chat_api(request):
    query = request.GET.get('text', '')
    if not query:
        return JsonResponse({'reply': 'Awaiting input...', 'is_health': False})
    
    try:
        # Start of the diagnostic logic
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Nikhil AI: Health Intelligence Core. Provide professional analysis."},
                {"role": "user", "content": query}
            ]
        )
        reply = response.choices[0].message.content
        
        # Save record to database
        SearchHistory.objects.create(user=request.user, query=query, ai_response=reply)
        q = urllib.parse.quote(query)
        
        return JsonResponse({
            'reply': reply, 
            'is_health': True,
            'h_link': f"https://www.google.com/maps/search/{q}+hospital",
            'p_link': f"https://www.1mg.com/search/all?name={q}"
        })

    except Exception as e:
        # This block was likely missing or misaligned, causing your error
        return JsonResponse({'reply': f"Diagnostic Interrupt: {str(e)}", 'is_health': False})

def logout_view(request):
    logout(request)
    return redirect('login')