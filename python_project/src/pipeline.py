from exceptions import InvalidDataError


class DataCleaner:
    """Ленивая очистка данных."""

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        for row in self.iterable:
            try:
                # Проверка пустых значений (используем .get() для безопасности)
                if not row.get("product") or not row.get("price") or not row.get("quantity"):
                    print(f"[WARNING] Пустые значения пропущены: {row}")
                    continue

                row["price"] = float(row["price"])
                row["quantity"] = int(row["quantity"])

                # Проверка отрицательной цены
                if row["price"] < 0:
                    print(f"[WARNING] Отрицательная цена пропущена: {row}")
                    continue

                yield row

            except ValueError as e:
                print(f"[WARNING] Некорректная строка пропущена: {row}, ошибка: {e}")
                continue
            except KeyError as e:
                print(f"[WARNING] Отсутствует обязательное поле: {e} в строке {row}")
                continue


class FilterIterator:
    """Ленивый фильтр."""

    def __init__(self, iterable, strategy):
        self.iterable = iterable
        self.strategy = strategy

    def __iter__(self):
        for row in self.iterable:
            if self.strategy.apply(row):
                yield row