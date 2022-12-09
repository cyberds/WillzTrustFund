from django.shortcuts import render, redirect, get_object_or_404
from .models import Voter
from account.models import Account
from .forms import VoterForm, PreRegisterForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

def pre_register(request):
    if request.method == "POST":
        form = PreRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.errors)
            data = Voter()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.gender = form.cleaned_data['gender']
            data.phone = form.cleaned_data['phone']
            data.local_gov_area = form.cleaned_data['local_gov_area']
            data.state = form.cleaned_data['state']
            data.date_of_birth = form.cleaned_data['date_of_birth']

            data.channel = form.cleaned_data['channel']
            data.save()
            messages.success(request, 'Thank you! your details has been submitted.')
            return HttpResponseRedirect('https://cvr.inecnigeria.org/Home/start')
        else:
            messages.error(request, form.errors)

    else:
        form = PreRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'pre_register.html', context)

@login_required(login_url = 'login')
def voter(request):
    user = Account.objects.get(id=request.user.id)
    voters = Voter.objects.filter(user=user)
    if request.method == "POST":
        form = VoterForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            print(form.errors)
            data = Voter()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.gender = form.cleaned_data['gender']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.village = form.cleaned_data['village']
            data.local_gov_area = form.cleaned_data['local_gov_area']
            data.state = form.cleaned_data['state']
            data.postal_code = form.cleaned_data['postal_code']
            data.country = form.cleaned_data['country']
            data.date_of_birth = form.cleaned_data['date_of_birth']
            data.photo = form.cleaned_data['photo']

            data.is_registered = form.cleaned_data['is_registered']
            data.is_eligible = form.cleaned_data['is_eligible']
            data.willing_to_register = form.cleaned_data['willing_to_register']
            data.political_party = form.cleaned_data['political_party']

            data.channel = form.cleaned_data['channel']
            data.user = user
            data.save()
            messages.success(request, 'Thank you! voter details has been submitted.')
            return redirect('voter')

    else:
        form = VoterForm()

    context = {
        'form': form,
        'voters': voters,
    }
    return render(request, 'voter.html', context)

@login_required(login_url = 'login')
def update_voter(request, id):
    user = Account.objects.get(id=request.user.id)
    voters = Voter.objects.filter(user=user)

    updated_voter = get_object_or_404(Voter, id=id)
    form = VoterForm(request.POST or None, request.FILES or None, instance=updated_voter)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('voter')

    context = {
        'form': form,
        'voters': voters,
        'updated_voter': updated_voter,
    }

    return render(request, 'voter.html', context)

@login_required(login_url = 'login')
def delete_voter(request, id):
    deleted_voter = Voter.objects.get(id=id)
    deleted_voter.delete()
    return redirect('voter')
