from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        note = Note(title = title, content = content, tag = tag)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        unique_tags = Note.objects.order_by().values('tag').distinct()
        tags = []
        for k in unique_tags:
            tags.append(k['tag'])
        print(tags)
        return render(request, 'notes/index.html', {'notes': all_notes, 'tags': tags})

def delete(request, id):
    Note.objects.filter(id=id).delete()
    all_notes = Note.objects.all()
    return redirect('index')
    #return render(request, 'notes/index.html', {'notes': all_notes})

def edit(request, id):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        Note.objects.filter(id=id).update(title=title, content=content)
        return redirect('index')
    else:  
        edit_note = Note.objects.get(id=id)
        print(edit_note)
        return render(request, 'notes/edit.html', {'note': edit_note})   


def filter(request, tag):
    g = Note.objects.filter(tag=tag)
    return render(request, 'notes/filter.html', {'g': g, 'tag':tag})