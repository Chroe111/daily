const fs = require("fs");

const filepath = "access.log";
let log = [];

if (fs.existsSync(filepath)) {
    let text = fs.readFileSync(filepath, "utf-8");
    log = text.split("\n").filter(line => line.length > 0);
}

process.argv.slice(2).forEach(arg => {
    if (arg.startsWith("--date=")) {
        log = log.filter(line => line.startsWith(arg.substring("--date=".length)));
    } else if (arg.startsWith("--keyword=")) {
        log = log.filter(line => line.includes(arg.substring("--keyword=".length)))
    } else {
        console.log("無効な引数が指定されています。");
        process.exit(1);
    }
});

log.forEach(line => console.log(line));
