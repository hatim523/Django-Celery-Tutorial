from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView

from task2.forms import ReviewForm


class ReviewEmailView(FormView):
    template_name = 'task2/review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!"
        return HttpResponse(msg)
