from django.shortcuts import render
from django.http import HttpResponse
from .transformer import process_data
from .passwordgen import passwordAlgorithm
from .passwordgen import passphraseAlgorithm
from django.shortcuts import redirect


def gen_view(request):
    if request.method == 'POST' and request.POST.get('passphrases') == "True":
        return render(request, 'generator/passphrase.html')
        """ return render(request, 'generator/result.html', {'password': password})
        password = passphraseAlgorithm() """
    elif request.method == 'POST' and (request.POST.get('none') == "True" or request.POST.get('specialChars') == "True" or request.POST.get('numbers') == "True" or request.POST.get('spaces') == "True" or request.POST.get('uppercase') == "True"):
        """ options = []
        for i, value in enumerate(request.POST):
            if i != 1 and value != "none":
                options.append(value)
            elif value == "none":
                try:
                    options[0] = "none"
                except:
                    options.append("none")
                break """
        
        password = passphraseAlgorithm(request)
        print(password)
        return render(request, 'generator/result.html', {'password': password})
    elif request.method == 'POST':
        prompt = request.POST.get('prompt')
        result = process_data(prompt)
        print(result)
        password = passwordAlgorithm(int(result[0]), int(result[1]), prompt)
        print(password)
        #redirect_view(request, password)
        return render(request, 'generator/result.html', {'password': 'testish'})

    return render(request, 'generator/generator.html')

