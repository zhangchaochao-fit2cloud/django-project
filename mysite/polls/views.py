from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


# Create your views here.

# index
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # 加载模板文件
    template = loader.get_template("polls/index.html")
    # 添加参数
    context = {
        'latest_question_list': latest_question_list
    }
    # render 载入模板
    # return HttpResponse(template.render(context, request))

    # django快捷方法
    return render(request, "polls/index.html", context)


# 详情
def detail(request, question_id):
    # get获取对象拿不到就抛异常
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exits")

    # django快捷函数 使用get函数 自动抛出404
    question = get_object_or_404(Question, pk=question_id)
    # get_list_or_404() 使用filter函数 自动抛出404

    # 根据外键进行添加值
    # question.choice_set.create(choice_text='Not much', votes=0)
    # question.choice_set.create(choice_text='The sky', votes=0)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # reverse 会将urls解析成具体的路径
        # HttpResponseRedirect 重定向到某个目录
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
