from django.views.generic import TemplateView


class SignupView(TemplateView):
    template_name = 'user/signup.html'


class LoginView(TemplateView):
    template_name = 'user/login.html'


class ProfileView(TemplateView):
    template_name = 'user/profile.html'


class LogoutView(TemplateView):
    template_name = 'user/logout.html'
