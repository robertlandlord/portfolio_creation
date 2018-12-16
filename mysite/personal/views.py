from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import *
from portfolio.models import Portfolio


# HERE IS THE MEAT :-)

# Create your views here.

#homepage
def index(request):
    return render(request, 'personal/home.html')    
#contact
def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please contact me at ', 'robertlandlord@gmail.com', 'or', 'grahamrubin@wustl.edu']})
#logout
def logout_user(request):
    logout(request)
    return redirect('index')
#registration of users
class UserFormView(View):
    form_class = UserForm
    template_name = 'personal/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process the form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False) #storing user info locally

            # cleaning data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #change password
            user.set_password(password)
            user.save()


            #returns User objects if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # also need to make them a portfolio
                    portfolio = Portfolio(user=User.objects.get(username=username))
                    portfolio.save()
                    return redirect('index') # redirecting you back to the home page

        return render(request, self.template_name, {'form': form})
#login page
class LoginFormView(View):
    form_class = LoginForm
    template_name = 'personal/login_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process the form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            #user = form.save(commit=False) #storing user info locally

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            #returns User objects if credentials are correct
            # again, authenticating
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index') # redirecting you back to the home page
            else:
                return render(request, self.template_name ,
                                          {'error_message': "<ul class='errorlist'> <li> Error occurred, please try again! </li> </ul>", 'form': form})

        return render(request, self.template_name, {'form': form})

class PassChangeFormView(View):
    form_class = PassChangeForm
    template_name = 'personal/password_change_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process the form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():


            # cleaned (normalized) data
            # get the current user's user object from database
            user = request.user
            username = user.username
            password = form.cleaned_data['password']
            password_check = form.cleaned_data['password_check']

            #changing password
            if password == password_check: #if the two typed passwords were the same
                user.set_password(password)
                user.save()
            else:
                return render(request, self.template_name,
                              {'error_message': "<ul class='errorlist'> <li> Passwords did not match! </li> </ul>",
                                  'form': form})
            #returns User objects if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index') # redirecting you back to the home page

        return render(request, self.template_name, {'form': form})















