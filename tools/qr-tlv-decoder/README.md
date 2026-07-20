<div dir="rtl">

# 🔍 فك تشفير QR الفاتورة السعودية (TLV Decoder)

كل فاتورة إلكترونية سعودية تحمل رمز QR بصيغة **TLV** (Tag-Length-Value) مشفّرة base64 حسب مواصفات ZATCA. هذي الأداة تفكّها وتعرض الحقول بشكل مقروء — مفيدة للتحقق من الفواتير أو تصحيح أخطاء التكامل.

## الاستخدام

امسح رمز QR بأي تطبيق قارئ، انسخ النص الناتج (سلسلة base64 طويلة)، ثم:

```bash
# Python (بدون أي مكتبات)
python decode.py "BASE64_من_رمز_QR"

# Node.js
node decode.mjs "BASE64_من_رمز_QR"
```

## جرّبها الآن — مثال جاهز (فاتورة مرحلة ثانية)

<div dir="ltr">

```bash
python decode.py "ASbZhdik2LPYs9ipINin2YTYo9mF2YQg2KfZhNiq2KzYp9ix2YrYqQIPMzEwMTIyMzkzNTAwMDAzAxQyMDI2LTA3LTE5VDE0OjMwOjAwWgQGMTE1LjAwBQUxNS4wMAYsQXJob294eXgzVk5mcTNneFZ4dU9Ua3grWDFESFlINWhHeDFPRlBsNFZnUT0HQKVDmX2E8SeYNQwJve8s2xcb9B7T5KX4CK8v6wxWJjAJx+9Fr9ZJS8i7RLUnTOLkbZHrpa2LcTamk4Kb6ku9WlkIIAAX3qd3D37P96s8IFBlRhKelr3rovVEu45UFOt5eGEiCSAGKYQy6AZrKeIiO8wjqpUEtWrlCPq/NDVQiGm5wxkOIg=="
```

```
[1] اسم البائع: مؤسسة الأمل التجارية
[2] الرقم الضريبي للبائع: 310122393500003
[3] طابع الوقت (التاريخ والوقت): 2026-07-19T14:30:00Z
[4] إجمالي الفاتورة (شامل الضريبة): 115.00
[5] إجمالي ضريبة القيمة المضافة: 15.00
[6] تجزئة XML للفاتورة (SHA-256): Arhooxyx3VNfq3gxVxuOTkx+X1DHYH5hGx1OFPl4VgQ=
[7] التوقيع الرقمي ECDSA: a543997d84f12798350c09bdef2cdb171bf41ed3e4a5f808af2feb0c56263009c7ef45afd6494...
[8] المفتاح العام ECDSA للبائع: 0017dea7770f7ecff7ab3c20506546129e96bdeba2f544bb8e5414eb79786122
[9] توقيع شهادة ختم التشفير: 06298432e8066b29e2223bcc23aa9504b56ae508fabf3435508869b9c3190e22
```

</div>

الوسوم 1–5 = المرحلة الأولى · الوسوم 6–9 = المرحلة الثانية (تجزئة XML، التوقيع، المفتاح العام، توقيع الشهادة).

---

💡 تبي تصدر فواتير برموز QR معتمدة تلقائيًا؟ جرّب [ZATCA Tools](https://zatcatools.up.railway.app) — مجانًا.

</div>
