from django.shortcuts import redirect, render
from academico.models import Curso
from django.contrib import messages

# Create your views here.


def index(request):
    cursos = Curso.objects.all()
    return render(request, 'academico/gestionCursos.html', {'cursos': cursos})


def registrar_curso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, 'Curso guardado correctamente')
    return redirect('/')


def eliminar_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, 'Curso eliminado correctamente')

    return redirect('/')


def editar_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, 'academico/editar-curso.html', {'curso': curso})


def patch_curso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)

    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    messages.success(request, 'Datos actualizados correctamente')

    return redirect('/')
