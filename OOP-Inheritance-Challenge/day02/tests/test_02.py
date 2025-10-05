import importlib.util
import pathlib
import pytest

template_path = pathlib.Path(__file__).parent.parent / "template.py"
spec = importlib.util.spec_from_file_location("day02_template", str(template_path))
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)


def test_classes_and_inheritance():
    assert hasattr(t, "Kendaraan"), "Kendaraan class missing"
    assert hasattr(t, "Mobil"), "Mobil class missing"
    assert hasattr(t, "Motor"), "Motor class missing"

    Kendaraan = t.Kendaraan
    Mobil = t.Mobil
    Motor = t.Motor

    # create instances if possible
    try:
        m1 = Mobil()
    except Exception:
        m1 = object.__new__(Mobil)

    try:
        m2 = Motor()
    except Exception:
        m2 = object.__new__(Motor)

    assert isinstance(m1, Kendaraan), "Mobil should inherit from Kendaraan"
    assert isinstance(m2, Kendaraan), "Motor should inherit from Kendaraan"


def test_berjalan_outputs(capsys):
    Mobil = t.Mobil
    Motor = t.Motor

    # Try creating with common constructor shapes or set attributes manually
    try:
        car = Mobil("Toyota", 180)
    except TypeError:
        try:
            car = Mobil(merk="Toyota", kecepatan_maksimal=180)
        except TypeError:
            car = object.__new__(Mobil)
            car.merk = "Toyota"
            car.kecepatan_maksimal = 180

    try:
        bike = Motor("Yamaha", 120)
    except TypeError:
        try:
            bike = Motor(merk="Yamaha", kecepatan_maksimal=120)
        except TypeError:
            bike = object.__new__(Motor)
            bike.merk = "Yamaha"
            bike.kecepatan_maksimal = 120

    assert hasattr(car, "berjalan") and callable(getattr(car, "berjalan")), "Mobil should implement berjalan()"
    assert hasattr(bike, "berjalan") and callable(getattr(bike, "berjalan")), "Motor should implement berjalan()"

    # Call and capture
    try:
        car.berjalan()
    except TypeError:
        pass
    try:
        bike.berjalan()
    except TypeError:
        pass

    captured = capsys.readouterr()
    out = captured.out

    assert "Toyota" in out or "mobil" in out.lower()
    assert "Yamaha" in out or "motor" in out.lower()
