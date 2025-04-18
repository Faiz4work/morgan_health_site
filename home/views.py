from django.shortcuts import render

from .models import Staff

def home(request):
    return render(request, 'index.html')

def newstaff(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        profession = request.POST.get('profession')

        staff = Staff(first_name=first_name, last_name=last_name, email=email, profession=profession)
        staff.save()

        return render(request, 'newstaff.html', {'message': 'Staff added successfully'})
    

    else:   
        return render(request, 'newstaff.html')
