import importlib.util
import pathlib
import pytest

# Load the template module by file path so tests work regardless of workspace name
template_path = pathlib.Path(__file__).parent.parent / "template.py"
spec = importlib.util.spec_from_file_location("day04_template", str(template_path))
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)


def test_classes_and_inheritance():
    assert hasattr(t, "LivingBeing"), "LivingBeing class is missing"
    assert hasattr(t, "Animal"), "Animal class is missing"
    assert hasattr(t, "Bird"), "Bird class is missing"

    LivingBeing = t.LivingBeing
    Animal = t.Animal
    Bird = t.Bird

    # Try to create a Bird instance; if constructor needs args, create without __init__
    try:
        b = Bird()
    except Exception:
        b = object.__new__(Bird)

    assert isinstance(b, Animal), "Bird should inherit from Animal"
    assert isinstance(b, LivingBeing), "Bird should inherit (transitively) from LivingBeing"


def test_methods_exist_and_outputs(capsys):
    Bird = t.Bird

    try:
        b = Bird()
    except Exception:
        b = object.__new__(Bird)

    # Methods expected by the README
    for method in ("breathe", "move", "fly"):
        assert hasattr(b, method) and callable(getattr(b, method)), f"Bird should implement {method}()"

    # Call them (if they accept no args). If they require args, we ignore the TypeError
    try:
        b.breathe()
    except TypeError:
        pass
    try:
        b.move()
    except TypeError:
        pass
    try:
        b.fly()
    except TypeError:
        pass

    captured = capsys.readouterr()
    out = captured.out.lower()

    # Accept either English or Indonesian expected words
    assert any(k in out for k in ("breathe", "bernapas", "nafas")), "breathe() should print or output something indicative of breathing"
    assert any(k in out for k in ("move", "bergerak")), "move() should print or output something indicative of moving"
    assert any(k in out for k in ("fly", "terbang")), "fly() should print or output something indicative of flying"
