from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
# Models
from .models import Workouts, Exercises
from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView



# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


# Add class for Workouts
class WorkoutsList(TemplateView):
    template_name = "workouts_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workout_name = self.request.GET.get("workout_name")
        if workout_name != None:
            context["workout_name"] = Workouts.objects.filter(workout_name__icontains=workout_name, user=self.request.user)
            context["header"] = f"Searching for {workout_name}"
        else:
            context["workout_name"] = Workouts.objects.all()   
            context["header"] = f"Searching for {workout_name}"
        return context
    
@method_decorator(login_required, name='dispatch')        
class WorkoutCreate(CreateView):
    model = Workouts
    fields = ['workout_name', 'video']
    template_name = "workout_create.html"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkoutCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('workouts_detail', kwargs={'pk': self.object.pk})
    
    
    
class WorkoutsDetail(DetailView):
    model = Workouts
    template_name = "workouts_detail.html"
    
    
    
class WorkoutUpdate(UpdateView):
    model = Workouts
    fields = ['workout_name', 'video']
    template_name = "workout_update.html"
    def get_success_url(self):
        return reverse('workouts_detail', kwargs={'pk': self.object.pk})
    
    
class WorkoutDelete(DeleteView):
    model = Workouts
    template_name = "workout_delete_confirmation.html"
    success_url = "/workouts/"


class ExerciseCreate(View):
    
    def post(self, request, pk):
        sets = request.POST.get("sets")
        reps = request.POST.get("reps")
        weight = request.POST.get("weight")
        notes = request.POST.get("notes")
        workout = Workouts.objects.get(pk=pk)
        Exercises.objects.create(
            sets=sets,
            reps=reps,
            weight=weight,
            notes=notes,
            workout=workout
            )
        return redirect('workouts_detail', pk=pk)
    
    
# class Signup(View):
#     def get(self, request):
#         form = UserCreationForm()
#         context = {"form": form}
#         return render(request, "registration/signup.html", context)
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("workouts_list")
#         else:
#             context = {"form": form}
#             return render(request, "registration/signup.html", context)



class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/login/')

        return render(request, self.template_name, {'form': form})
    

    
class CustomLoginView(LoginView):
    form_class = LoginForm
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        
        if not remember_me:
            self.request.session.set_expiry(0)
            
            self.request.session.modified = True
            
        return super(CustomLoginView, self).form_valid(form)
    
    
    
    
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
    
    
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')