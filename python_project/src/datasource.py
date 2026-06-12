import csv
from exceptions import FileFormatError


class DataSource:
    """Источник данных."""

    def __init__(self, filepath):
        if not filepath.endswith(".csv"):
            raise FileFormatError("Поддерживаются только CSV файлы")

        self.filepath = filepath

    def __iter__(self):
        with open(self.filepath, encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                yield row