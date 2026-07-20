from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# from userauths.models import User


User = get_user_model()

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]