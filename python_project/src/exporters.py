import csv
from pathlib import Path


class CSVExporter:
    def export(self, data, filepath):
        data = list(data)

        if not data:
            return

        path = Path(filepath)

        # автоматически создаёт папки
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=data[0].keys()
            )

            writer.writeheader()
            writer.writerows(data)