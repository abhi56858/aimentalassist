from django.contrib import admin
from django.urls import path, include  # Added 'include'
from django.views.generic.base import RedirectView
from api.views import RegisterView, ProfileView, GoogleLogin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', RedirectView.as_view(url='/api/login/'), name='root-redirect'),

    path('admin/', admin.site.urls),
    
    path('accounts/', include('allauth.urls')), 

    path('api/register/', RegisterView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/profile/', ProfileView.as_view()),
    path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),
]