/**
 * إصدار فاتورة مبسطة معتمدة من ZATCA عبر ZATCA Tools API — Node.js 18+ (fetch مدمج).
 * التوثيق الكامل: https://zatcatools.up.railway.app/docs/api
 *
 * التشغيل:  ZTK_KEY=ztk_live_xxx node issue-invoice.mjs
 */

const API = 'https://zatcatools.up.railway.app/api/v1';
const KEY = process.env.ZTK_KEY ?? 'ztk_live_YOUR_KEY';

const res = await fetch(`${API}/invoices`, {
  method: 'POST',
  headers: {
    Authorization: `Bearer ${KEY}`,
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
  body: JSON.stringify({
    type: 'simplified', // simplified = مبسطة (B2C) | standard = ضريبية (B2B، تحتاج customer)
    lines: [
      { name: 'خدمة استشارية', quantity: 1, unit_price: 500 },
    ],
  }),
});

const invoice = await res.json();

if (!res.ok) {
  console.error(`فشل الإصدار (${res.status}):`, invoice.error?.message);
  process.exit(1);
}

console.log(`✅ الفاتورة ${invoice.number} — الحالة: ${invoice.status}`);
console.log(`الإجمالي: ${invoice.totals.grand} ${invoice.totals.currency}`);
console.log(`PDF: ${invoice.links.pdf}`);

// تنزيل ملف الـ PDF المعتمد
const pdf = await fetch(invoice.links.pdf, { headers: { Authorization: `Bearer ${KEY}` } });
await import('node:fs/promises').then(fs =>
  fs.writeFile(`${invoice.number}.pdf`, Buffer.from(await pdf.arrayBuffer()))
);
console.log(`💾 تم حفظ ${invoice.number}.pdf`);
