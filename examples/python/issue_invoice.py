# -*- coding: utf-8 -*-
"""
إصدار فاتورة مبسطة معتمدة من ZATCA عبر ZATCA Tools API — مكتبة Python القياسية فقط.
التوثيق الكامل: https://zatcatools.com/docs/api

التشغيل:  ZTK_KEY=ztk_live_xxx python issue_invoice.py
"""
import json
import os
import urllib.error
import urllib.request

API = "https://zatcatools.com/api/v1"
KEY = os.environ.get("ZTK_KEY", "ztk_live_YOUR_KEY")

payload = {
    "type": "simplified",  # simplified = مبسطة (B2C) | standard = ضريبية (B2B، تحتاج customer)
    "lines": [
        {"name": "خدمة استشارية", "quantity": 1, "unit_price": 500},
    ],
}

req = urllib.request.Request(
    f"{API}/invoices",
    data=json.dumps(payload, ensure_ascii=False).encode(),
    headers={
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    },
    method="POST",
)

try:
    with urllib.request.urlopen(req, timeout=60) as r:
        invoice = json.load(r)
except urllib.error.HTTPError as e:
    error = json.load(e)
    raise SystemExit(f"فشل الإصدار ({e.code}): {error['error']['message']}")

print(f"✅ الفاتورة {invoice['number']} — الحالة: {invoice['status']}")
print(f"الإجمالي: {invoice['totals']['grand']} {invoice['totals']['currency']}")
print(f"PDF: {invoice['links']['pdf']}")
