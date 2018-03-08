import csv

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from members.models import Status
from .models import Member


@login_required
def index(request):
    member_list = Member.objects.all()
    context = {'member_list': member_list}
    return render(request, 'members/index.html', context)


@login_required
def detail(request, member_id):
    context = {'member': get_object_or_404(Member, pk=member_id)}
    return render(request, 'members/detail.html', context)


@login_required
def upload(request):
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file'].read().decode('utf-8').splitlines()[1:]
        Member.create_all(csv.reader(csvfile), status=request.POST.get('status', Status.ACTIVE))
    return redirect('index')
