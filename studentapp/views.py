from django.shortcuts import render

def student_form(request):

    if request.method == "POST":

        student_name = request.POST.get("student_name")
        student_id = request.POST.get("student_id")

        # Validation
        if not student_name:
            return render(
                request,
                'student_form.html',
                {'error': 'Student Name cannot be blank.'}
            )

        if not student_id:
            return render(
                request,
                'student_form.html',
                {'error': 'Student ID cannot be blank.'}
            )

        major = request.POST.get("major")
        standing = request.POST.get("standing")
        graduation = request.POST.get("graduation")
        comments = request.POST.get("comments")

        languages = request.POST.getlist("languages")

        context = {
            'student_name': student_name,
            'student_id': student_id,
            'major': major,
            'standing': standing,
            'languages': ", ".join(languages),
            'graduation': graduation,
            'comments': comments,
        }

        return render(request, 'results.html', context)

    return render(request, 'student_form.html')