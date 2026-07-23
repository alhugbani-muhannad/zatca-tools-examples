# -*- coding: utf-8 -*-
"""
فك تشفير رمز QR للفاتورة الإلكترونية السعودية (صيغة TLV حسب مواصفات ZATCA).

امسح رمز QR بأي قارئ، انسخ النص (base64)، ومرّره للأداة:

    python decode.py "BASE64_FROM_QR"

يدعم وسوم المرحلة الأولى (1-5) والمرحلة الثانية (6-9).
أداة مجانية من ZATCA Tools — https://zatcatools.com
"""
import base64
import sys

# Windows console compatibility (cp1252 -> UTF-8)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TAGS = {
    1: "اسم البائع",
    2: "الرقم الضريبي للبائع",
    3: "طابع الوقت (التاريخ والوقت)",
    4: "إجمالي الفاتورة (شامل الضريبة)",
    5: "إجمالي ضريبة القيمة المضافة",
    6: "تجزئة XML للفاتورة (SHA-256)",       # المرحلة الثانية
    7: "التوقيع الرقمي ECDSA",                 # المرحلة الثانية
    8: "المفتاح العام ECDSA للبائع",           # المرحلة الثانية
    9: "توقيع شهادة ختم التشفير",              # المرحلة الثانية
}
BINARY_TAGS = {7, 8, 9}  # قيم ثنائية — تُعرض hex


def decode_tlv(b64: str) -> list[tuple[int, str]]:
    raw = base64.b64decode(b64)
    fields, i = [], 0
    while i + 2 <= len(raw):
        tag, length = raw[i], raw[i + 1]
        value = raw[i + 2 : i + 2 + length]
        fields.append((tag, value.hex() if tag in BINARY_TAGS else value.decode("utf-8", "replace")))
        i += 2 + length
    return fields


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("الاستخدام: python decode.py <base64_من_رمز_QR>")

    for tag, value in decode_tlv(sys.argv[1].strip()):
        label = TAGS.get(tag, f"وسم غير معروف ({tag})")
        shown = value if len(value) <= 80 else value[:77] + "..."
        print(f"[{tag}] {label}: {shown}")
