from django.shortcuts import render
from PyDictionary import PyDictionary

def dictionary(request):
    if request.method == 'GET' and 'search' in request.GET:
        search = request.GET.get('search')
        dictionary = PyDictionary()
        meaning = dictionary.meaning(search)
        antonyms = dictionary.antonym(search)
        synonyms = dictionary.synonym(search)

        context = {
            'search': search,
            'meaning': meaning['Noun'][0] if meaning else None,
            'antonyms': antonyms,
            'synonyms': synonyms,
        }
        return render(request, 'dictionary.html', context)
    else:
        return render(request, 'dictionary.html')

