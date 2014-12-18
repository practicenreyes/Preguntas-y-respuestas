from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from preguntasyrespuestas.models import Pregunta
from django.template import RequestContext
from preguntasyrespuestas.form import PreguntaForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	preguntas = Pregunta.objects.all()
	return render_to_response('preguntasyrespuestas/index.html', 
							 {'preguntas': preguntas},
							 context_instance=RequestContext(request))

def pregunta_detalle(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	return render_to_response('preguntasyrespuestas/pregunta_detalle.html',
							 {'pregunta': pregunta},
							 context_instance=RequestContext(request))

@login_required
def pregunta_crear(request):
	if request.method == 'POST':
		form = PreguntaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('preguntas')
	else:
		form = PreguntaForm()
	return render_to_response('preguntasyrespuestas/pregunta_crear.html',
							 {'form': form},
	 						 context_instance=RequestContext(request))

@login_required
def pregunta_editar(request, pregunta_id):
	pregunta = get_object_or_404(Pregunta, pk=pregunta_id)
	if request.method == 'POST':
		form = PreguntaForm(request.POST, instance=pregunta)
		if form.is_valid():
			form.save()
			return redirect('pregunta_detalle', pregunta_id)
	else:
		form = PreguntaForm(instance=pregunta)
	return render_to_response('preguntasyrespuestas/pregunta_editar.html',
							 {'form': form},
	 						 context_instance=RequestContext(request))
#[template_directory]/preguntasyrespuestas/index.html