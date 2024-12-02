from django.http import HttpResponse
from security.models import User
from django.core.exceptions import ValidationError

def unsafe_users(request, user_id):
    """Fixed SQL injection vulnerability with proper validation"""

    # Ensure user_id is a valid integer
    try:
        user_id = int(user_id)  # Attempt to convert user_id to an integer
    except ValueError:
        return HttpResponse("Invalid user ID", status=400)  # Return an error if conversion fails

    # Retrieve the user safely using Django ORM
    try:
        user = User.objects.get(id=user_id)
        return HttpResponse(f"User {user.id} {user.username}")  # Customize as per your model
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)
