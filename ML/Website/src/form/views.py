import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import FormAvis #, Post, Rating
from .forms import AvisForm, Form_avis

# Create your views here.


def __str__(self):
    return self.name


def formulaire(request):
    form_personne_endlist= FormAvis.objects.filter().order_by('-id')[:10] #on affichera uniquements jusqu'aux 10 dernieres lignes des avis

    if request.method == "POST":
        form = Form_avis(request.POST)

        if form.is_valid():
            b = form.save(commit=False) #le model va etre cree par le formulaire mais pas encore sauvegarde dans la BD
            b.date = datetime.date.today()
            # print("Date = "+ str(b.date)+" Note="+ str(b.note))
            # print("Rate = " + str(b.rate))
            b.save()  # Sauvegarde dans la BD
            form = Form_avis()
    else:
        form = Form_avis()
    return render(request, "form/index.html", {"form": form, "endlist_personne": form_personne_endlist})


# def rate(request: HttpRequest, post_id: int, rating: int) -> HttpResponse:
#     # post = Post.objects.get(id=post_id)
#     post = FormAvis.objects.get(id=post_id)
#     # Rating.objects.filter(post=post, user=request.user).delete()
#     post.rating_set.create(note=rating)
#     return formulaire(request)
