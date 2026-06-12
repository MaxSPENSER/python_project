import pandas as pd
from decorators import log_execution

class PandasAnalytics:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)

    @log_execution
    def process(self):
        # 1. Удаление дубликатов
        self.df.drop_duplicates(inplace=True)

        # 2. Удаление пустых значений
        self.df.dropna(inplace=True)

        # 3. Преобразование типов
        self.df["price"] = self.df["price"].astype(float)
        self.df["quantity"] = self.df["quantity"].astype(int)

        # 4. Создание новой колонки
        self.df["total"] = self.df["price"] * self.df["quantity"]

        # 5. Фильтрация
        self.df = self.df[self.df["price"] > 0]

        return self.df

    def save(self, output_path):
        self.df.to_csv(output_path, index=False)