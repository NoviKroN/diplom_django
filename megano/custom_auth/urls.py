from django.urls import path
from .views import SignInView, SignUpView, signOut, ProfileView

urlpatterns = [
    path("sign-in/", SignInView.as_view(), name="login"),
    path("sign-up/", SignUpView.as_view(), name="register"),
    path('sign-out/', signOut, name='sign_out'),
    path("profile/", ProfileView.as_view(), name="profile"),
]
