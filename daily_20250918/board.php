<?php

$data = [];

function get_id($line) {
    $pattern = "/^\[(\d+)\]/";
    preg_match($pattern, $line, $matches);
    if (count($matches) >= 2) {
        return $matches[1];
    } else {
        return NULL;
    }
}

function show_list() {
    global $data;
    return implode("", array_values($data));
}

function post($text) {
    global $data;
    $id = empty($data) ? 1 : max(array_keys($data)) + 1;
    $date = date("Y-m-d H:i:s");
    $data[$id] = "[$id] ($date) $text\n";
    echo "投稿しました。ID: $id\n";
}

function delete($id) {
    global $data;
    if (array_key_exists($id, $data)) {
        unset($data[$id]);
        echo "投稿を削除しました。\n";
    } else {
        echo "存在しない投稿 ID です。\n";
    }
}

$FILENAME = "board.txt";

if (file_exists($FILENAME)) {
    foreach(file($FILENAME) as $line) {
        if (strlen($line) == 0) {
            continue;
        }
        $id = get_id($line);
        if (!is_null($id)) {
            $data[$id] = $line;
        } else {
            echo "無効な行を削除しました。\n";
        }
    }
}

if ($argc < 2) {
    echo "コマンドを指定してください。\n";
} elseif ($argv[1] == "post") {
    if ($argc < 3) {
        echo "投稿内容を入力して下さい。\n";
        exit(1);
    }
    post($argv[2]);
} elseif ($argv[1] == "list") {
    echo show_list();
} elseif ($argv[1] == "delete") {
    if ($argc < 3) {
        echo "ID を指定してください。\n";
        exit(1);
    }
    delete($argv[2]);
} else {
    echo "無効なコマンドです。";
    exit(1);
}

file_put_contents($FILENAME, show_list());

?>