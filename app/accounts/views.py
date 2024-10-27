from django.contrib.auth import get_user_model, update_session_auth_hash
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect
from django.template.context_processors import request
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

    def get_object(self, queryset=None):
        if not self.request.user.is_anonymous:
            return self.request.user
        raise Http404()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_user'] = self.form_class(instance=self.object)
        context['form_pass'] = self.pass_form_class(user=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_user = self.form_class(request.POST, instance=self.object)
        form_pass = self.pass_form_class(user=self.object, data=request.POST)
        if form_user.is_valid() and "save_profile" in request.POST:
            form_user.save()
            return HttpResponseRedirect(reverse_lazy('user_profile'))
        elif form_pass.is_valid() and 'save_password' in request.POST:
            user = form_pass.save()
            request.session.cycle_key()
            if hasattr(user, "get_session_auth_hash"):
                request.session["_auth_user_hash"] = user.get_session_auth_hash()
            return HttpResponseRedirect(reverse_lazy('user_profile'))

        return self.render_to_response(self.get_context_data(form_user=form_user, form_pass=form_pass))
