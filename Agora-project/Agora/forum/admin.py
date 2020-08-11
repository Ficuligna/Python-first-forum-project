from django.contrib import admin
from .models import Discussione, Post, Sezione
# Register your models here.

class DiscussioneAdmin(admin.ModelAdmin):
    model = Discussione
    list_display = ["titolo","sezione_appartenenza","creatore"]
    search_fields = ["titolo", "creatore"]
    list_filter = ["sezione_appartenenza", "data"]

class SezioneAdmin(admin.ModelAdmin):
    model = Sezione
    list_display = ["titolo","descrizione"]
    search_fields = ["titolo"]
    list_filter = ["titolo"]

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["discussione_appartenenza","creatore"]
    search_fields = ["testo", "creatore", "discussione_appartenenza"]
    list_filter = ["discussione_appartenenza", "data"]

admin.site.register(Sezione,SezioneAdmin)
admin.site.register(Discussione,DiscussioneAdmin)
admin.site.register(Post,PostAdmin)
