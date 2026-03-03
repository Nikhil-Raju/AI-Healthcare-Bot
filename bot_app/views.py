from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from openai import OpenAI
import urllib.parse
from .models import SearchHistory

# Initialize OpenAI Client - FIXED SYNTAX
client = OpenAI(
    api_key="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"
)

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
    # Fixed: Filter history by the logged-in user
    history = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'index.html', {'history': history})

def chat_api(request):
    query = request.GET.get('text', '')
    if not query:
        return JsonResponse({'reply': 'No input provided.'})
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Nexus Health AI. Provide symptoms, medications in **bold**, and a professional disclaimer."},
                {"role": "user", "content": query}
            ]
        )
        reply = response.choices[0].message.content
        
        # Save search to database
        SearchHistory.objects.create(user=request.user, query=query, ai_response=reply)
        
        q = urllib.parse.quote(query)
        return JsonResponse({
            'reply': reply, 
            'h_link': f"https://www.google.com/maps/search/{q}+hospital+near+me",
            'p_link': f"https://www.1mg.com/search/all?name={q}"
        })
    except Exception as e:
        return JsonResponse({'reply': f"Nexus Core Error: {str(e)}"})

def logout_view(request):
    logout(request)
    return redirect('login')