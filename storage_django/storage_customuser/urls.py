from django.urls import path
from .views import EmployeeView, CustomUserLoginView, CustomUserSignupView

urlpatterns = [
    path('signup/', CustomUserSignupView.as_view(), name='signup'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('employees/', EmployeeView.as_view(), name='employees'),
]