from django.shortcuts import render, redirect
from main import models



def quiz_detail(request, code):
    try:
        quiz = models.Quiz.objects.get(code=code)
        questions = models.Question.objects.filter(quiz=quiz)
        if request.method == 'POST':
            answer = models.Answer.objects.create(
                quiz = quiz,
                user_name = request.POST['user_name'],
                phone = request.POST.get('phone'),
                email = request.POST.get('email')
            )
            for key, value in request.POST.items():
                if key.isdigit():
                    models.AnswerDetail.objects.create(
                        answer = answer,
                        question_id = int(key),
                        user_answer_id = int(value)
                    )
            return redirect('answer_detail',answer.code)
        context = {
            'quiz':quiz,
            'questions':questions
        }
        return render(request, 'front/quiz-detail.html', context)
    except:
        return redirect('index')


def eror(request):
    return render(request, 'front/erorr/error.html')