from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Sezione(models.Model):
    titolo = models.CharField(max_length = 80)
    descrizione = models.CharField(max_length = 150, blank=True, null=True )
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("show_sezione", kwargs={"pk":self.pk})

    class Meta:
        verbose_name = "Sezione"
        verbose_name_plural = "Sezioni"


class Discussione(models.Model):
    titolo = models.CharField(max_length = 80)
    data = models.DateTimeField(auto_now_add = True)
    sezione_appartenenza = models.ForeignKey(Sezione, on_delete=models.CASCADE)
    creatore = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "discussioni")

    def __str__(self):
        return self.titolo

    def get_absolute_url(self):
        return reverse("show_discussione", kwargs={"pk":self.pk})

    class Meta:
        verbose_name = "Discussione"
        verbose_name_plural = "Discussioni"

class Post(models.Model):
    testo = models.TextField()
    data = models.DateTimeField(auto_now_add = True)
    discussione_appartenenza = models.ForeignKey(Discussione, on_delete=models.CASCADE)
    creatore = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts")

    def __str__(self):
        return self.creatore.username

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
