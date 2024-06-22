from django.contrib import admin



from . import models


@admin.register(models.UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')


