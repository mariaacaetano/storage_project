from django.urls import path
from .views import SignUpView, LoginView, EmployeeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('employees/', EmployeeView.as_view(), name='employees'),
]
