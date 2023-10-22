from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django_htmx.http import HttpResponseClientRedirect
User = get_user_model()

# Create your views here.
def login_user(request):
    ctx = {}
    return render(request, 'accounts/login.html', ctx)

def register(request):
    ctx = {}
    return render(request, 'accounts/register.html', ctx)

def htmx_login(request):
    status = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"testing >>> : {username} {password}")
        if len(username) == 0:
            status = "Username is required"
        elif len(password) == 0:
            status = "Password is required"
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                status = "Login successful"
            else:
                status = "Invalid username or password"
    ctx = {'status': status}
    return render(request, 'partials/login_form.html', ctx)

def htmx_register(request):
    if request.method=='POST':
    #extraction
        username=request.POST.get('username')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        email=request.POST.get('email')
        print(f"testing >>> : {username} {password} {cpassword} {email}")
        if len(username) == 0:
            status = "Username is required"
        elif len(password) == 0:
            status = "Password is required"
        elif len(cpassword) == 0:
            status = "cPassword is required"
        elif len(email) == 0:
            status = "email is required"
        #validation
        #todo
        #processin 
        else:
            user=User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()
            return HttpResponseClientRedirect('/')
    ctx={}
    return render(request, 'partials/register_form.html', ctx)