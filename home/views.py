from django.shortcuts import render
import wikipediaapi
# Create your views here.
def home(request):
    if request.method == 'GET':
        try:
            search=request.GET.get('search')
            wiki_wiki = wikipediaapi.Wikipedia('en')
            page_py = wiki_wiki.page(search)
            wiki_wiki = wikipediaapi.Wikipedia('en')
            data={'title':page_py.title,'info':page_py.summary[0:10000]}
        except Exception as e:
            data={'title':'','info':''}
            
    return render(request, 'index.html',data) 