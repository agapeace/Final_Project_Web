from django.shortcuts import render, redirect
from university.models import *
from .forms import StudForm, CreateUserForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def about_us(request):
    return render(request, 'university/about_us.html', {'title': 'About Us'})

def blog(request):
    return render(request, 'university/blog.html', {'title': 'Blog'})

def organizations(request):
    return render(request, 'university/organizations.html', {'title': 'Organization'})

def contact_us(request):
    return render(request, 'university/contact_us.html', {'title': 'Contact Us'})

def logins(request):
    return render(request, 'university/login.html', {'title': 'Login'})

def create(request):
    return render(request, 'university/create.html', {'title': 'Create'})

def update(request):
    return render(request, 'university/update.html', {'title': 'Update'})



def member(request):
    member1 = {"name": "Damir", "surname": "Agadilov", "phone": "87021324363", "email": "damir@mail.ru"}
    member2 = {"name": "Baglan", "surname": "Abitali", "phone": "87017777777", "email": "baga@mail.ru"}
    data = {"member1": member1, "member2": member2}

    return render(request, 'university/about_team.html', context=data)

def create(request):
    error = ''
    if request.method == 'POST':
        form = StudForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = "Form incorrect"
    form = StudForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'university/create.html', data)


class NewsDetailView(DetailView):
    model = Stud
    template_name = 'university/details_view.html'
    context_object_name = 'stud'


class UpdateView(UpdateView):
    model = Stud
    template_name = 'university/create.html'
    form_class = StudForm

class DeleteView(DeleteView):
    model = Stud
    success_url = '/'
    template_name = 'university/delete.html'

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)

            return redirect('sign_in')

    context = {'form': form}
    return render(request, 'university/sign_up.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('about_us')
        else:
            messages.info(request, 'Username or password is incorrect!')

    context = {}
    return render(request, 'university/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('about_us')