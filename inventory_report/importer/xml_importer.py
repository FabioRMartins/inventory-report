import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            with open(path) as file:
                reader = xmltodict.parse(file.read())["dataset"]["record"]
                return list(reader)
