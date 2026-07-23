/**
 * التحقق من صحة الرقم الضريبي السعودي (VAT Number) — يشتغل في المتصفح وNode.
 *
 * القواعد الرسمية: 15 خانة رقمية، يبدأ بالرقم 3 وينتهي بالرقم 3.
 * الخانة الحادية عشرة = 1 عضو مجموعة ضريبية، 0 = منشأة مستقلة.
 *
 * أداة مجانية من ZATCA Tools — https://zatcatools.com
 */

export function validateSaudiVat(vat) {
  const digits = String(vat).replace(/\D/g, '');

  const checks = {
    'طول 15 خانة': digits.length === 15,
    'يبدأ بالرقم 3': digits.startsWith('3'),
    'ينتهي بالرقم 3': digits.endsWith('3'),
  };

  return {
    vat: digits,
    valid: Object.values(checks).every(Boolean),
    checks,
    vatGroupMember: digits.length === 15 && digits[10] === '1',
  };
}

// تشغيل مباشر من سطر الأوامر: node validate.js 310122393500003
if (typeof process !== 'undefined' && process.argv?.[2]) {
  const result = validateSaudiVat(process.argv[2]);
  for (const [check, ok] of Object.entries(result.checks)) {
    console.log(`${ok ? '✅' : '❌'} ${check}`);
  }
  console.log(
    result.valid
      ? `\n✅ الرقم صحيح الصيغة (${result.vatGroupMember ? 'عضو مجموعة ضريبية' : 'منشأة مستقلة'})`
      : '\n❌ الرقم غير صحيح'
  );
}
