from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<10 :
            messages.error(request, "Please fill the form currectly ") 

        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your form has been successfully submit") 

    return render(request, 'home/contact.html')

def search(request):
    query=request.GET['query']
    if len(query)>80:
        allPosts=Post.objects.none()
    else:
        allPostsTitle=Post.objects.filter(title__icontains=query)
        allPostsContent=Post.objects.filter(content__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)

    if allPosts.count( )== 0:
        messages.warning(request, 'No search result found. Please refine your query')

    params={'allPosts':allPosts, 'query':query}
    return render(request, 'home/search.html', params)

def handleSignup(request):
    if request.method=='POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(uname)>10:
            messages.warning(request, 'User must be 10 character')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, 'Password did not match')
            return redirect('home')

        if not uname.isalnum():
            messages.error(request, 'User name should be contain number and chaaracter only')
            return redirect('home')



        myuser=User.objects.create_user(uname, email, pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, "Your iCoder account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Login")
            return redirect('home')

        else:
            messages.error(request, 'Invalid details')
            return redirect('home')
    return HttpResponse('404 - Not Found')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('home')
    
    

