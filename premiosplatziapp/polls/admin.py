from django.contrib import admin

from .models import Question,Choice


# class ChoiceAdmin(admin.ModelAdmin):
#     readonly_fields = ['vote'] # campo de solo lectura


admin.site.register([
    Question,
    Choice
])
   
   
# admin.site.register(apps.all_models.get('polls').values())
