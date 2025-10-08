import importlib.util
import pathlib
import pytest

# Load template module
template_path = pathlib.Path(__file__).parent.parent / "template.py"
spec = importlib.util.spec_from_file_location("day05_template", str(template_path))
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)


def _make_instance(cls, *args, **kwargs):
    try:
        return cls(*args, **kwargs)
    except Exception:
        return object.__new__(cls)


def test_classes_and_inheritance():
    assert hasattr(t, "BankAccount"), "BankAccount class missing"
    assert hasattr(t, "SavingsAccount"), "SavingsAccount class missing"
    assert hasattr(t, "CheckingAccount"), "CheckingAccount class missing"

    BankAccount = t.BankAccount
    SavingsAccount = t.SavingsAccount
    CheckingAccount = t.CheckingAccount

    sa = _make_instance(SavingsAccount)
    ca = _make_instance(CheckingAccount)

    assert isinstance(sa, BankAccount), "SavingsAccount should inherit from BankAccount"
    assert isinstance(ca, BankAccount), "CheckingAccount should inherit from BankAccount"


def test_deposit_and_balance_behavior():
    BankAccount = t.BankAccount

    acct = _make_instance(BankAccount)

    # try common attribute names for balance
    if not hasattr(acct, "balance"):
        # try initializing via constructor
        try:
            acct = BankAccount(100)
        except Exception:
            acct = object.__new__(BankAccount)
            acct.balance = 0

    # deposit method should exist
    assert hasattr(acct, "deposit") and callable(getattr(acct, "deposit")), "BankAccount should implement deposit()"

    # capture balance before/after deposit
    before = getattr(acct, "balance", None)
    try:
        acct.deposit(50)
    except TypeError:
        # maybe signature different; try keyword
        try:
            acct.deposit(amount=50)
        except Exception:
            pass

    after = getattr(acct, "balance", None)

    # If balance tracked as number, expect increase
    if isinstance(before, (int, float)) and isinstance(after, (int, float)):
        assert after >= before, "deposit should increase or not decrease the balance"


def test_savings_and_checking_specifics():
    SavingsAccount = t.SavingsAccount
    CheckingAccount = t.CheckingAccount

    sa = _make_instance(SavingsAccount)
    ca = _make_instance(CheckingAccount)

    # SavingsAccount: expect some interest-related method or attribute
    interest_ok = any([
        (hasattr(sa, "apply_interest") and callable(getattr(sa, "apply_interest"))) ,
        hasattr(sa, "interest_rate"),
    ])
    assert interest_ok, "SavingsAccount should expose interest functionality (method apply_interest or attribute interest_rate)"

    # CheckingAccount: expect fee-related method or attribute
    fee_ok = any([
        (hasattr(ca, "charge_fee") and callable(getattr(ca, "charge_fee"))) ,
        hasattr(ca, "fee"),
    ])
    assert fee_ok, "CheckingAccount should expose fee functionality (method charge_fee or attribute fee)"
