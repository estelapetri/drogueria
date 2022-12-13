from django.shortcuts import render

#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from drogueria.models import Medicamento
from drogueria.forms import Buscar
from drogueria.forms import MedicamentoForm 
from django.views import View 


class BuscarMedicamento(View):
    form_class = Buscar
    template_name = 'Drogueria/buscar_medicamento.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_medicamentos = Medicamento.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_medicamentos':lista_medicamentos})
        return render(request, self.template_name, {"form": form})

class AltaMedicamento(View):

    form_class = MedicamentoForm
    template_name = 'drogueria/alta_medicamento.html'
    initial = {"nombre":"", "droga":"", "codigo":"", "precio":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el medicamento {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})

        return render(request, self.template_name, {"form": form})