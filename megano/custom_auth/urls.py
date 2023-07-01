from django.urls import path
from .views import SignInView, SignUpView, signOut

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('sign-out/', signOut, name='sign_out'),
]
