from django.shortcuts import render
from .models import Student, Job
from .utils import model_implementation

def home(request):
    if request.method == 'POST':
        student_id = request.POST.get('student-id')
        recommended_jobs_with_sentiment = model_implementation(student_id)
        context = {
            'student_id': student_id,
            'recommended_jobs_with_sentiment': recommended_jobs_with_sentiment,
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')
