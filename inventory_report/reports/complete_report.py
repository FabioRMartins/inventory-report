from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(file):

        report = SimpleReport.generate(file)

        empresa = [item["nome_da_empresa"] for item in file]
        contagem_estoque = Counter(empresa)

        report += "\nProdutos estocados por empresa:\n"
        for nome_empresa, quantidade in contagem_estoque.items():
            report += f"- {nome_empresa}: {quantidade}\n"
        return report
