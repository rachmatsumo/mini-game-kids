<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$data = file_get_contents('php://input');
if ($data) {
    $json = json_decode($data, true);
    if (is_array($json)) {
        file_put_contents(__DIR__ . '/score.json', json_encode($json, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));
        echo json_encode(['status' => 'success']);
        exit;
    }
}
echo json_encode(['status' => 'error', 'message' => 'Invalid JSON']);
