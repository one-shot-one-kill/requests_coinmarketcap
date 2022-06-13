from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound

from .models import Coin, CoinName, Comment
from .forms import CoinForm, CommentForm
from .parse import view_information  


def home(request):
	if request.method == 'POST':
		form = CoinForm(request.POST)
		if form.is_valid():
			form.save()
			coin_name = CoinName.objects.all()[0].name
			coin_info = view_information(coin_name)
			Coin.objects.create(name=coin_info['name'], slug=coin_info['name'],
				description=coin_info['description'], market_cap=coin_info['market_cap'],
				price=coin_info['price'])

	form = CoinForm()


	obj_list = Coin.objects.all()

	return render(request, 'main/pages/home.html', {'coins': obj_list, 'form': form})


def delete(request, id): 
	try:
		coin = Coin.objects.get(id=id)
		coin.delete()
		return HttpResponseRedirect('/')
	except Coin.DouesNotExists:
		return HttpResponseNotFound('<h2>Coin not found</h2>')


def detail(request, coin):
	coin = get_object_or_404(Coin, slug=coin)
	comments = coin.comments.filter(active=True)
	new_comment = None 
	comment_form = None 
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.coin = coin 
			new_comment.save()
		else:
			comment_form = CommentForm()
	return render(request, 'main/pages/detail.html', {'coin': coin, 'comments': comments,
		'comment_form': comment_form, 'new_comment': new_comment})