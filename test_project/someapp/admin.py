from django.contrib import admin
from .models import SomeModel, SomeOtherModel, HitCount

admin.site.register(SomeModel)
admin.site.register(SomeOtherModel)
admin.site.register(HitCount)
