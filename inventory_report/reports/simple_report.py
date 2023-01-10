from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products):

        mais_antiga = [item["data_de_fabricacao"] for item in products]

        validade_proxima = [item["data_de_validade"] for item in products]

        empresa_mais_produtos = Counter(
            [item["nome_da_empresa"] for item in products]
            ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {min(mais_antiga)}\n"
            f"Data de validade mais próxima: {min(validade_proxima)}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}"
        )
