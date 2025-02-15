import re
from django.shortcuts import render, get_object_or_404
import random
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import qrcode
from io import BytesIO
from django.views.decorators.csrf import csrf_protect
import math

# these are for knowing which page to return for each link

def Index(request):
    return render(request, 'index.html')

#@csrf_protect
class UserSignupView(CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'register.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('create_meetup')

#@csrf_protect
class UserLoginView(LoginView):
    template_name='login.html'

def logout_user(request):
    logout(request)
    return redirect("/")


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def style(request):
    return render(request, 'style.css')

def location(request):
    return render(request, 'create_meetup.html')

def friends_list(request):
    profile = request.user.profile
    following = profile.follows.all()
    return render(request, 'friends_list.html', {'following': following})

def history(request):
    profile = request.user.profile  # Get the logged-in user's profile
    meetups = profile.scanned_meetups.all() | profile.scanned_by_meetups.all()
    return render(request, "history.html", {"meetups": meetups})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, "user_list.html", {"profiles": profiles})

def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    following_list = profile.follows.all()
    return render(request, "profile.html", {"profile": profile, "following_list": following_list})

def verification(request):
    return render(request, "verification.html")

#calculates the distsance between latitude and longitude between two poitns
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371000  # Radius of the Earth in meters
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # Distance in meters

@login_required
def verify_meetup(request):
    scanner = request.user.profile  # The user scanning the QR code

    # Extract query parameters from the request
    qr_user_id = request.GET.get('user_id')
    qr_lat = request.GET.get('lat')
    qr_lon = request.GET.get('lon')
    scanner_lat = request.GET.get('scanner_lat')
    scanner_lon = request.GET.get('scanner_lon')

    # Validate required parameters
    if not all([qr_user_id, qr_lat, qr_lon, scanner_lat, scanner_lon]):
        return JsonResponse({'error': 'Missing required location data'}, status=400)

    try:
        # Convert coordinates to float
        qr_lat, qr_lon = float(qr_lat), float(qr_lon)
        scanner_lat, scanner_lon = float(scanner_lat), float(scanner_lon)
    except ValueError:
        return JsonResponse({'error': 'Invalid latitude or longitude values'}, status=400)

    # Fetch the QR code owner
    try:
        qr_owner = Profile.objects.get(user__id=qr_user_id)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'QR code owner not found'}, status=404)

    # Calculate distance between scanner and QR code location
    distance = calculate_distance(qr_lat, qr_lon, scanner_lat, scanner_lon)

    if distance > 100:  # If users are not within 10 meters
        return JsonResponse({
            'error': 'Users must be within 10 meters to verify meetup',
            'distance': round(distance, 2)  # Return distance even on failure
        }, status=400)

    # Users follow each other
    scanner.follows.add(qr_owner)
    qr_owner.follows.add(scanner)

    # Log the meetup
    meetup = Meetup.objects.create(
        scanner=scanner,
        scanned=qr_owner,
        location=f"{scanner_lat}, {scanner_lon}",
        timestamp=now()
    )

    # Return JSON response with verification details
    return JsonResponse({
        'success': True,
        'message': 'Meetup verified!',
        'meetup_id': meetup.id,
        'distance': round(distance, 2),  # Verified distance
        'scanner_username': scanner.user.username,  # Scanner (who verified)
        'qr_owner_username': qr_owner.user.username,  # QR Code Owner
        'location': f"{scanner_lat}, {scanner_lon}",  # Meetup Location
        'timestamp': meetup.timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Date and Time
    })