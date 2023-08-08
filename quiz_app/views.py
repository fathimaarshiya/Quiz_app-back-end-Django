from django.shortcuts import render
from .models import Exam 

# Create your views here.


def quiz_view(request):
    questions = Exam.objects.order_by('?')[:5]
    context = {'questions': questions}
    return render(request, 'quiz/quiz.html', context)

def submit_quiz(request):
    if request.method == 'POST':
        questions = Exam.objects.order_by('?')[:5]
        correct answers = 0
        user_answers = {}
        
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            user_answers[question] = selected_option
            
            if selected_option == question.correct_option:
                 correct answers+= 1
        
        context = {'user_answers': user_answers, 'score': score}
        return render(request, 'quiz/quiz_result.html', context)
    
    return redirect('quiz:quiz')