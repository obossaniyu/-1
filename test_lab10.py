
import pytest
from lab10 import Schedule


def test_add():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    assert "Математика" in s.lessons


def test_get():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    assert s.get("Математика")["room"] == "101"


def test_update():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    s.update("Математика", "Пятница", "11:00", "12:00", "102")
    assert s.get("Математика")["room"] == "102"


def test_delete():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    s.delete("Математика")
    assert not s.lessons


def test_duplicate():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    with pytest.raises(ValueError):
        s.add("Математика", "Пятница", "11:00", "12:00", "102")


def test_room_conflict():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    with pytest.raises(ValueError, match="Аудитория уже занята"):
        s.add("Физика", "Среда", "09:30", "10:30", "101")


def test_time_conflict():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    with pytest.raises(ValueError, match="Конфликт времени"):
        s.add("Физика", "Среда", "09:30", "10:30", "102")


def test_different_days():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    s.add("Физика", "Пятница", "09:00", "10:00", "101")
    assert len(s.lessons) == 2


def test_no_overlap():
    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    s.add("Физика", "Среда", "10:00", "11:00", "101")
    assert len(s.lessons) == 2


def test_invalid_time():
    s = Schedule()
    with pytest.raises(ValueError):
        s.add("Физика", "Среда", "12:00", "09:00", "101")


def test_invalid_day():
    s = Schedule()
    with pytest.raises(ValueError):
        s.add("Физика", "Ошибка", "09:00", "10:00", "101")


def test_empty_name():
    s = Schedule()
    with pytest.raises(ValueError):
        s.add("", "Среда", "09:00", "10:00", "101")


def test_delete_missing():
    s = Schedule()
    with pytest.raises(KeyError):
        s.delete("Физика")


def test_save_load(tmp_path):
    filename = tmp_path / "schedule.json"

    s = Schedule()
    s.add("Математика", "Среда", "09:00", "10:00", "101")
    s.save(filename)

    other = Schedule()
    other.load(filename)

    assert other.lessons == s.lessons


def test_missing_file(tmp_path):
    s = Schedule()
    s.load(tmp_path / "missing.json")
    assert s.lessons == {}
