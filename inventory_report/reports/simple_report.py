from datetime import datetime
from collections import Counter

class SimpleReport:
    @staticmethod
    def generate(list_of_products):

        fabricacao_mais_antiga = [item["data_de_fabricacao"] for item in list_of_products]

        validade_mais_proxima = [item["data_de_validade"] for item in list_of_products]

        empresa_mais_produtos = Counter([item["nome_da_empresa"] for item in list_of_products]).most_common(1)[0][0]


        return (
            f"Data de fabricação mais antiga: {min(fabricacao_mais_antiga)}\n"
            f"Data de validade mais próxima: {min(validade_mais_proxima)}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}"
        )