import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



def qun_prod_cat():
    #wykres ilosci kupionych produktów w zależności od kategorii
    df_ord = pd.read_csv("../static/zamowienie.csv")
    df_cat = pd.read_csv("../static/kategoria.csv")
    df_prod = pd.read_csv("../static/produkt.csv")
    df_po = pd.read_csv("../static/produkty_zamowienia.csv")
    df_client = pd.read_csv("../static/klient.csv")
    df_seller = pd.read_csv("../static/sprzedawca.csv")

    sns.set()
    df_cat = df_cat.rename(columns={"Id_kategorii": "Id_kategorii", "Nazwa": "Nazwa_kategorii"})
    merged_prod_cat = pd.merge(df_cat, df_prod)
    merged_prod_cat = pd.merge(merged_prod_cat, df_po)
    category_vc = merged_prod_cat["Nazwa_kategorii"].value_counts()
    category_vc = category_vc.to_frame()
    sns.barplot(x=category_vc.index, y="Nazwa_kategorii", palette="ch:.25", data=category_vc)
    plt.ylabel("Ilość wystąpień")
    plt.xticks(
        rotation=65,
        horizontalalignment='right',
        fontweight='light',
        fontsize='10'
    )
    plt.savefig('../static/{}'.format("qun_prod_cat"))
qun_prod_cat()

def qun_prod_in_ord():
    #wykres ilości zamówioncyh produktów w jednym zamówieniu


    vc_df_ord_prd = df_po["Id_zamowienia"].value_counts()
    counted = pd.DataFrame(vc_df_ord_prd)
    counted.sort_index()
    counted_v = counted["Id_zamowienia"].value_counts()
    counted_v_df = pd.DataFrame(counted_v)
    counted_v_df = counted_v_df.sort_index()
    plt.title("Wykresy ilości przedmiotów w jednym zamówieniu")
    sns.barplot(x=counted_v_df.index, y="Id_zamowienia", palette="ch:.25", data=counted_v_df)
    plt.ylabel("Ilość zamówień")
    plt.xlabel("Ilość przedmiotów")
    plt.savefig('../static/{}'.format("qun_prod_in_ord"))

def qun_ord_of_client():
    #ilosc zamowien
    zamowienia_klienta = df_client.merge(df_cat, how='left', left_on='Id_klienta', right_on='Id_klienta')
    zamowienia_klienta = zamowienia_klienta["Id_klienta"].value_counts()
    zamowienia_klienta = pd.DataFrame(zamowienia_klienta)
    zamowienia_klienta = zamowienia_klienta['Id_klienta'].value_counts()
    zamowienia_klienta = pd.DataFrame(zamowienia_klienta)
    sns.barplot(x=zamowienia_klienta.index, y="Id_klienta", data=zamowienia_klienta)
    plt.xlabel("Ilość zamówień")
    plt.ylabel("Ilość klientów")
    plt.title("Ilość zamówień złożonych przez klienta")
    plt.savefig('../static/{}'.format("qun_ord_of_client"))