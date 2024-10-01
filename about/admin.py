from django.contrib import admin
from .models import Bio, Education, Experience, Hobby, Interest, Skill

# Register your models here.
admin.site.register(Bio)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Hobby)
admin.site.register(Interest)
