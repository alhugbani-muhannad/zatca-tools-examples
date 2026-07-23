<div dir="rtl">

# ✅ التحقق من الرقم الضريبي السعودي (VAT Validator)

تحقّق من صيغة أي رقم ضريبي سعودي قبل ما ترسله لأنظمة الفوترة — حسب القواعد الرسمية:

- **15 خانة** رقمية
- **يبدأ** بالرقم 3 و**ينتهي** بالرقم 3
- الخانة **الحادية عشرة**: `1` = عضو مجموعة ضريبية (يحتاج TIN إضافي عند الربط) · `0` = منشأة مستقلة

## الاستخدام

```bash
# Python
python validate.py 310122393500003

# Node.js / متصفح (ES Module)
node validate.js 310122393500003
```

```js
import { validateSaudiVat } from './validate.js';

validateSaudiVat('310122393500003');
// { valid: true, vatGroupMember: false, checks: {...} }
```

---

💡 [ZATCA Tools](https://zatcatools.com) يتحقق من الرقم الضريبي تلقائيًا ويربط منشأتك مع الهيئة خلال دقائق — مجانًا.

</div>
