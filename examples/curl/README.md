<div dir="rtl">

# أمثلة cURL — ZATCA Tools API

كل الطلبات تحتاج مفتاح API في الترويسة: `Authorization: Bearer ztk_live_...`
([كيف أحصل على المفتاح؟](../../README.md#quick-start))

</div>

```bash
export ZTK_KEY="ztk_live_YOUR_KEY"
export ZTK="https://zatcatools.up.railway.app/api/v1"
```

## 1) Account — بيانات المنشأة والحصة

```bash
curl "$ZTK/account" -H "Authorization: Bearer $ZTK_KEY"
```

## 2) إصدار فاتورة مبسطة (B2C) — تُبلَّغ للهيئة فورًا

```bash
curl -X POST "$ZTK/invoices" \
  -H "Authorization: Bearer $ZTK_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "simplified",
    "lines": [
      { "name": "قهوة عربية — كيس 500 جم", "quantity": 2, "unit_price": 45 },
      { "name": "توصيل", "quantity": 1, "unit_price": 15 }
    ]
  }'
```

## 3) إصدار فاتورة ضريبية (B2B) — مع بيانات العميل

```bash
curl -X POST "$ZTK/invoices" \
  -H "Authorization: Bearer $ZTK_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "standard",
    "customer": {
      "name": "شركة العميل التجارية",
      "vat_number": "311111111101113",
      "street": "طريق الملك فهد",
      "building_number": "8228",
      "city": "الرياض",
      "postal_zone": "12262"
    },
    "lines": [{ "name": "اشتراك سنوي", "quantity": 1, "unit_price": 5000 }]
  }'
```

## 4) قائمة الفواتير (مع فلترة وترقيم صفحات)

```bash
curl "$ZTK/invoices?status=accepted&per_page=10" -H "Authorization: Bearer $ZTK_KEY"
```

## 5) فاتورة واحدة + تنزيل PDF / XML / QR

```bash
curl "$ZTK/invoices/INVOICE_UUID"      -H "Authorization: Bearer $ZTK_KEY"
curl "$ZTK/invoices/INVOICE_UUID/pdf"  -H "Authorization: Bearer $ZTK_KEY" -o invoice.pdf
curl "$ZTK/invoices/INVOICE_UUID/xml"  -H "Authorization: Bearer $ZTK_KEY" -o invoice.xml
curl "$ZTK/invoices/INVOICE_UUID/qr.svg" -H "Authorization: Bearer $ZTK_KEY" -o qr.svg
```

## 6) إشعار دائن (إلغاء/تخفيض) — يرجع للفاتورة الأصلية بسبب إلزامي

```bash
curl -X POST "$ZTK/notes" \
  -H "Authorization: Bearer $ZTK_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "kind": "credit",
    "invoice_uuid": "INVOICE_UUID",
    "reason": "إرجاع المنتج",
    "lines": [{ "name": "قهوة عربية — كيس 500 جم", "quantity": 1, "unit_price": 45 }]
  }'
```

<div dir="rtl">

## شكل الخطأ الموحّد

كل الأخطاء ترجع بنفس الصيغة مع رمز HTTP مناسب (401/402/409/422):

```json
{ "error": { "code": "quota_exceeded", "message": "..." } }
```

</div>
