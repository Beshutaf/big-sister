from django.shortcuts import render, get_object_or_404

from .models import Member


def index(request):
    members_list = Member.objects.all()
    context = {'members_list': members_list}
    return render(request, 'members/index.html', context)


def detail(request, member_id):
    context = {'member': get_object_or_404(Member, member_id)}
    return render(request, 'members/detail.html', context)
