from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.

def employee_form_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Handle valid form submission (save the form data, send an email, etc.)
            return render(request, 'success.html')  # You can create a success page later
    else:
        form = EmployeeForm()

    return render(request, 'employee_form.html', {'form': form})
