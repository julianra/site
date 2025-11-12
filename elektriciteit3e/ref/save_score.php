<?php
// Bestand waarin alle scores worden bewaard
$file = __DIR__ . '/scores.json';

// JSON-bestand lezen of nieuw starten
if (file_exists($file)) {
    $data = json_decode(file_get_contents($file), true);
    if (!is_array($data)) $data = [];
} else {
    $data = [];
}

// Inkomende data
$input = json_decode(file_get_contents('php://input'), true);
$name  = trim($input['name'] ?? '');
$klas  = trim($input['klas'] ?? '');
$code  = trim($input['code'] ?? '');
$score = (int)($input['score'] ?? 0);

if ($name === '' || $klas === '' || $code === '') {
    http_response_code(400);
    echo json_encode(['error' => 'Ongeldige invoer']);
    exit;
}

// Bestaande speler zoeken
$found = false;
foreach ($data as &$row) {
    if ($row['name'] === $name && $row['klas'] === $klas && $row['code'] === $code) {
        $found = true;
        if ($score > $row['score']) $row['score'] = $score;
        break;
    }
}
unset($row);

// Nieuwe speler?
if (!$found) {
    $data[] = ['name'=>$name,'klas'=>$klas,'code'=>$code,'score'=>$score];
}

// Bestand opslaan
file_put_contents($file, json_encode($data, JSON_PRETTY_PRINT));

// Resultaat terugsturen
echo json_encode(['ok'=>true,'data'=>$data]);
?>
