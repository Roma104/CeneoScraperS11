from itertools import product
import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
produkt = input("Podaj identyfikator produktu:")

opinions = pd.read_json(f"opinions/{produkt}.json")
print(opinions)