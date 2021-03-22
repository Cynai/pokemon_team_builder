from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

def home(request):
    #create team lists for home page display
    #popular teams order by views and new teams order by most recently added
    popular_team_list = Team.objects.order_by('-views')[:4]
    new_team_list = Team.objects.order_by('-time')[:8]
    
    context_dict = {}
    context_dict['popular_teams'] = popular_team_list
    context_dict['new_teams'] = new_team_list 

    visitor_cookie_handler(request)

    #find out html address!!

    response = render(request, 'builder/home.html', context=context_dict)
    return response

def popular(request):
    popular_team_list = Team.objects.order_by('-views')
    
    context_dict = {}
    context_dict['popular_teams'] = popular_team_list

    visitor_cookie_handler(request)

    #find out html address!!

    reponse = render(request, 'builder/popular_teams.html', context=context_dict)
    return response

def recent(request):
    new_team_list = Team.objects.order_by('-time')[:8]
    
    context_dict = {}
    context_dict['new_teams'] = new_team_list

    visitor_cookie_handler(request)

    #find out html address!!

    reponse = render(request, 'builder/recent_teams.html', context=context_dict)
    return response

#@login_required
def share(request):
    if not request.user.is_authenticated():

    #list of public teams
    #list of private teams
    
    context_dict = {}

    else:
        return HttpResponse("You are not logged in.")
    
#@login_required
def share_priv_username(request, username_private_slug):

    #list of private teams
    
    context_dict = {}

#@login_required
def share_username(request, username_slug):

    #list of public teams
    
    context_dict = {}

#@login_required
def friends(request):

    #get list of friends
    #get list of each friend's teams

    context_dict = {}

#@login_required
def viewfriend(request, friendname_slug):

    #get list of friendname_slug's teams
    
    context_dict = {}

def builder(request):
    context_dict = {}

def buildteam(request, teamname_slug):
    context_dict = {}

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('builder:home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'builder/login.html')

def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request,
                  'builder/register.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('builder:home'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits
