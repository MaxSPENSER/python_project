import pytest

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from pipeline import DataCleaner
from pipeline import FilterIterator
from strategies import PriceFilterStrategy


@pytest.fixture
def sample_data():
    return [
        {"product": "Keyboard", "price": "100", "quantity": "2"},
        {"product": "Mouse", "price": "50", "quantity": "1"},
    ]


@pytest.mark.pipeline

def test_cleaner(sample_data):
    cleaner = DataCleaner(sample_data)

    result = list(cleaner)

    assert result[0]["price"] == 100.0


@pytest.mark.parametrize(
    "price, expected",
    [
        (100, True),
        (50, False),
    ]
)

def test_filter_strategy(price, expected):
    strategy = PriceFilterStrategy(100)

    row = {"price": price}

    assert strategy.apply(row) == expected


@pytest.mark.pipeline

def test_filter_iterator(sample_data):
    cleaner = DataCleaner(sample_data)

    strategy = PriceFilterStrategy(80)

    filtered = FilterIterator(cleaner, strategy)

    result = list(filtered)

    assert len(result) == 1