from django.contrib.auth import get_user_model, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, FormView
from accounts.forms import CustomUserCreationForm, CustomUserUpdateForm, CustomPasswordChangeForm
from django.contrib.auth.views import PasswordChangeView


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class UserProfileUpdateView(UpdateView):
    model = get_user_model()
    form_class = CustomUserUpdateForm
    pass_form_class = CustomPasswordChangeForm
    template_name = 'dashboard/dashboard_user_profile.html'

    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'username': self.object.username})

    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        return get_object_or_404(self.model, username=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.object)
        context['form2'] = self.pass_form_class(user=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        form2 = self.pass_form_class(user=self.object, data=request.POST)
        if "save_profile" in request.POST and form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        elif 'save_password' in request.POST and form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse_lazy("login"))

        return self.render_to_response(self.get_context_data(form=form, form2=form2))