from django.shortcuts import render, redirect,get_object_or_404
from .models import studetn

# Create your views here.
def show_student(request):
    all_std = studetn.objects.all()
    data = {
        'students': all_std
    }
    return render(request, 'students.html', data)

def add_student (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        E_no = request.POST.get('E_no')
        image = request.FILES.get('image')
        studetn.objects.create(
            name = name,
            e_no = E_no,
            image = image,
        )
        return redirect('show_student')
    return render(request, 'create.html',)     


def edit_student(request, id):
    student_obj = get_object_or_404(studetn,id=id)
    # if studetn.student_obj != request.student_obj:
    #     return redirect('show_student')
    if request.method == 'POST':
        Up_name = request.POST.get('name')
        Up_ENO = request.POST.get('e_no')
        Up_image = request.FILES.get('image')
        student_obj.name = Up_name
        student_obj.e_no = Up_ENO
        if Up_image:
         student_obj.image = Up_image
        student_obj.save()
        return redirect('show_student')
    return render(request, 'edit.html',{'student':student_obj})    

def delete_student(request, id):
    student_obj = get_object_or_404(studetn, id=id)    
    student_obj.delete()
    return redirect('show_student')