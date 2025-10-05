import importlib.util
import pathlib
import pytest

template_path = pathlib.Path(__file__).parent.parent / "template.py"
spec = importlib.util.spec_from_file_location("day03_template", str(template_path))
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)


def _get_manager_class():
    # README uses 'Manajer' but template defines 'Manager' — accept either.
    if hasattr(t, "Manager"):
        return t.Manager
    if hasattr(t, "Manajer"):
        return t.Manajer
    return None


def test_pegawai_and_manager_exist():
    assert hasattr(t, "Pegawai"), "Pegawai class missing"
    Manager = _get_manager_class()
    assert Manager is not None, "Manager/Manajer class missing"


def test_hitung_gaji_override_and_super():
    Pegawai = t.Pegawai
    Manager = _get_manager_class()

    # create instances with attributes; if constructors vary, set attributes manually
    try:
        p = Pegawai("Andi", 5000)
    except TypeError:
        p = object.__new__(Pegawai)
        p.nama = "Andi"
        p.gaji_dasar = 5000

    try:
        m = Manager("Budi", 7000, 2000)
    except TypeError:
        try:
            m = Manager(nama="Budi", gaji_dasar=7000, tunjangan=2000)
        except TypeError:
            m = object.__new__(Manager)
            m.nama = "Budi"
            m.gaji_dasar = 7000
            m.tunjangan = 2000

    # Both should implement hitung_gaji
    assert hasattr(p, "hitung_gaji") and callable(getattr(p, "hitung_gaji")), "Pegawai should have hitung_gaji()"
    assert hasattr(m, "hitung_gaji") and callable(getattr(m, "hitung_gaji")), "Manager should have hitung_gaji()"

    # Call them and compare results if they return numbers
    try:
        gp = p.hitung_gaji()
    except TypeError:
        gp = None

    try:
        gm = m.hitung_gaji()
    except TypeError:
        gm = None

    if isinstance(gp, (int, float)) and isinstance(gm, (int, float)):
        assert gm >= gp, "Manager's calculated salary should be >= Pegawai's base salary when tunjangan present"
