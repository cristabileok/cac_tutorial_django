from django.shortcuts import render, HttpResponse

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
    '''contact_view = "<h2>Contacto</h2>"
    contact_view += "<ol>"
    for i in range(5):
        contact_view += f"<li>Contacto {i}</li>"
    contact_view += "</ol>"
    return HttpResponse(base_h1 + contact_view)'''
    return render(request, "core/contact.html")