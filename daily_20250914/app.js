const fs = require("fs");

const filepath = "habits.json";
let data = {"habits": []};

if (fs.existsSync(filepath)) {
    data = JSON.parse(fs.readFileSync("habits.json", "utf-8"));
} else {
    console.log("ファイルが見つかりません。");
    process.exit(1);
}

function add(habit) {
    data["habits"].push({"name": habit, "records": {}});
}

function check(habit, isCompleted) {
    const today = new Date().toLocaleDateString('sv-SE');
    let matched = data["habits"].find(elem => elem["name"] == habit);
    if (matched !== undefined) {
        matched["records"][today] = (isCompleted == "y");
    } else {
        throw new Error();
    }
}

function list() {
    data["habits"].forEach(elem => {
        console.log(elem["name"]);
        Object.entries(elem["records"]).forEach(([day, done]) => {
            console.log(`・${day}: ${done ? "o" : "x"}`);
        })
    })
}

console.log(process.argv);

if (process.argv.length < 3) {
    console.log("コマンドを指定してください。");
    process.exit(1);
} else if (process.argv[2] == "add") {
    if (process.argv.length < 4) {
        console.log("習慣を指定して下さい。");
        process.exit(1);
    } else {
        add(process.argv[3]);
        console.log("習慣を追加しました。");
    }
} else if (process.argv[2] == "check") {
    if (process.argv.length == 5 && (process.argv[4] == "y" || process.argv[4] == "n")) {
        try {
            check(process.argv[3], process.argv[4]);
            console.log("本日の実行を記録しました。");
        } catch {
            console.log("存在しない習慣です。");
            process.exit(1);
        }
    } else {
        console.log("入力が不正です。");
        process.exit(1);
    }
} else if (process.argv[2] == "list") {
    list();
} else {
    console.log("無効なコマンドです。");
    process.exit(1);
}

fs.writeFileSync(filepath, JSON.stringify(data, null, 2));
