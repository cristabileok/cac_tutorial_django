from django.shortcuts import render, HttpResponse
from .forms import ContactInfo
from .models import ContactsDatabase

# Create your views here.

def home(request):
    return render(request, "core/home.html")
    
def about(request):
    return render(request, "core/about.html")
    
def portfolio(request):
    '''portfolio_view = "<h2>Portafolio</h2>"
    portfolio_view += "<ul>"
    for i in ("Aplicación X", "Sitio Web Y", "Base de Datos Z"):
        portfolio_view += f"<li>{i}</li>"
    portfolio_view += "</ul>"
    return HttpResponse(
        base_h1 + portfolio_view)'''
    return render(request, "core/portfolio.html")

def contact(request):
    if request.method == 'POST':
        myForm = ContactInfo(request.POST)
        if myForm.is_valid():
            informationForm = myForm.cleaned_data
            form_name = informationForm['name']
            form_email = informationForm['email']
            form_phone = informationForm['phone']
            form_msj = informationForm['msj']
            
            art=ContactsDatabase.objects.create(name=form_name, email=form_email, phone=int(form_phone), msj=form_msj)
            
            
            return render(request, "core/contact_thanks.html", {'info':informationForm,'form_name':form_name})
            
            #return HttpResponse(
            #    f"<h1>Gracias por enviar el formulario</h2><p>{informationForm}</p>")
        
    else:
        myForm = ContactInfo()
            
    return render(request, "core/contact.html", {'form':myForm})