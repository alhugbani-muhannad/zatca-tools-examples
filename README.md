<div dir="rtl">

# 🇸🇦 أمثلة وأدوات الفوترة الإلكترونية — ZATCA Tools

أمثلة تكامل جاهزة وأدوات مجانية للفوترة الإلكترونية السعودية (**المرحلة الثانية — منصة فاتورة**).

هذا المستودع مقدّم من [**ZATCA Tools**](https://zatcatools.up.railway.app) — أسرع طريقة تربط منشأتك مع هيئة الزكاة والضريبة والجمارك وتصدر فواتير معتمدة خلال دقائق، بدون نظام محاسبي وبدون تعقيد. **ابدأ مجانًا بأول 50 فاتورة.**

| | |
|---|---|
| 🌐 المنصة | [zatcatools.up.railway.app](https://zatcatools.up.railway.app) |
| 📚 توثيق الـ API | [zatcatools.up.railway.app/docs/api](https://zatcatools.up.railway.app/docs/api) |
| ✍️ المدونة (أدلة عربية) | [zatcatools.up.railway.app/blog](https://zatcatools.up.railway.app/blog) |

---

## 📦 وش تلقى هنا؟

### 1) أمثلة التكامل مع الـ API — [`examples/`](examples/)

أصدر فاتورة ضريبية معتمدة من الهيئة بأقل من 30 سطر كود:

| اللغة | الملف |
|---|---|
| cURL | [`examples/curl/README.md`](examples/curl/README.md) |
| PHP | [`examples/php/issue-invoice.php`](examples/php/issue-invoice.php) |
| Node.js | [`examples/node/issue-invoice.mjs`](examples/node/issue-invoice.mjs) |
| Python | [`examples/python/issue_invoice.py`](examples/python/issue_invoice.py) |

**كل الأمثلة تستخدم [ZATCA Tools REST API](https://zatcatools.up.railway.app/docs/api):** أنت ترسل بنود الفاتورة كـ JSON، والمنصة تتولى كل التعقيد — XML بصيغة UBL، التوقيع الرقمي، رمز QR، وسلسلة ICV/PIH، والإرسال للهيئة — وترجع لك الفاتورة المعتمدة بروابط PDF وXML جاهزة.

```bash
curl -X POST https://zatcatools.up.railway.app/api/v1/invoices \
  -H "Authorization: Bearer ztk_live_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"type":"simplified","lines":[{"name":"خدمة استشارية","quantity":1,"unit_price":500}]}'
```

> 🔑 **مفتاح الـ API**: سجّل مجانًا في [ZATCA Tools](https://zatcatools.up.railway.app/start) ← أكمل الربط مع فاتورة ← الإعدادات ← تبويب API ← «توليد مفتاح».

### 2) أدوات مجانية — [`tools/`](tools/)

أدوات مستقلة تفيدك حتى لو ما كنت تستخدم منصتنا:

| الأداة | وش تسوي |
|---|---|
| [`qr-tlv-decoder`](tools/qr-tlv-decoder/) | فك تشفير رمز QR لأي فاتورة سعودية (TLV → حقول مقروءة) |
| [`qr-tlv-generator`](tools/qr-tlv-generator/) | توليد رمز QR متوافق مع المرحلة الأولى (TLV base64) |
| [`vat-validator`](tools/vat-validator/) | التحقق من صحة الرقم الضريبي السعودي (15 رقم) |

---

## 🤔 ليش ZATCA Tools؟

- ⚡ **ربط خلال دقائق**: CSR والشهادات وفحوص التوافق الستة — كلها تلقائية
- 🧾 **فواتير ضريبية (B2B) ومبسطة (B2C)** موقّعة ومعتمدة، مع إشعارات الدائن والمدين
- 🔗 **REST API** نظيف للمطورين — JSON داخل، فاتورة معتمدة + PDF خارج
- 🗄️ **أرشفة XML/PDF** لكل فاتورة بصيغتها النظامية
- 🆓 **مجاني** — أول 50 فاتورة بدون بطاقة

---

## المساهمة

لقيت خطأ أو عندك مثال بلغة ثانية؟ افتح Issue أو Pull Request — كل مساهمة مرحّب فيها 🤝

## الترخيص

[MIT](LICENSE) — استخدم الأكواد بحرية في مشاريعك.

</div>

---

<div dir="ltr">

**English summary**: Integration examples (cURL/PHP/Node/Python) and free developer tools (TLV QR decoder/generator, VAT number validator) for Saudi Arabia's ZATCA Phase 2 e-invoicing (Fatoora), provided by [ZATCA Tools](https://zatcatools.up.railway.app) — the fastest way for Saudi businesses to connect to ZATCA and issue compliant e-invoices via a clean REST API. First 50 invoices free.

**Keywords**: ZATCA, Fatoora, فاتورة, الفوترة الإلكترونية, e-invoicing Saudi Arabia, KSA VAT, TLV QR, UBL, simplified tax invoice, فاتورة ضريبية مبسطة

</div>
