from django.shortcuts import render


def index(request):
    members_list = []
    context = {'members_list': members_list}
    return render(request, 'members/index.html', context)


def detail(request, member_id):
    context = {'member_id': member_id}
    return render(request, 'members/detail.html', context)
