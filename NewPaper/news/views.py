from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/news_create.html', {'form': form})

def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_detail', pk=news.id)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/news_edit.html', {'form': form})

def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'news/news_delete.html', {'news': news})