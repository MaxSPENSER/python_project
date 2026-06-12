from pathlib import Path

from datasource import DataSource
from pipeline import DataCleaner, FilterIterator
from exporters import CSVExporter
from analytics import PandasAnalytics
from strategies import PriceFilterStrategy
from exceptions import InvalidDataError, FileFormatError


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw" / "ecommerce_logs.csv"
FILTERED_DATA = BASE_DIR / "data" / "processed" / "filtered.csv"
CLEANED_DATA = BASE_DIR / "data" / "processed" / "cleaned_data.csv"


def run_pipeline():
    try:
        source = DataSource(str(RAW_DATA))

        cleaned = DataCleaner(source)

        strategy = PriceFilterStrategy(100)

        filtered = FilterIterator(cleaned, strategy)

        exporter = CSVExporter()
        exporter.export(filtered, str(FILTERED_DATA))

        analytics = PandasAnalytics(str(RAW_DATA))
        analytics.process()
        analytics.save(str(CLEANED_DATA))

        print("Проект успешно выполнен")

    except FileFormatError as e:
        print(f"Ошибка файла: {e}")

    except InvalidDataError as e:
        print(f"Ошибка данных: {e}")

    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")


if __name__ == "__main__":
    run_pipeline()