import re
from webbrowser import get
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from.models import Campaña
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

#Vista de Home, Recopila los datos desde la db y los muestra en el template home.
@login_required
def home(request):
        nombres = Campaña.objects.all()
        if len(nombres)>0:
            data = {'message':"Success" } # ,'nombres':nombres #
        return render(request, 'api/home.html', {"nombres":nombres})

#llamado al template edicionhome donde esta el crud para la actualizacion del estado.
@login_required
def edicionhome(request, nombre):
    nombres = Campaña.objects.get(nombre=nombre)
    return render(request, "api/edicionhome.html", {"nombres":nombres})
    

#Actualizacion a la base de datos mediante el select del template.
@login_required
def editarstatus(request):

    nombre = request.POST['nombre_campaña']
    statuscampaña = request.POST['scampaña']
    
    nombres = Campaña.objects.get(nombre=nombre)
    nombres.nombre = nombre
    nombres.statuscampaña = statuscampaña
    nombres.save()   
    
      
    return redirect('home')
      
   

  




class BeliveoStatus(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'jsonResponse/'

    def get(self,request):
        statuscampaña = list(Campaña.objects.values())
        status = { 'statuscampaña':statuscampaña}
        return JsonResponse(status)


def welcome(request):

    return render(request, 'api/welcome.html')