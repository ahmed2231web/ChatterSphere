from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Message

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'registration/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(email=email).exists():
            return render(request, 'registration/register.html', {'error': 'Email already exists'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        return redirect('chat_home')

    return render(request, 'registration/register.html')

def login_view(request):
    print("Login view called")  # Debug print
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"Login attempt for email: {email}")  # Debug print
        
        if not email or not password:
            return render(request, 'registration/login.html', {'error': 'Please fill in all fields'})
        
        try:
            user = User.objects.get(email=email)
            print(f"Found user: {user.username}")  # Debug print
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                print("Authentication successful")  # Debug print
                login(request, user)
                return redirect('chat_home')
            else:
                print("Authentication failed")  # Debug print
                return render(request, 'registration/login.html', {'error': 'Invalid password'})
        except User.DoesNotExist:
            print(f"No user found with email: {email}")  # Debug print
            return render(request, 'registration/login.html', {'error': 'No account found with this email'})

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def chat_home(request):
    return render(request, 'chat/index.html')

@login_required
def chat_room(request, room_name):
    messages = Message.objects.filter(room=room_name).order_by('timestamp')[:50]  # Get last 50 messages
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
        'username': request.user.username
    })