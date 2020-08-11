from django.shortcuts import render
import pandas as pd
import seaborn as sns
import numpy as np
from django.views.generic import TemplateView
import os
import matplotlib.pylab as plb

"""
from plots_graphs.models import Klient
from plots_graphs.models import Produkty_Zamowienia
"""
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import django.http
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from plots_graphs.product_making_plot import making_plot

import PIL, PIL.Image, io
from django.http import HttpResponse
# Create your views here.

def product_plot_make_view():
    making_plot()









"""
def showimage(request):
    # Construct the graph
    t = np.arangearange(0.0, 2.0, 0.01)
    s = np.sin(2 * np.pi * t)
    plt.plot(t, s, linewidth=1.0)

    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)

    # Store image in a string buffer
    buffer = io.StringIO()
    canvas = plb.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    plb.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")


to działa ale nie wyskakuje obrazek
def show(request):

    x = np.arange(10)
    y = x
    fig = plt.figure()
    plt.plot(x, y)
    canvas = fig.canvas
    buf, size = canvas.print_to_buffer()
    image = PIL.Image.frombuffer('RGBA', size, buf, 'raw', 'RGBA', 0, 1)
    buffer=io.BytesIO()
    image.save(buffer,'PNG')
    graphic = buffer.getvalue()
    graphic = base64.b64encode(graphic)
    buffer.close()
    return render(request, 'graphic.html', {'graphic': graphic})


to działa ale generuje templatke
class Products(TemplateView):
    def getSNSData(request):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'I:/Aplikacja_Licencjat/static/produkt.csv')
        df = pd.read_csv(file_path)
        gr = sns.barplot(x = "Id_produktu", y ="Cena", data = df)
        response = HttpResponse(content_type="image/jpeg")
        gr.figure.savefig(response, format="png")
        return response


def product_plot_view():
    df = pd.read_csv("../static/zamowienie.csv")
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plt=("Id_produktu", "Cena")
    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    print(df)
    return response



def product_plot_view(request,*args,**kwargs):
    df = pd.read_csv("datas/zamowienie.csv")
    fig = Figure()
    canvas = FigureCanvas
    ax = fig.add_subplot(111)
    x = df.columns[0]
    y = df.columns[3]
    ax.plot(x,y)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


def product_plot_view(request,*args,**kwargs):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    x = Produkt.id_produktu
    y = Produkt.cena
    ax.plot(x, y)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def product_plot_view(request,*args,**kwargs):
    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.add_subplot(111)
    x = np.arange(-2,1.5,.01)
    y = np.sin(np.exp(2*x))
    ax.plot(x, y)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def klient_plot_view(request):
    sns.set()
    df_klient = pd.read_csv('/static/klient.csv', sep=';')
    clients = []
    for i in range(len(df_klient)):
        clients.append(
            Klient(
                id_klienta=df_klient.iloc[i][0]


        )
        )
        sns.barplot(x="Nazwa", y="Cena", data=df_product)


def produkty_zamowienia_plot_view(request):
    sns.set()
    df_p_z = pd.read_csv('/static/produkty_zamowienia.csv', sep=';')
    products_orders = []
    for i in range(len(df_p_z)):
        products_orders.append(
            Produkty_Zamowienia(
                id_zamowienia=df_p_z.iloc[i][0],
                id_

            )
        )
        sns.barplot(x="Nazwa", y="Cena", data=df_p_z)
"""