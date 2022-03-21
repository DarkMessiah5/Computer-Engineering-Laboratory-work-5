from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http.response import JsonResponse

# Create your views here.

from .models import Student

class Index(TemplateView):

    template_name = 'index.html'

    existing_students = Student.objects.all()

    def get(self, request):
        self.existing_students = Student.objects.all()

        return render(request, self.template_name, {'existing_students' : self.existing_students})


class AddStudent(TemplateView):

    template_name = 'addStudent.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(post, request):
        Student.objects.create(name=request.POST.get("nf"), programing_mark=request.POST.get("pm"),
                               informatics_mark=request.POST.get("inf"), math_mark=request.POST.get("math"),
                               discrete_math_mark=request.POST.get("disc"), history_mark=request.POST.get("his"))

        return redirect('Index')


class ChangeMark(TemplateView):

    template_name = 'changeMark.html'

    existing_students = Student.objects.all()

    def get(self, request):
        self.existing_students = Student.objects.all()

        return render(request, self.template_name, {'existing_students': self.existing_students})

    def post(post, request):
        user = request.POST.get("sn")
        subject = request.POST.get("dn")
        mark = request.POST.get("mark-name")

        print(subject)

        student = Student.objects.get(pk=user)
        if (subject == 'pr'):
            student.programing_mark = mark
        elif (subject == 'inf'):
            student.informatics_mark = mark
        elif (subject == 'math'):
            student.math_mark = mark
        elif (subject == 'disc'):
            student.discrete_math_mark = mark
        elif (subject == 'hist'):
            student.history_mark = mark

        student.save()

        return redirect('Index')


def student_data_view(request, pk):
    student = Student.objects.get(pk=pk)
    data = {
        'pr': student.programing_mark,
        'inf': student.informatics_mark,
        'math': student.math_mark,
        'disc': student.discrete_math_mark,
        'hist': student.history_mark
    }

    return JsonResponse({
        'data': data
    })
