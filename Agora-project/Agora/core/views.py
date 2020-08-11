from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.list import ListView
from forum.models import Discussione,Post,Sezione
# Create your views here.
class Homepage(ListView):
    queryset = Sezione.objects.all
    template_name = "core/homepage.html"

def profilo(request, username):
    utente = get_object_or_404(User,username = username)
    context = {"utente": utente}
    return render(request, "core/profilo_utente.html", context)

class UtentiListView(ListView):

    model = User
    template_name = "core/lista_utenti.html"
    paginate_by = 100  # if pagination is desired

def cerca(request):
    if "q" in request.GET:
        querystring = request.GET.get("q")
        if len(querystring) == 0:
            return redirect("/cerca/")
        discussioni = Discussione.objects.filter(titolo__icontains = querystring)
        posts = Post.objects.filter(testo__icontains = querystring)
        users = User.objects.filter(username__icontains = querystring)
        context = {"discussioni":discussioni,"posts":posts,"users":users}
        return render(request, "core/cerca.html", context)
    else:
        return render(request, "core/cerca.html")
