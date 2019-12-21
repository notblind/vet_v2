from django import forms

class CommentsForm(forms.Form):
	message = forms.CharField(label='Ваш отзыв', max_length=300, required=True, widget=forms.Textarea)

	message.widget.attrs.update({'class':'form-control', 'placeholder':'Сообщение', 'rows':6})

