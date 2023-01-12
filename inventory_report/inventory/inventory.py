from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        if path.endswith(".csv"):
            reader = CsvImporter.import_data(path)
        elif path.endswith(".json"):
            reader = JsonImporter.import_data(path)
        elif path.endswith(".xml"):
            reader = XmlImporter.import_data(path)
        if type == "simples":
            return SimpleReport.generate(reader)
        else:
            type == "completo"
            return CompleteReport.generate(reader)
