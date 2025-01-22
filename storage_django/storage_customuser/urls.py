from django.urls import path
from .views import signup, LoginView, EmployeeView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('employees/', EmployeeView.as_view(), name='employees'),
]