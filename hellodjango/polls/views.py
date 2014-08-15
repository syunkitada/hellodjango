from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
from django.views import generic
from django import forms
from hellodjango import bootstrap

# Create your views here.

# class based view
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.order_by('-pub_date')[:5]

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = request.POST
        else:
            data = {'msg': 'not valid'}
    else:
        data = {}
        form = ContactForm()

    return render(request, 'polls/detail.html', {
        'value': [ 'test', 'aaa' ],
        'poll': poll,
        'form': form,
        'form_data': {
            'action'      : reverse('polls:detail', args=(poll_id,)),
            'method'      : 'POST',
            'submit_value': 'Send',
        },
        'data': data
    })

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': poll,
            'error_message': "You don't selected choice",
            })
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))

class SubjectField(forms.CharField):
    def clean(self, value):
        if value == 'hoge':
            raise forms.ValidationError('hoge is bad')
        return value

class ContactForm(forms.Form):
    subject = SubjectField(max_length=10)
    title = forms.CharField(max_length=10)
    which = forms.BooleanField()


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
