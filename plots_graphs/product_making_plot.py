import matplotlib.pyplot as plt
import pandas as pd
def product_making_plot():
    fig = plt.figure(dpi=128, figsize=(10, 6))
    df = pd.read_csv('../static/produkt.csv')
    df.plot(x='Id_produktu', y="Cena", kind='scatter')
    print(df)
    plt.savefig('../static/{}'.format("cena_id_produktu"))

product_making_plot()