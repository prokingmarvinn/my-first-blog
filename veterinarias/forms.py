from django import forms

from .models import Veterinario, Pasciente
class VeterinarioForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Veterinario
        fields = ('nombre', 'edad', 'pascientes')
def __init__ (self, *args, **kwargs):
        super(VeterinarioForm, self).__init__(*args, **kwargs)
        self.fields["veterinarios"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["veterinarios"].help_text = "Ingreso de pascientes"
        self.fields["veterinarios"].queryset = Actor.objects.all()

#class PascienteForm(forms.ModelForm):
#todos los campos de Cliente
  # class Meta:
    #  model = Pasciente
     # fields = ('nombre', 'tipoproducto', 'descripcion', 'precio')
