from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile, Meetup, MeetupToDo, Post, Comment, Message
from django.utils.timezone import now
from django.urls import reverse
from .models import Profile, Post, Message
from .forms import UserSignupForm, PostForm, MessageForm
from .models import User

User = get_user_model()

class ModelTests(TestCase):
    
    # set up for creating a user and posts 
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", email="user1@example.com", password="password123")
        self.user2 = User.objects.create_user(username="user2", email="user2@example.com", password="password123")
        self.profile1 = Profile.objects.get(user=self.user1)
        self.profile2 = Profile.objects.get(user=self.user2)
        self.post = Post.objects.create(user=self.user1, text="Hello World!")
        self.message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hey!")

 # testing user creation
    def test_user_creation(self):
        self.assertEqual(self.user1.email, "user1@example.com")
        self.assertTrue(Profile.objects.filter(user=self.user1).exists())

# testing for following a user
    def test_follow_users(self):
        self.profile1.follows.add(self.profile2)
        self.assertTrue(self.profile2 in self.profile1.follows.all())

# can a user create a post
    def test_post_creation(self):
        self.assertEqual(self.post.text, "Hello World!")
        self.assertEqual(self.post.user, self.user1)

# can a user send a message
    def test_message_sending(self):
        self.assertEqual(self.message.sender, self.user1)
        self.assertEqual(self.message.receiver, self.user2)
        self.assertEqual(self.message.content, "Hey!")

# can a user like a post 
    def test_like_post(self):
        self.post.likes.add(self.user1)
        self.assertEqual(self.post.like_count(), 1)

# can a user comment 
    def test_comment_on_post(self):
        """Test adding comments to a post"""
        comment = Comment.objects.create(user=self.user2, post=self.post, text="Nice post!")
        self.assertEqual(comment.text, "Nice post!")
        self.assertEqual(self.post.comment_count(), 1)

# testing all forms 
class FormTests(TestCase):

    def test_valid_signup_form(self):
        form_data = {
            "email": "test@example.com",
            "password1": "password123",
            "password2": "password123"
        }
        form = UserSignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_signup_form(self):
        form_data = {
            "email": "test@example.com",
            "password1": "password123",
            "password2": "wrongpassword"
        }
        form = UserSignupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_valid_post_form(self):
        form_data = {"text": "Hello, world!"}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_message_form(self):
        form_data = {"content": ""}
        form = MessageForm(data=form_data)
        self.assertFalse(form.is_valid())

