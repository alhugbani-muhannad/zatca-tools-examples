/**
 * فك تشفير رمز QR للفاتورة الإلكترونية السعودية (صيغة TLV حسب مواصفات ZATCA).
 *
 *     node decode.mjs "BASE64_FROM_QR..."
 *
 * يدعم وسوم المرحلة الأولى (1-5) والمرحلة الثانية (6-9).
 * أداة مجانية من ZATCA Tools — https://zatcatools.up.railway.app
 */

const TAGS = {
  1: 'اسم البائع',
  2: 'الرقم الضريبي للبائع',
  3: 'طابع الوقت (التاريخ والوقت)',
  4: 'إجمالي الفاتورة (شامل الضريبة)',
  5: 'إجمالي ضريبة القيمة المضافة',
  6: 'تجزئة XML للفاتورة (SHA-256)',
  7: 'التوقيع الرقمي ECDSA',
  8: 'المفتاح العام ECDSA للبائع',
  9: 'توقيع شهادة ختم التشفير',
};
const BINARY_TAGS = new Set([7, 8, 9]);

export function decodeTlv(base64) {
  const raw = Buffer.from(base64, 'base64');
  const fields = [];
  for (let i = 0; i + 2 <= raw.length; ) {
    const tag = raw[i];
    const length = raw[i + 1];
    const value = raw.subarray(i + 2, i + 2 + length);
    fields.push({
      tag,
      label: TAGS[tag] ?? `وسم غير معروف (${tag})`,
      value: BINARY_TAGS.has(tag) ? value.toString('hex') : value.toString('utf8'),
    });
    i += 2 + length;
  }
  return fields;
}

if (process.argv[2]) {
  for (const { tag, label, value } of decodeTlv(process.argv[2].trim())) {
    const shown = value.length > 80 ? value.slice(0, 77) + '...' : value;
    console.log(`[${tag}] ${label}: ${shown}`);
  }
} else {
  console.log('الاستخدام: node decode.mjs <base64_من_رمز_QR>');
}
