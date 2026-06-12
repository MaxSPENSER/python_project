import pytest

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from datasource import DataSource
from pipeline import DataCleaner
from exceptions import FileFormatError
from exceptions import InvalidDataError


def test_invalid_file_format():
    with pytest.raises(FileFormatError):
        DataSource("data.json")


def test_negative_price_skipped():
    """Отрицательные цены пропускаются с предупреждением"""
    data = [{"price": "-10", "quantity": "1"}]
    cleaner = DataCleaner(data)
    result = list(cleaner)
    assert result == []  # строка с отрицательной ценой пропущена


@pytest.mark.pipeline
def test_empty_data():
    cleaner = DataCleaner([])
    result = list(cleaner)
    assert result == []


@pytest.mark.pipeline
def test_invalid_value_skipped():
    data = [{"price": "abc", "quantity": "1"}]
    cleaner = DataCleaner(data)
    result = list(cleaner)
    assert result == []