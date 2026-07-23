<?php
/**
 * إصدار فاتورة مبسطة معتمدة من ZATCA عبر ZATCA Tools API — بدون أي مكتبات خارجية.
 * التوثيق الكامل: https://zatcatools.com/docs/api
 */

$apiKey = getenv('ZTK_KEY') ?: 'ztk_live_YOUR_KEY';

$payload = [
    'type' => 'simplified', // simplified = مبسطة (B2C) | standard = ضريبية (B2B، تحتاج customer)
    'lines' => [
        ['name' => 'خدمة استشارية', 'quantity' => 1, 'unit_price' => 500],
    ],
];

$ch = curl_init('https://zatcatools.com/api/v1/invoices');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => json_encode($payload, JSON_UNESCAPED_UNICODE),
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer '.$apiKey,
        'Content-Type: application/json',
        'Accept: application/json',
    ],
]);

$response = json_decode(curl_exec($ch), true);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($status !== 201) {
    exit("فشل الإصدار ({$status}): ".($response['error']['message'] ?? 'خطأ غير معروف')."\n");
}

echo "✅ الفاتورة {$response['number']} — الحالة: {$response['status']}\n";
echo "الإجمالي: {$response['totals']['grand']} {$response['totals']['currency']}\n";
echo "PDF: {$response['links']['pdf']}\n";
echo "XML: {$response['links']['xml']}\n";
