from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from .forms import VeterinarioForm
from veterinarias.models import Veterinario, Consulta, Pasciente
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def veterinarias_nueva(request):
    if request.method == "POST":
        formulario = VeterinarioForm(request.POST)
        if formulario.is_valid():
            consulta = Veterinario.objects.create(nombre=formulario.cleaned_data['nombre'], edad = formulario.cleaned_data['edad'])
            for pasciente_id in request.POST.getlist('veterinarios'):
                consulta = Consulta(pasciente_id=pasciente_id, consulta_id = consulta.id), Consulta(veterinario_id=veterinario_id,consulta_id = consulta.id)
                consulta.save()
            messages.add_message(request, messages.SUCCESS, 'Veterinario Guardado Exitosamente')
    else:
        formulario = VeterinarioForm()
    return render(request, 'veterinarias/veterinaria_editar.html', {'formulario': formulario})

def veterinario_editar(request, pk):
    consulta = get_object_or_404(Veterinario, pk=pk)
    if request.method == "POST":
        formulario = VeterinarioForm(request.POST, instance=consulta)
        if formulario.is_valid():
            consulta = formulario.save(commit=False)
            consulta.save()
            return redirect('veterinario_detalle', pk=consulta.pk)
    else:
        formulario = VeterinarioForm(instance=consulta)
    return render(request, 'veterinarias/veterinaria_editar.html', {'formulario': formulario})
