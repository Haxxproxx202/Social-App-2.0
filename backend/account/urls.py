from django.urls import path, include
from .views import dashboard, register, edit
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('login/', user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', dashboard, name='dashboard'),

    # change password
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # reset password
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),

]


x="https://127.0.0.1:8000/images/create/?title=cokolwiek&url=https://assets.winni.in/product/primary/2021/10/55603.jpeg"
yy = "https://images.immediate.co.uk/production/volatile/sites/30/2017/01/Bunch-of-bananas-67e91d5.jpg"
