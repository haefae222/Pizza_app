from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.utils.timezone import now
import uuid
#... any other imports

# this is for our actual classes, such as users and pizzas

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    qr_code_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

class Meetup(models.Model):
    scanner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="scanned_meetups")
    scanned = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="scanned_by_meetups")
    timestamp = models.DateTimeField(default=now)
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional location

    def save(self, *args, **kwargs):
        """Ensure users follow each other when a meetup is created."""
        if self.scanned not in self.scanner.follows.all():
            self.scanner.follows.add(self.scanned)
        if self.scanner not in self.scanned.follows.all():
            self.scanned.follows.add(self.scanner)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Meetup between {self.scanner.user.email} and {self.scanned.user.email} at {self.timestamp}"