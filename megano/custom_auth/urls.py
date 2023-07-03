from django.urls import path

from . import views
from .views import SignInView, SignUpView, signOut, ProfileView, ProfilePasswordView

urlpatterns = [
    path("sign-in/", SignInView.as_view(), name="login"),
    path("sign-up/", SignUpView.as_view(), name="register"),
    path('sign-out/', views.signOut),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/password/", views.ProfilePasswordView.as_view(), name="profile-password"),
    path("profile/avatar/", views.ProfileAvatarView.as_view(), name="profile-avatar"),
]
