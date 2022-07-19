from django.contrib import admin
from .models import Goal, Current_Goal, History

admin.site.register(Goal)
admin.site.register(Current_Goal)
admin.site.register(History)
