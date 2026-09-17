from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


def dashboard(request):
    students = Student.objects.all()

    total_students = students.count()

    if total_students > 0:
        average = sum(student.total_marks for student in students) / total_students
    else:
        average = 0

    passed = students.filter(
        django_installation=1,
        template_usage=1
    ).count()

    needs_improvement = total_students - passed

    context = {
        "students": students,
        "total_students": total_students,
        "average": round(average, 2),
        "passed": passed,
        "needs_improvement": needs_improvement,
    }

    return render(request, "evaluation/dashboard.html", context)


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "evaluation/students.html",
        {"students": students}
    )


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    return render(
        request,
        "evaluation/student_detail.html",
        {"student": student}
    )


def add_student(request):

    if request.method == "POST":

        Student.objects.create(
            roll_number=request.POST["roll_number"],
            name=request.POST["name"],
            register_number=request.POST["register_number"],
            department=request.POST["department"],
            section=request.POST["section"],
            django_installation=int(request.POST["django_installation"]),
            template_usage=int(request.POST["template_usage"]),
            model_and_views=int(request.POST["model_and_views"]),
            output=int(request.POST["output"]),
        )

        return redirect("student_list")

    return render(request, "evaluation/student_form.html")