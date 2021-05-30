from django.shortcuts import render


# Create your views here.
#dummy post data
posts = [
		{
			'author': 'Abhishek KS',
			'title': 'Blog Post 1',
			'content': 'First blog post',
			'date_posted': 'May 29, 2020'

		},
		{
			'author': 'Abhishek KS',
			'title': 'Blog Post 2',
			'content': 'Second blog post',
			'date_posted': 'May 30, 2020'
		}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})