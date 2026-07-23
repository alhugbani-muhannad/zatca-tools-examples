# -*- coding: utf-8 -*-
"""
توليد رمز QR متوافق مع المرحلة الأولى من الفوترة الإلكترونية السعودية (TLV base64).

حسب مواصفات ZATCA، رمز المرحلة الأولى = خمسة وسوم TLV مشفّرة base64:
  1: اسم البائع   2: الرقم الضريبي   3: طابع الوقت ISO8601   4: الإجمالي شامل الضريبة   5: مبلغ الضريبة

    python generate.py "مؤسسة الأمل" 310122393500003 "2026-07-19T14:30:00Z" 115.00 15.00

الناتج: سلسلة base64 — حوّلها لصورة QR بأي مكتبة (qrcode في Python مثلًا).
أداة مجانية من ZATCA Tools — https://zatcatools.com

⚠️ ملاحظة: المرحلة الثانية تتطلب وسوم توقيع إضافية (6-9) لا يمكن توليدها إلا بشهادة
ختم تشفير معتمدة من الهيئة — وهذا بالضبط ما تتولاه منصة ZATCA Tools عنك تلقائيًا.
"""
import base64
import sys

# Windows console compatibility (cp1252 -> UTF-8)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def tlv(tag: int, value: str) -> bytes:
    encoded = value.encode("utf-8")
    if len(encoded) > 255:
        raise ValueError(f"قيمة الوسم {tag} أطول من 255 بايت")
    return bytes([tag, len(encoded)]) + encoded


def phase1_qr(seller: str, vat: str, timestamp: str, total: str, vat_amount: str) -> str:
    payload = tlv(1, seller) + tlv(2, vat) + tlv(3, timestamp) + tlv(4, total) + tlv(5, vat_amount)
    return base64.b64encode(payload).decode()


if __name__ == "__main__":
    if len(sys.argv) != 6:
        raise SystemExit(
            'الاستخدام: python generate.py "اسم البائع" الرقم_الضريبي '
            '"2026-07-19T14:30:00Z" الإجمالي مبلغ_الضريبة'
        )

    print(phase1_qr(*sys.argv[1:6]))
