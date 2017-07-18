from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return  render(request, 'store_app/index.html')

def checkout(request):
    session = request.session
    session['order_counter'] = session.get('order_counter',0)
    session['charged_with'] = session.get('charged_with',0)
    session['order_total'] = session.get('order_total', 0)
    context = {
        'charged_with' : session['charged_with'],
        'order_counter' : session['order_counter'],
        'order_total'   : session['order_total']
    }
    return render(request, 'store_app/checkout.html', context)

def process(request):
    price_list = {
        '1' :   {'product_name':'Dojo Shirt', 'product_prize':19.99},
        '2' :   {'product_name':'Dojo Sweater', 'product_prize':29.99},
        '3' :   {'product_name':'Dojo Cup', 'product_prize':4.99},
        '4' :   {'product_name':'Algorithm Book', 'product_prize':49.99},
    }

    session = request.session
    
    if request.method == 'POST':
        session['order_counter'] = session.get('order_counter',0)
        session['charged_with'] = session.get('charged_with',0)
        session['order_total'] = session.get('order_total', 0)

        session['charged_with'] = price_list[request.POST['product_id']]['product_prize'] * int(request.POST['quantity'])
        session['order_counter'] += int(request.POST['quantity'])
        session['order_total'] += session['charged_with']

    return redirect('/checkout')

def clear_result(request):
    request.session.clear()
    return redirect('/checkout')