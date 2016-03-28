from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import StockIndex, Equity


def index(request):
    stockindexes = StockIndex.objects.all()
    context = {'stockindex_list': stockindexes}
    return render(request, 'stockindex/index.html', context)


def addindex(request):
    s = StockIndex(symbol=request.POST['symbol'],name=request.POST['name'])
    s.save()
    return render(request, 'stockindex/index.html', {'stockindex_list': StockIndex.objects.all()})


def deleteindex(request):
    stockindex = get_object_or_404(StockIndex, pk=request.POST['stockindex'])
    stockindex.delete()
    return render(request, 'stockindex/index.html', {'stockindex_list': StockIndex.objects.all()})


def details(request, stockindex_id):
    stockindex = get_object_or_404(StockIndex, pk=stockindex_id)
    return render(request, 'stockindex/detail.html', {'stockindex': stockindex}) 


def add(request, stockindex_id):
    stockindex = get_object_or_404(StockIndex, pk=stockindex_id)
    try:
        equity = stockindex.equity_set.get(symbol=request.POST['symbol'])
    except (KeyError, Equity.DoesNotExist):
        equity = stockindex.equity_set.create(symbol=request.POST['symbol'],price=request.POST['price'],number=request.POST['number'])
        return HttpResponseRedirect(reverse('stockindex:detail', args=(stockindex.id,)))
    else:
        equity.price = request.POST['price']
        equity.number = request.POST['number']
        equity.save()
        return HttpResponseRedirect(reverse('stockindex:detail', args=(stockindex.id,)))


def modify(request, stockindex_id):
    stockindex = get_object_or_404(StockIndex, pk=stockindex_id)
    try:
        equity = stockindex.equity_set.get(pk=request.POST['equity'])
    except (KeyError, Equity.DoesNotExist):
        # Redisplay the stock index
        return render(request, 'stockindex/detail.html', {
            'stockindex': stockindex,
            'error_message': "You have to select equity from the index!",
        })
    else:
        if 'update' in request.POST:
            return render(request, 'stockindex/detail.html', {'stockindex': stockindex, 'stock': equity})
        elif 'delete' in request.POST:
            equity.delete()
            return render(request, 'stockindex/detail.html', {'stockindex': stockindex})


