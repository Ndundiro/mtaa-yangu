from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NeighbourHoodForm, PostForm
from .models import Neighbourhood

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'neighbourhood/index.html')


def add_mtaa(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            mtaa = form.save(commit=False)
            mtaa.admin = request.user.profile
            mtaa.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'create_mtaa.html', {'form': form})


def mitaa(request):
    mitaa_zote = Neighbourhood.objects.all()
    mitaa_zote = mitaa_zote[::-1]
    params = {
        'mitaa_zote': mitaa_zote,
    }
    return render(request, 'mitaa_zote.html', params)


# def create_post(request, mtaa_id):
#     mtaa = Neighbourhood.objects.get(id=mtaa_id)
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.mtaa = mtaa
#             post.user = request.user.profile
#             post.save()
#             return redirect('index')
#     else:
#         form = PostForm()
#     return render(request, 'create_post.html', {'form': form})



