import pandas as pd

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from analytics import PandasAnalytics


def test_dataframe_creation(tmp_path):
    file = tmp_path / "test.csv"

    df = pd.DataFrame({
        "price": [10, 20],
        "quantity": [1, 2]
    })

    df.to_csv(file, index=False)

    analytics = PandasAnalytics(file)

    result = analytics.process()

    assert "total" in result.columns



def test_total_calculation(tmp_path):
    file = tmp_path / "test.csv"

    df = pd.DataFrame({
        "price": [10],
        "quantity": [3]
    })

    df.to_csv(file, index=False)

    analytics = PandasAnalytics(file)

    result = analytics.process()

    assert result.iloc[0]["total"] == 30