from django import forms

from .tasks import send_review_email_task


class ReviewForm(forms.Form):
    name = forms.CharField(label=forms.CharField(
        label='First Name',
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'FirstName'}
        )
    ))
    email = forms.EmailField(max_length=100)
    review = forms.CharField(label='Review', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['review']
        )