from django.contrib import admin
from .models import SomeModel, SomeOtherModel

admin.site.register(SomeModel)
admin.site.register(SomeOtherModel)
