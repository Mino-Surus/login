from django.shortcuts import render, HttpResponse

def show_number(request):

    number = request.session.get('number')
    return render(request, 'main.html',
                {
                    'number': number
                }
                )
    request.session['number'] = 42
    


def set_number(request, number):
    response = HttpResponse()
    response.set_cookie('number', number)
    return response