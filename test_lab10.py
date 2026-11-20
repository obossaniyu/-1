
import pytest
from lab10 import Inventory


def test_add():
    inv = Inventory()
    inv.add("Молоко", 100, 5)
    assert "Молоко" in inv.products


def test_get():
    inv = Inventory()
    inv.add("Молоко", 100, 5)
    assert inv.get("Молоко")["price"] == 100


def test_update():
    inv = Inventory()
    inv.add("Молоко", 100, 5)
    inv.update("Молоко", 120, 10)
    assert inv.get("Молоко")["price"] == 120
    assert inv.get("Молоко")["quantity"] == 10


def test_delete():
    inv = Inventory()
    inv.add("Молоко", 100, 5)
    inv.delete("Молоко")
    assert "Молоко" not in inv.products


def test_duplicate():
    inv = Inventory()
    inv.add("Молоко", 100, 5)

    with pytest.raises(ValueError):
        inv.add("Молоко", 100, 5)


def test_negative_price():
    inv = Inventory()

    with pytest.raises(ValueError):
        inv.add("Молоко", -100, 5)


def test_negative_quantity():
    inv = Inventory()

    with pytest.raises(ValueError):
        inv.add("Молоко", 100, -5)


def test_empty_name():
    inv = Inventory()

    with pytest.raises(ValueError):
        inv.add("", 100, 5)


def test_report_count():
    inv = Inventory()
    inv.add("Молоко", 100, 5)
    inv.add("Хлеб", 50, 10)
    assert inv.report()[0] == 2


def test_report_quantity():
    inv = Inventory()
    inv.add("Молоко", 100, 5)
    inv.add("Хлеб", 50, 10)
    assert inv.report()[1] == 15


def test_report_cost():
    inv = Inventory()
    inv.add("Молоко", 100, 5)
    inv.add("Хлеб", 50, 10)
    assert inv.report()[2] == 1000


def test_empty_report():
    inv = Inventory()
    assert inv.report() == (0, 0, 0)


def test_save_load(tmp_path):
    filename = tmp_path / "products.json"

    inv = Inventory()
    inv.add("Молоко", 100, 5)
    inv.save(filename)

    new_inv = Inventory()
    new_inv.load(filename)

    assert new_inv.products == inv.products


def test_missing_file(tmp_path):
    inv = Inventory()
    inv.load(tmp_path / "missing.json")
    assert inv.products == {}


def test_delete_missing():
    inv = Inventory()

    with pytest.raises(KeyError):
        inv.delete("Молоко")
