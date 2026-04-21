from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

def registro_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = UserCreationForm()

    return render(request, 'registro/registro.html', {'formulario': formulario})

def inicio(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def perfil(request):
    if request.method == 'POST':
        # Si el formulario fue enviado, actualizamos el perfil
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirigimos a la misma página después de guardar
    else:
        # Si no, mostramos el formulario vacío
        form = UserChangeForm(instance=request.user)

    return render(request, 'perfil.html', {'form': form})