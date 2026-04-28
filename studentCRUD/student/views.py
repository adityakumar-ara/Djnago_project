# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
# SHOW DATA
def show_students(request):
    all_std = Student.objects.all()
    data = {
        'students': all_std
    }
    return 
# EDIT DATA
def edit_student(request, id):
    std = Student.objects.get(id=id)
    if request.method == 'POST':
        std.name = request.POST.get('name')
        std.roll = request.POST.get('roll')
        std.village = request.POST.get('village')
        std.Email = request.POST.get('Email')


        if len(request.FILES) != 0:
            std.image = request.FILES.get('image')
        std.save()    
        return redirect('students')
    
    return render(request,'students/edit_student.html',{'i':std})


def delete_student(request, id):
    # 1. Database se us specific student ko nikal lo
    std = Student.objects.get(id=id)
    
    # 2. Usko hamesha ke liye database se uda (delete) do
    std.delete()
    
    # 3. Wapas apne students list wale page par chale jao
    return redirect('students')
