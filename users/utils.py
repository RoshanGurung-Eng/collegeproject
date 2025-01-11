from django.contrib.auth.hashers import make_password
from users.models import UserDetails
from rest_framework.exceptions import ValidationError

def create_user(username, email, password):
    # Check if username is provided
    if not username:
        raise ValidationError("Username is required.")  # Raise an error if username is not provided

    # Check if email is provided
    if not email:
        raise ValidationError("Email is required.")  # Raise an error if email is not provided

    # Hash the password
    hashed_password = make_password(password)  # Hash the password before saving

    # Check if user already exists by email
    if UserDetails.objects.filter(email=email).exists():
        raise ValidationError("Email is already taken.")  # Raise an error if email already exists

    # Create or get the user details
    user_details, created = UserDetails.objects.get_or_create(
        username=username,
        email=email,
        defaults={'password': hashed_password}  # Set the hashed password if not provided
    )

    return user_details
