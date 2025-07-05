from django.shortcuts import render

from currency.utils import get_currency_data


def currency_view(request):
    data = get_currency_data()
    context = {
        "data": data
    }

    return render(request, 'currency.html', context)

