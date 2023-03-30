from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import PollForm
from .models import Question, Choice
from django.utils import timezone


# Create your views here.
#
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     #output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     #template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list
#     }
#     #return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)
#
# # def index(request):
# #     return HttpResponse("HELLO!")
#
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     #return HttpResponse("You're looking at question %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
#
def hellow(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions. """
        # return Question.objects.order_by('-pub_date')[:5]
        """Return the last five published questions (not including those set to be
           published in the future)."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    # model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didnot select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def new(request):
    return render(request, 'polls/form_create.html')


def createmodelform1(request):
    # POST라면 입력한 내용을 form을 이용하여 데이터베이스에 저장
    if request.method == 'POST':
        form = pollForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('polls:index')

    # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = pollForm()
        return render(request, 'polls/form_create.html', {'form': form})


def pollcreateform(request):
    if request.method == 'POST':  # POST라면 입력한 내용을 form을 이용하여 데이터베이스에 저장
        form = PollForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('polls:index')
        else:
            return redirect('polls:index')
    # GET이라면 입력값을 받을 수 있는 html을 가져다 줘야함
    else:
        form = PollForm()
        return render(request, 'polls/form_create.html', {'form': form})


class PollCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question_text', 'pub_date']
    template_name = 'polls/question_form.html'
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
