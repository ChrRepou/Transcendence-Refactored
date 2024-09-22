from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PlayerCreationForm

# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         form = PlayerRegistrationForm(request.POST)
#         if form.is_valid():
#             # Save the user
#             form.save()
#             email = form.cleaned_data.get('email')
#             print(f'Account created for {email}!')
#             messages.success(request, f'Account created for {email}!')
#             return JsonResponse({'success': True, 'redirect_url': '/login'})
#         else:
#             errors = form.errors.as_json()
#             return JsonResponse({'success': False, 'errors': errors, 'form': form.as_table()})
#     else:
#         form = PlayerRegistrationForm()
#     return render(request, 'skeleton.html', {'form': form})


def main(request):
    return render(request, 'index.html')

class SignUpView(CreateView):
    form_class = PlayerCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
