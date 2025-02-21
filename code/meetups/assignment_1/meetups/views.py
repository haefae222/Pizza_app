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
from django.core.paginator import Paginator
from django.db.models import Q

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
    if request.method != "POST":
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        data = json.loads(request.body)  # Parse JSON data from POST request

        scanner = request.user.profile  # The user scanning the QR code
        qr_user_id = data.get("user_id")
        qr_lat = data.get("qr_lat")
        qr_lon = data.get("qr_lon")
        scanner_lat = data.get("scanner_lat")
        scanner_lon = data.get("scanner_lon")
        scanner_address = data.get("scanner_address", "Unknown Location")  # Get the address

        if not all([qr_user_id, qr_lat, qr_lon, scanner_lat, scanner_lon]):
            return JsonResponse({'error': 'Missing required location data'}, status=400)

        # Convert coordinates to float
        try:
            qr_lat, qr_lon = float(qr_lat), float(qr_lon)
            scanner_lat, scanner_lon = float(scanner_lat), float(scanner_lon)
        except ValueError:
            return JsonResponse({'error': 'Invalid latitude or longitude values'}, status=400)

        # Fetch the QR code owner
        try:
            qr_owner = Profile.objects.get(user__id=qr_user_id)
        except Profile.DoesNotExist:
            return JsonResponse({'error': 'QR code owner not found'}, status=404)

        # Calculate distance
        distance = calculate_distance(qr_lat, qr_lon, scanner_lat, scanner_lon)
        if distance > 100:
            return JsonResponse({'error': 'Users must be within 10 meters to verify meetup', 'distance': round(distance, 2)}, status=400)

        # Store meetup in the database
        meetup = Meetup.objects.create(
            scanner=scanner,
            scanned=qr_owner,
            location=scanner_address,  # Store address instead of lat/lon
            timestamp=now()
        )

        return JsonResponse({
            'success': True,
            'message': 'Meetup verified!',
            'meetup_id': meetup.id,
            'distance': round(distance, 2),
            'scanner_username': scanner.user.username,
            'qr_owner_username': qr_owner.user.username,
            'location': scanner_address,  # Return the address
            'timestamp': meetup.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        })
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


@login_required
def user_profile_page(request, username=None):
    if username:  # Fetch the profile by username if provided
        profile = get_object_or_404(Profile, user__username=username)
    else:  # Default to the logged-in user's profile if no username is given
        profile = request.user.profile

    meetups = MeetupToDo.objects.filter(user=request.user)
    following_list = profile.follows.all()

    if 'person_to_meet' in request.POST and 'meet_time' in request.POST:
            person_to_meet = request.POST['person_to_meet']
            meet_time = request.POST['meet_time']
            MeetupToDo.objects.create(user=request.user, person_to_meet=person_to_meet, meet_time=meet_time)
            return redirect('profile', username=profile.user.username)  # Redirect after adding to-do item

    return render(request, 'profile.html', {
        'profile': profile,
        'meetups': meetups,
        'following_list': following_list
    })

@login_required
def delete_meetup(request, meetup_id):
    # Check if the request is a POST (we're doing it via AJAX, so it should be POST)
    if request.method == 'POST':
        # Get the meetup object or return a 404 if it doesn't exist
        meetup = get_object_or_404(MeetupToDo, id=meetup_id, user=request.user)
        
        # Delete the meetup
        meetup.delete()
        
        # Return a JSON response indicating success
        return JsonResponse({'success': True})

    # If the method is not POST, we can return an error response
    return JsonResponse({'success': False}, status=400)

@login_required
def dashboard(request):
    profile = request.user.profile
    following = profile.follows.all()

    # Ensure user's own posts are included
    posts = Post.objects.filter(user__profile__in=following) | Post.objects.filter(user=request.user)
    posts = posts.order_by("-created_at")  # Latest first

    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        return redirect("dashboard")

    return render(request, "dashboard.html", {"posts": posts, "form": form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Order by latest posts
    paginator = Paginator(posts, 5)  # Load 5 posts per page

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posts_json = [
            {
                "user": post.user.username,
                "text": post.text,
                "created_at": post.created_at.strftime("%B %d, %Y, %I:%M %p"),
                "image": post.image.url if post.image else None,
                "id": post.id,
            }
            for post in page_obj
        ]
        return JsonResponse({"posts": posts_json})

    return render(request, "posts.html", {"posts": page_obj})

def update_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        action = request.POST.get('action')  # action could be 'like' or 'comment'
        post = get_object_or_404(Post, id=post_id)

        if action == 'like':
            # Toggle the like/unlike action
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
            response = {
                'like_count': post.like_count(),
                'liked': request.user in post.likes.all()
            }

        elif action == 'comment':
            comment_text = request.POST.get('comment_text')
            # Create a new comment
            comment = Comment.objects.create(
                user=request.user,
                post=post,
                text=comment_text
            )
            response = {
                'comment_count': post.comment_count(),
                'comment_text': comment.text,
                'comment_user': comment.user.username,
                'created_at': comment.created_at.strftime("%b %d, %Y %H:%M")
            }

        return JsonResponse(response)
    
@login_required
def message_page(request, receiver_id):
    """Show a conversation between the logged-in user and another user."""
    receiver = User.objects.get(id=receiver_id)
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=receiver)) |
        (Q(sender=receiver) & Q(receiver=request.user))
    ).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            # Create and save the message
            Message.objects.create(sender=request.user, receiver=receiver, content=content, timestamp=now())
            return redirect('message_page', receiver_id=receiver.id)
    else:
        form = MessageForm()

    return render(request, 'message_page.html', {'messages': messages, 'receiver': receiver, 'form': form})