from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Jugador
from .forms import JugadorForm

def jugador_list(request):
    jugadores = Jugador.objects.all()
    return render(request, 'jugadoresapp/jugador_list.html', {'jugadores': jugadores})

def jugador_detail(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    return render(request, 'jugadoresapp/jugador_detail.html', {'jugador': jugador})

@login_required
def jugador_nuevo(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            jugador = form.save(commit=False)
            jugador.usuario = request.user
            jugador.save()
            return redirect('jugador_detail', pk=jugador.pk)
    else:
        form = JugadorForm()
    return render(request, 'jugadoresapp/jugador_editar.html', {'form': form})
