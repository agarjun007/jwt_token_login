from django.urls import re_path,path
from django.contrib.auth import views as auth_views
from . import views  

urlpatterns = [
    path('',views.Login.as_view(),name='login'),
    path('signup/',views.Signup.as_view(),name='signup'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    # path('reset-password/',views.reset_password.as_view(),name='reset_password'),
    path('hello/', views.HelloView.as_view(), name='hello'),

    path('reset-password/',auth_views.PasswordResetView.as_view(template_name='forgot_password.html'),name='reset_password'),
    path('reset-password-sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
    path('reset<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset-password-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),




]
