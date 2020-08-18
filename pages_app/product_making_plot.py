import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
"""
df_ord = pd.read_csv("static/zamowienie.csv")
df_cat = pd.read_csv("static/kategoria.csv")
df_prod = pd.read_csv("static/produkt.csv")
df_po = pd.read_csv("static/produkty_zamowienia.csv")
df_client = pd.read_csv("static/klient.csv")
df_seller = pd.read_csv("static/sprzedawca.csv")

"""
def qun_prod_cat():

    # wykres ilosci kupionych produktów w zależności od kategorii

    df_cat = pd.read_csv("static/kategoria.csv")
    df_prod = pd.read_csv("static/produkt.csv")
    df_po = pd.read_csv("static/produkty_zamowienia.csv")

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
    plt.savefig('static/{}'.format("qun_prod_cat"))
    plt.clf()

def qun_prod_in_ord():

    # wykres ilości zamówioncyh produktów w jednym zamówieniu

    df_po = pd.read_csv("static/produkty_zamowienia.csv")

    sns.set()
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
    plt.savefig('static/{}'.format("qun_prod_in_ord"))
    plt.clf()

def qun_ord_of_client():

    #ilosc zamowien klienta

    df_client = pd.read_csv("static/klient.csv")
    df_ord = pd.read_csv("static/zamowienie.csv")

    sns.set()
    ord_client = df_client.merge(df_ord, how='left', left_on='Id_klienta', right_on='Id_klienta')
    ord_client = ord_client["Id_klienta"].value_counts()
    ord_client = pd.DataFrame(ord_client)
    ord_client = ord_client['Id_klienta'].value_counts()
    ord_client = pd.DataFrame(ord_client)
    sns.barplot(x=ord_client.index, y="Id_klienta", data=ord_client)
    plt.xlabel("Ilość zamówień")
    plt.ylabel("Ilość klientów")
    plt.title("Ilość zamówień złożonych przez klienta")
    plt.savefig('static/{}'.format("qun_ord_of_client"))
    plt.clf()

def qun_ord_sel():

    #ilość zamówień obsłużonych przez sprzedawce

    df_ord = pd.read_csv("static/zamowienie.csv")
    df_seller = pd.read_csv("static/sprzedawca.csv")

    sns.set()
    df_ord_sel = pd.merge(df_seller, df_ord)
    df_ord_sel = df_ord_sel['Id_sprzedawcy'].value_counts()
    df_ord_sel = pd.DataFrame(df_ord_sel)
    df_ord_sel = df_ord_sel.reset_index()
    df_ord_sel = df_ord_sel.rename(columns={"index": "Id_sprzedawcy", "Id_sprzedawcy": "Ilosc_zam"})
    df_ord_sel = pd.merge(df_ord_sel, df_seller)
    plt.title("Ilość zamówień obsłużonych przez sprzedawce")
    sns.barplot(x="Imie", y="Ilosc_zam", data=df_ord_sel)
    plt.yticks([5, 10, 15, 20])
    plt.xlabel("Sprzedawca")
    plt.ylabel("Ilość zamówień")
    plt.savefig('static/{}'.format("qun_ord_of_sel"))
    plt.clf()

def income_cat():

    # przychód ze sprzedaży ze wzlęgu na kategorię

    df_cat = pd.read_csv("static/kategoria.csv")
    df_prod = pd.read_csv("static/produkt.csv")
    df_ord_prod = pd.read_csv("static/produkty_zamowienia.csv")

    sns.set()
    df_merged = pd.merge(df_prod, df_ord_prod)
    df_profit = pd.DataFrame(columns=["Przychod"])
    df_merged1 = df_merged[df_merged.Id_kategorii == 1]
    df_merged2 = df_merged[df_merged.Id_kategorii == 2]
    df_merged3 = df_merged[df_merged.Id_kategorii == 3]
    df_merged4 = df_merged[df_merged.Id_kategorii == 4]
    df_merged5 = df_merged[df_merged.Id_kategorii == 5]
    df_merged6 = df_merged[df_merged.Id_kategorii == 6]
    df_merged7 = df_merged[df_merged.Id_kategorii == 7]
    df_merged8 = df_merged[df_merged.Id_kategorii == 8]
    df_merged9 = df_merged[df_merged.Id_kategorii == 9]
    df_merged10 = df_merged[df_merged.Id_kategorii == 10]
    df_merged11 = df_merged[df_merged.Id_kategorii == 11]
    df_merged12 = df_merged[df_merged.Id_kategorii == 12]
    df_merged13 = df_merged[df_merged.Id_kategorii == 13]
    df_merged14 = df_merged[df_merged.Id_kategorii == 14]
    sum1 = df_merged1.Cena.sum()
    sum2 = df_merged2.Cena.sum()
    sum3 = df_merged3.Cena.sum()
    sum4 = df_merged4.Cena.sum()
    sum5 = df_merged5.Cena.sum()
    sum6 = df_merged6.Cena.sum()
    sum7 = df_merged7.Cena.sum()
    sum8 = df_merged8.Cena.sum()
    sum9 = df_merged9.Cena.sum()
    sum10 = df_merged10.Cena.sum()
    sum11 = df_merged11.Cena.sum()
    sum12 = df_merged12.Cena.sum()
    sum13 = df_merged13.Cena.sum()
    sum14 = df_merged14.Cena.sum()
    df_profit.index = df_profit.index + 1
    df_profit.loc[1] = sum1
    df_profit.loc[2] = sum2
    df_profit.loc[3] = sum3
    df_profit.loc[4] = sum4
    df_profit.loc[5] = sum5
    df_profit.loc[6] = sum6
    df_profit.loc[7] = sum7
    df_profit.loc[8] = sum8
    df_profit.loc[9] = sum9
    df_profit.loc[10] = sum10
    df_profit.loc[11] = sum11
    df_profit.loc[12] = sum12
    df_profit.loc[13] = sum13
    df_profit.loc[14] = sum14
    df_profit = pd.merge(df_profit, df_cat, left_on=df_profit.index, right_on="Id_kategorii")
    plt.title("Przychód ze względu na kategorię")
    sns.barplot(x="Nazwa", y="Przychod", data=df_profit)
    plt.xlabel("Nazwa kategorii")
    plt.ylabel("Przychód")
    plt.savefig('static/{}'.format("income_cat"))
    plt.clf()