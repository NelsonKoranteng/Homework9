
from django.urls import path
from . import views

urlpatterns = [
    # SQL injection
    # http://127.0.0.1:8080/security/unsafe/users/1%20or%201
    path('unsafe/users/<user_id>', views.unsafe_users, name='unsafe_users')    
    
]
