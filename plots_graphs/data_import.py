"""import pandas as pd
from plots_graphs.models import Produkt
def product_data_import():
    df_product = pd.read_csv('plots_graphs/datas/produkt.csv', sep=',')
    products = []
    for i in range(len(df_product)):
        products.append(
            Produkt(
                id_produktu=df_product.iloc[i][0],
                nazwa=df_product.iloc[i][1],
                id_kategorii=df_product.iloc[i][2],
                cena=df_product.iloc[i][3]
            )
        )
    Produkt.objects.bulk_create(products)
    return products
"""