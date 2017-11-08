from django.contrib import admin
from veterinarias.models import Pasciente, PascienteAdmin, Veterinario, VeterinarioAdmin
# Register your models here.
admin.site.register(Pasciente, PascienteAdmin)
admin.site.register(Veterinario, VeterinarioAdmin)
