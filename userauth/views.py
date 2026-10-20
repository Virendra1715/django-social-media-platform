from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikePost,Followers
from django.db.models import Q

def signup(request):
    try:
        if request.method == 'POST':
            fnm = request.POST.get('fnm')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')

            my_user = User.objects.create_user(
                username=fnm,
                email=emailid,
                password=pwd
            )

            new_profile = Profile.objects.create(
                user=my_user,
                id_user=my_user.id
            )

            login(request, my_user)

            return redirect('/')

        return render(request, 'signup.html')

    except:
        invalid = "User already exists"
        return render(
            request,
            'signup.html',
            {'invalid': invalid}
        )


def loginn(request):

    if request.method == 'POST':

        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')

        userr = authenticate(
            request,
            username=fnm,
            password=pwd
        )

        if userr is not None:
            login(request, userr)
            return redirect('/')

        invalid = 'Invalid Credentials'

        return render(
            request,
            'loginn.html',
            {'invalid': invalid}
        )

    return render(request, 'loginn.html')


def logoutt(request):

    logout(request)

    return redirect('loginn')


def upload(request):

    if request.method == 'POST':

        image = request.FILES.get('image_upload')
        caption = request.POST.get('caption')

        Post.objects.create(
            user=request.user.username,
            image=image,
            caption=caption
        )

        return redirect('/')

    return redirect('/')



@login_required(login_url='loginn')
def home(request):

    # Get the current user's profile.
    # Create it if it doesn't exist.
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    # Get users followed by the current user
    following_users = Followers.objects.filter(
        follower=request.user.username
    ).values_list('user', flat=True)

    # Get posts from the current user and followed users
    posts = Post.objects.filter(
        Q(user=request.user.username) |
        Q(user__in=following_users)
    ).order_by('-created_at')

    context = {
        'post': posts,
        'profile': profile,
    }

    return render(request, 'main.html', context)

def search_results(request):

    query = request.GET.get('q', '')

    users = User.objects.filter(
        username__icontains=query
    )

    return render(
        request,
        'userauth/search.html',
        {
            'users': users,
            'query': query
        }
    )


def likes(request, id):

    username = request.user.username

    post = get_object_or_404(Post, id=id)

    like_filter = LikePost.objects.filter(
        post_id=id,
        username=username
    ).first()

    if like_filter is None:

        LikePost.objects.create(
            post_id=id,
            username=username
        )

        post.no_of_likes += 1

    else:

        like_filter.delete()

        post.no_of_likes -= 1

    post.save()

    return redirect('/')


def explore(request):

    post = Post.objects.all().order_by('-created_at')

    profile = Profile.objects.get(
        user=request.user
    )

    context = {
        'post': post,
        'profile': profile
    }

    return render(
        request,
        'explore.html',
        context
    )


def profile(request, id_user):

    # Find the user whose profile is being opened
    user_object = get_object_or_404(
        User,
        username=id_user
    )

    # Find that user's profile
    user_profile = get_object_or_404(
        Profile,
        user=user_object
    )

    # Find that user's posts
    user_posts = Post.objects.filter(
        user=id_user
    ).order_by('-created_at')

    user_post_length = user_posts.count()

    # Current logged-in user
    follower = request.user.username

    # Profile being viewed
    user = id_user

    # Check whether current user is already following this user
    if Followers.objects.filter(
        follower=follower,
        user=user
    ).first():

        follow_unfollow = 'Unfollow'

    else:

        follow_unfollow = 'Follow'

    # Number of followers this user has
    user_followers = Followers.objects.filter(
        user=id_user
    ).count()

    # Number of users this user is following
    user_following = Followers.objects.filter(
        follower=id_user
    ).count()

    # Context sent to profile.html
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'profile': user_profile,
        'follow_unfollow': follow_unfollow,
        'user_following': user_following,
        'user_followers': user_followers,
    }

    # Only the owner can edit their profile
    if request.user.username == id_user:

        if request.method == 'POST':

            bio = request.POST.get('bio')
            location = request.POST.get('location')
            image = request.FILES.get('image')

            user_profile.bio = bio
            user_profile.location = location

            if image:
                user_profile.profileimg = image

            user_profile.save()

            return redirect(
                'profile',
                id_user=id_user
            )

    return render(
        request,
        'profile.html',
        context
    )

def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if Followers.objects.filter(
            follower=follower,
            user=user
        ).first():

            delete_follower = Followers.objects.get(
                follower=follower,
                user=user
            )
            delete_follower.delete()

            return redirect('/profile/' + user)

        else:
            new_follower = Followers.objects.create(
                follower=follower,
                user=user
            )

            return redirect('/profile/' + user)

    return redirect('/')