from django import forms
from django.shortcuts import get_object_or_404, render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Inventaire,Incident
import sweetify

# Create your views here.
def sing_up(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('/')
            print("=="*5, " NEW POST: ",name,email, password, repassword, "=="*5)

    context = {
        'error':error,
        'message':message
    }
    return render(request, 'inventaire/ajouterCompte.html', context)
def sing_in(request):
  
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                return redirect('/base')
            else:
                print("mot de pass incorrecte")
                
        else:
            print("User does not exist")

    return render(request, 'inventaire/connexion.html', {})
def connexion(request):
    return render(request, 'inventaire/connexion.html') 
def ajouter(request):
    return render(request, 'inventaire/ajouterCompte.html') 
def base(request):
    return render(request, 'inventaire/base.html') 
def inventaire(request):
    return render(request, 'inventaire/inventaire.html')
def edit(request):
        sn = request.GET.get('SN')
        inventaires = Inventaire.objects.filter(SN=sn)if sn else Inventaire.objects.all() 
        return render(request, 'inventaire/edit.html',{'inventaires': inventaires,'sn': sn})
def ajouterinv(request):
    error = False
    message = ""

    class InventoryItemForm(forms.ModelForm):
        class Meta:
            model = Inventaire
            fields = '__all__'

    if request.method == "POST":
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventaire')  # Redirect to the inventory list or another appropriate page
        else:
            error = True
            message = "Invalid data. Please check the fields."

    else:
        form = InventoryItemForm()

    context = {
        'form': form,
        'error': error,
        'message': message,
    }

    return render(request, 'inventaire/ajouterInventaire.html', context) 
def update(request):
    sn = request.POST.get('SN')
    print(sn)
    
    # Filter inventaires by SN if provided, else get all inventaires
    inventaires = Inventaire.objects.filter(SN=sn) if sn else Inventaire.objects.all()
    
    if request.method == 'POST':
        application = request.POST.get('Application')
        ip = request.POST.get('IP')
        marque = request.POST.get('Marque')
        disk = request.POST.get('Disk')
        cpu = request.POST.get('CPU')
        ram = request.POST.get('RAM')
        date = request.POST.get('Date')
        support = request.POST.get('Support')
        type = request.POST.get('Type')
        site = request.POST.get('Site')
        position = request.POST.get('Position')
        description = request.POST.get('Description')

       # Create a new Incident instance and set its attributes
        new_incident = Incident(SN=sn, Description=description, Application=application,Type=type)

        # Save the new incident to the database
        new_incident.save()


        # Update fields of each Inventaire instance
        for inventaire in inventaires:
            print(inventaire)
            inventaire.Application = application
            inventaire.IP = ip
            inventaire.Marque = marque
            inventaire.Disk = disk
            inventaire.CPU = cpu
            inventaire.RAM = ram
            inventaire.Date = date
            inventaire.Support = support
            inventaire.Type = type
            inventaire.Site = site
            inventaire.Position = position
            inventaire.save()

        return redirect('tableinventaire')  # Redirect to the appropriate page after the modification

    return render(request, 'inventaire/edit.html', {'inventaires': inventaires})

def tableinventaire(request):
    marque = request.GET.get('marque')
    inventaires = Inventaire.objects.filter(Marque=marque) if marque else Inventaire.objects.all()
    return render(request, 'inventaire/tableInventaire.html', {'inventaires': inventaires, 'marque': marque})

def supprimer_inventaire(request):
    inventaire_id = request.GET.get('SN')  # Changer en 'inventaire_id'
    
    if inventaire_id:
        try:
            inventaire = Inventaire.objects.get(pk=inventaire_id)
            marque = inventaire.Marque  # Récupère la marque de l'inventaire avant la suppression
            inventaire.delete()
        except Inventaire.DoesNotExist:
            pass
    
    return redirect(f"/tableinventaire?marque={marque}")

def search_by_sn(request):
    search_sn = request.GET.get('search_sn')  # Get the search query from the request

    # Perform the search using the SN field
    inventaires = Inventaire.objects.filter(SN=search_sn)

    return render(request, 'inventaire/tableInventaire.html', {'inventaires': inventaires})

def searchInc_by_sn(request):
    search_sn = request.GET.get('search_sn')  # Get the search query from the request

    # Perform the search using the SN field
    incidents = Incident.objects.filter(SN=search_sn)

    return render(request, 'inventaire/incident.html', {'incidents': incidents})

def incident(request):
    incidents = Incident.objects.all()
    return render(request, 'inventaire/incident.html', {'incidents': incidents})
