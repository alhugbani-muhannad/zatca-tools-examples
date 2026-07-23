# -*- coding: utf-8 -*-
"""
التحقق من صحة الرقم الضريبي السعودي (VAT Number).

القواعد الرسمية: 15 خانة رقمية، يبدأ بالرقم 3 وينتهي بالرقم 3.
الخانة الحادية عشرة = 1 تعني عضو مجموعة ضريبية، و 0 تعني منشأة مستقلة.

    python validate.py 310122393500003

أداة مجانية من ZATCA Tools — https://zatcatools.com
"""
import re
import sys

# Windows console compatibility (cp1252 -> UTF-8)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def validate_saudi_vat(vat: str) -> dict:
    digits = re.sub(r"\D", "", vat)

    checks = {
        "طول 15 خانة": len(digits) == 15,
        "يبدأ بالرقم 3": digits.startswith("3") if digits else False,
        "ينتهي بالرقم 3": digits.endswith("3") if digits else False,
    }

    return {
        "vat": digits,
        "valid": all(checks.values()),
        "checks": checks,
        "vat_group_member": len(digits) == 15 and digits[10] == "1",
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("الاستخدام: python validate.py <الرقم_الضريبي>")

    result = validate_saudi_vat(sys.argv[1])
    for check, ok in result["checks"].items():
        print(f"{'✅' if ok else '❌'} {check}")

    if result["valid"]:
        kind = "عضو مجموعة ضريبية" if result["vat_group_member"] else "منشأة مستقلة"
        print(f"\n✅ الرقم صحيح الصيغة ({kind})")
    else:
        print("\n❌ الرقم غير صحيح")
