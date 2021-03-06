from django.http import  HttpResponseRedirect, HttpResponse 
from django.shortcuts import get_object_or_404, render 
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be 
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question 
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Exclude any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question 
    template_name = 'polls/results.html'

def testview(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

#    return HttpResponse("welcome to the page at %s" % request.path)

#def index(request):
 #   latest_question_list = Question.objects.order_by('-pub_date')[:5]
  #  context = {'latest_question_list':latest_question_list}
   # return render(request, 'polls/index.html', context)

#def detail(request, question_id):
 #   question = get_object_or_404(Question, pk=question_id)
  #  return render(request, 'polls/detail.html', {'question':question})

#def results(request, question_id):
 #   question = get_object_or_404(Question, pk=question_id)
  #  return render(request, 'polls/results.html', {'question':question})
    

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # display the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing
        # with POST data. this prevents data from being posted twice 
        # if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

 


