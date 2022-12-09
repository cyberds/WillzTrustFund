from django.shortcuts import render, redirect
from .models import Lead
from .forms import EnquiryForm
from django.contrib import messages
from company.models import Company

# Create your views here.
def contact_us(request):
    company = Company.objects.get(id=1, is_client=False)

    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            data = Lead()
            data.full_name = form.cleaned_data['full_name']
            data.email = form.cleaned_data['email']
            data.company_name = form.cleaned_data['company_name']
            data.job_title = form.cleaned_data['job_title']
            data.involvement = form.cleaned_data['involvement']
            data.program = form.cleaned_data['program']
            data.message = form.cleaned_data['message']
            data.channel = form.cleaned_data['channel']
            data.save()
            messages.success(request, 'Thank you! Your enquiry has been submitted.')
            return redirect('contact_us')

    else:
        form = EnquiryForm()

    context = {
        'company': company,
        'form': form,
    }
    return render(request, 'contact.html', context)

def get_involved(request, involvement):
    company = Company.objects.get(id=1, is_client=False)

    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            data = Lead()
            data.full_name = form.cleaned_data['full_name']
            data.email = form.cleaned_data['email']
            data.company_name = form.cleaned_data['company_name']
            data.job_title = form.cleaned_data['job_title']
            data.involvement = form.cleaned_data['involvement']
            data.program = form.cleaned_data['program']
            data.message = form.cleaned_data['message']
            data.channel = form.cleaned_data['channel']
            data.save()
            messages.success(request, 'Thank you! Your enquiry has been submitted.')
            return redirect('get_involved')

    else:
        form = EnquiryForm()

    context = {
        'involvement': involvement,
        'company': company,
        'form': form,
    }
    return render(request, 'get_involved.html', context)
