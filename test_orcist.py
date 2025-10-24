from HexingSpells import to_decimal, to_base
import pytest

def test_to_decimal_conversion():
    """Tests the conversions from provided base to base 10"""
    assert to_decimal("C7", 16) == 199
    assert to_decimal("1111000", 2) == 120
    assert to_decimal("4S", 36) == 172
    assert to_decimal("A", 18) == 10
    assert to_decimal("125", 6) == 53
def test_to_base_conversion():
    """Tests the conversions from base 10 to the provided base"""
    assert to_base(199, 16) == "C7"
    assert to_base(48, 20) == "28"
    assert to_base(32, 3) == "1012"
    assert to_base(182392, 33) == "52G1"
    assert to_base(1, 1) == "1"

