from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):

	return render(request, 'home.html')


def count(request):

	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	count_dict = {}

	for word in wordlist:

		if word in count_dict:

			count_dict[word] += 1

		else:
			
			count_dict[word] = 1


	sorted_words= sorted(count_dict.items(), key = lambda k:k[1], reverse = True)

	return render(request, 'count.html',{'fulltext':fulltext, 'count': len(wordlist), 'sorted_words' : sorted_words})


def about(request):

	return render(request, 'about.html')