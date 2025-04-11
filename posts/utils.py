from .models import Post
from profiles.models import Profile
from django.http import HttpResponse

def action_permission(func):
    def wrapper(request, **kwargs):
        pk = kwargs.get('pk')
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.get(pk=pk)
        print("Logged-in user ID:", profile.user.id)
        print("Post author ID:", post.author.user.id)
        if profile.user.id == post.author.user.id:
            print('yes')
            return func(request, **kwargs)
        else:
            print('no')
            return HttpResponse('access denied -you need to be the author of the post to delete it.')

    return wrapper