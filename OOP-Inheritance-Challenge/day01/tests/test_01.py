import importlib.util
import pathlib
import pytest

# Load the template module by file path so imports don't break due to hyphens in the
# repository/folder name.
template_path = pathlib.Path(__file__).parent.parent / "template.py"
spec = importlib.util.spec_from_file_location("day01_template", str(template_path))
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)


def test_classes_exist_and_inheritance():
    # Binatang should be a class and Mamalia should inherit from it
    assert hasattr(t, "Binatang"), "Binatang class is missing"
    assert hasattr(t, "Mamalia"), "Mamalia class is missing"

    Binatang = t.Binatang
    Mamalia = t.Mamalia

    # instantiate to ensure constructors exist (may raise if required args missing)
    try:
        b = Binatang()
    except Exception:
        # it's fine if constructor requires args; presence is the main check
        b = None

    try:
        m = Mamalia()
    except Exception:
        # If Mamalia requires args, try to create a dummy instance via object.__new__
        m = object.__new__(Mamalia)

    assert isinstance(m, Binatang), "Mamalia should inherit from Binatang"


def test_attributes_and_deskripsikan_output(capsys):
    Mamalia = t.Mamalia

    # Try common constructor shapes; if they fail, set attributes manually
    try:
        m = Mamalia("Kucing", 2, True)
    except TypeError:
        try:
            m = Mamalia(nama="Kucing", umur=2, peliharaan=True)
        except TypeError:
            # fallback: create instance without calling __init__ and set attributes
            m = object.__new__(Mamalia)
            m.nama = "Kucing"
            m.umur = 2
            m.peliharaan = True

    # Attributes
    assert hasattr(m, "nama"), "Mamalia should have attribute 'nama'"
    assert hasattr(m, "umur"), "Mamalia should have attribute 'umur'"
    assert hasattr(m, "peliharaan"), "Mamalia should have attribute 'peliharaan'"

    # deskripsikan method should exist
    assert hasattr(m, "deskripsikan") and callable(getattr(m, "deskripsikan")), \
        "Mamalia should implement method 'deskripsikan()'"

    # Capture printed output (method is expected to print)
    try:
        m.deskripsikan()
    except TypeError:
        # If deskripsikan requires args, call with none; the presence check above is the key
        pass

    captured = capsys.readouterr()
    out = captured.out.strip()

    # Expected format from README: "Nama: Kucing, Umur: 2 tahun, Mamalia peliharaan: Ya"
    assert "Nama:" in out
    assert "Kucing" in out
    assert "Umur" in out
    assert "2" in out
    assert "Mamalia" in out
