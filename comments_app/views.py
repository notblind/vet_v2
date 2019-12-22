from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View

from django.core.paginator import Paginator
from .models import CommentsModel
from personal.models import ClientModel
from .forms import CommentsForm


# Create your views here.

class Comments(View):
	
	def get(self, request):
		model = CommentsModel.objects.order_by('-timedate')
		paginator = Paginator(model, 4)
		page_number = request.GET.get('page', 1)
		page = paginator.get_page(page_number)

		is_paginated = page.has_other_pages()

		if page.has_previous():
			prev_url = '?page={}'.format(page.previous_page_number())
		else:
			prev_url = ''

		if page.has_next():
			next_url = '?page={}'.format(page.next_page_number())
		else:
			next_url = ''

		if request.user.is_authenticated:
			form = CommentsForm()
		else:
			form = None

		context = {
			'form':form,
			'model':page,
			'prev_url':prev_url,
			'next_url':next_url,
			'is_paginated':is_paginated,
		}

		return render(request,'comments/comments.html', context=context)

	def post(self, request):
		form = CommentsForm(request.POST)
		if form.is_valid():
			message = form.cleaned_data['message']
			client = ClientModel.objects.get(user=request.user)
			model = CommentsModel(client=client,message=message)
			model.save()
			return redirect('comments')
		return redirect('comments')