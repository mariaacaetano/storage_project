from django.urls import path
from .views import EmployeeView, CustomUserLoginView, CustomUserSignupView, UserInfoView

urlpatterns = [
    path('signup/', CustomUserSignupView.as_view(), name='signup'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path('user-info/', UserInfoView.as_view(), name='user-info'),
    path('employees/', EmployeeView.as_view(), name='employees'),
]