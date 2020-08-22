from django.shortcuts import render
from django.http import HttpResponse
from .making_plot import qun_prod_cat
from .making_plot import qun_prod_in_ord
from .making_plot import qun_ord_of_client
from .making_plot import qun_ord_sel
from .making_plot import income_cat
from .making_plot import income_month

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request,"home.html", {})

def plots_page_view(request, *args, **kwargs):

    return render(request, "plots_page.html", {})


def plots(request, id):
    # oddaj w argumencie nazwe pliku

    nazwa=""
    id = int(id)
    if id == 1:
        qun_prod_cat()
        nazwa="qun_prod_cat.png"
    elif id == 2:
        qun_prod_in_ord()
        nazwa = "qun_prod_in_ord.png"
    elif id == 3:
        qun_ord_of_client()
        nazwa = "qun_ord_of_client.png"
    elif id == 4:
        qun_ord_sel()
        nazwa = "qun_ord_of_sel.png"
    elif id == 5:
        income_cat()
        nazwa = "income_cat.png"
    elif id == 6:
        income_month()
        nazwa = "income_month.png"

    args={
        "nazwa": nazwa
    }

    return render(request, "plots_page.html", args)


