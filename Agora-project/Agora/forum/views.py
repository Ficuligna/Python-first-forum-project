from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from django.http import HttpResponseBadRequest
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from .mixins import CreaSezioneMixin
from .models import Discussione,Post,Sezione
from .forms import AggiungiRisposta,FormDiscussione

# Create your views here.

class CreaSezione(CreaSezioneMixin,CreateView):
    model = Sezione
    fields = "__all__"
    template_name = "forum/crea_sezione.html"
    success_url = "/"

def show_sezione(request, pk):
    sezione = get_object_or_404(Sezione, pk=pk)
    discussioni = Discussione.objects.filter(sezione_appartenenza = sezione).order_by("data")
    context = {"sezione":sezione, "discussioni": discussioni}
    return render(request, "forum/show_sezione.html", context)

@login_required
def crea_discussione(request,pk):
    sezione = get_object_or_404(Sezione, pk = pk)
    if request.method == "POST":
        form = FormDiscussione(request.POST)
        if form.is_valid():
            discussione = form.save(commit=False)
            discussione.sezione_appartenenza = sezione
            discussione.creatore = request.user
            discussione.save()
            primo_post = Post.objects.create(
            discussione_appartenenza = discussione,
            creatore = request.user , testo = form.cleaned_data["contenuto"])
            return HttpResponseRedirect(discussione.get_absolute_url())

    else:
        form = FormDiscussione()
    context = {"form": form}
    return render(request, "forum/crea_discussione.html", context)

def show_discussione(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    posts = Post.objects.filter(discussione_appartenenza = discussione)
    form_risposta = AggiungiRisposta()
    context = {"discussione": discussione , "posts": posts, "form_risposta": form_risposta}
    return render(request, "forum/show_discussione.html", context)

def aggiungi_risposta(request, pk):
    discussione = get_object_or_404(Discussione, pk=pk)
    if request.method == "POST":
        form = AggiungiRisposta(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.discussione_appartenenza = discussione
            form.instance.creatore = request.user
            form.save()
            return HttpResponseRedirect(discussione.get_absolute_url())
    else:
        return HttpResponseBadRequest()

class CancellaPost(DeleteView):
    model = Post
    success_url = "/"
