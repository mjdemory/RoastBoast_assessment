from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import RoastBoastModel

from homepage.forms import InputThoughtsForm

# import string
#
# import random

# Create your views here.


def index(request):
    html = "index.html"
    roastsboast = RoastBoastModel.objects.all().order_by('post_date')
    return render(request, html, {"title": 'What does the ghost say?', "roastsboast": roastsboast})


def create_post_view(request):
    if request.method == "POST":
        form = InputThoughtsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # secret_key = string.ascii_letters + string.digits
            RoastBoastModel.objects.create(
                choices=data.get('choices'),
                body=data.get('body')
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = InputThoughtsForm()
    return render(request, "basic_form.html", {"form": form})


def boast_view(request):
    html = "boast.html"
    boasts = RoastBoastModel.objects.filter(choices=True).order_by('post_date')
    return render(request, html, {"posts": boasts})


def roast_view(request):
    html = "roast.html"
    roasts = RoastBoastModel.objects.filter(choices=False).order_by('post_date')
    return render(request, html, {"posts": roasts})


def upvote_view(request, upvote_id):
    post = RoastBoastModel.objects.filter(id=upvote_id).first()
    post.upvote += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote_view(request, downvote_id):
    post = RoastBoastModel.objects.filter(id=downvote_id).first()
    post.downvote -= 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# code from SohailAslam during study session
def sortbyvote_view(request):
    html = "sortedbyvote.html"
    posts = RoastBoastModel.objects.all()
    posts = list(posts)
    posts = sorted(posts, key=lambda x: x.votes, reverse=True)
    return render(request, html, {"votes": posts})

# def delete_vote_view(request, post_id):
#
#     return redirect("homepage")


