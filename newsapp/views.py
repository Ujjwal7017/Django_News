from django.shortcuts import render
import requests
from django.core.paginator import Paginator
from django.http import JsonResponse

def index(request):
    try:
        search_query = request.GET.get('q')
        if search_query:
            # If search query is provided, filter news articles accordingly
            r = requests.get(f'https://newsapi.org/v2/everything?q={search_query}&apiKey=49d28b7457e94c7480ea1afe7acc0f59')
        else:
            # If no search query is provided, fetch top headlines
            r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=49d28b7457e94c7480ea1afe7acc0f59')

        res = r.json()
        if 'articles' in res:
            data = res['articles']

            # Pagination
            paginator = Paginator(data, 9)  # Show 9 articles per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'newsapp/index.html', {'news': page_obj, 'search_query': search_query})
        else:
            return render(request, 'newsapp/index.html', {'error': 'API response structure has changed. Please update the code to handle the new format.'})
    except requests.exceptions.RequestException as e:
        return render(request, 'newsapp/index.html', {'error': f'An error occurred: {e}'})

def categories(request):
  # You can optionally define a list of categories here (e.g., categories = ["Business", "Sports", "Technology"])
  return render(request, 'newsapp/categories.html')

# views.py

def get_headlines(request, category):
    api_key = '49d28b7457e94c7480ea1afe7acc0f59'
    language = 'en'  # Specify English language
    url = f'https://newsapi.org/v2/top-headlines?category={category}&language={language}&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    return JsonResponse(data)

def about(request):
    return render(request, 'newsapp/about.html')

def feedback(request):
    return render(request, 'newsapp/feedback.html')




