from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

# class형 view
# index page
class IndexView(generic.ListView):
    # html
    template_name = 'polls/index.html'
    # context 이름?
    context_object_name = 'latest_question_list'

    # 보여질때 갯수, pub_date 기준 정렬 상태
    def get_queryset(self):
        '''REturn the last five published questions.'''
        return Question.objects.order_by('-pub_date')[:5]

# 상세 페이지
class DetailView(generic.DetailView):
    # 연결 모델
    model = Question
    # html
    template_name = 'polls/detail.html'

# 결과 페이지
class ResultView(generic.DetailView):
    # 연결 모델
    model = Question
    # html
    template_name = 'polls/results.html'

# 투표
def vote(request, question_id):
    # 질문이있으면 pk의 질문
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 질문의 항목 선택 값 받기?
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExixt):
        # Redisplay the question voting from.
        return render(request, 'polls/detail.html', {'question':question, 'error_message':"You didn't select a choice.",})
    else:
        # 투표 1 증가
        selected_choice.votes += 1
        # 투표 저장
        selected_choice.save()
        # 투표가 끝나면 결과페이지로 이동
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# 함수형 view
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list' : latest_question_list,
#     }
#
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})