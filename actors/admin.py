from django.contrib import admin

from actors.models import Actor, Role, Director, DirectorGenre

admin.site.register(Actor)
admin.site.register(Role)
admin.site.register(Director)
admin.site.register(DirectorGenre)
