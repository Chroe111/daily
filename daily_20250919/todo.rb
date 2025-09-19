require "json"

FILENAME = "todo.json"

$data = []
if File.exist?(FILENAME)
    File.open(FILENAME, "r") do |file| 
        $data = JSON.load(file)
    end
end

def find(id)
    return $data.find{|todo| todo["id"] == id}
end

def parse_number(input)
    begin
      return Integer(input)
    rescue 
        return nil
    end
end

def add(task)
    id = $data.empty? ? 1 : $data.map{|todo| todo["id"]}.max + 1
    $data.push({"id" => id, "task" => task, "done" => false})
    puts "タスクを登録しました。タスク ID: #{id}"
end

def list()
    if $data.empty?
        puts "タスクは登録されていません。"
    else
        for todo in $data do
            puts "[#{todo['done'] ? 'x' : ' '}] #{todo['id']}. #{todo['task']}"
        end
    end
end

def done(id)
    todo = find(id)
    if todo.nil?
        puts "存在しない ID です。"
        return
    end
    todo["done"] = true
    puts "タスク「#{todo['task']}」を完了しました。"
end

def delete(id)
    todo = find(id)
    if todo.nil?
        puts "存在しない ID です。"
        return
    end
    $data.delete(todo)
    puts "タスク「#{todo['task']}」を削除しました。"
end

if ARGV.length == 0
    puts "コマンドを指定してください。"
    exit(1)
elsif ARGV[0] == "add"
    if ARGV.length == 1
        puts "内容を指定してください。"
        exit(1)
    end
    add(ARGV[1])
elsif ARGV[0] == "list"
    list()
elsif ARGV[0] == "done"
    if ARGV.length == 1
        puts "ID を指定してください。"
        exit(1)
    end
    id = parse_number(ARGV[1])
    if id.nil?
        puts "無効な ID です。"
        exit(1)
    end
    done(id)
elsif ARGV[0] == "delete"
    if ARGV.length == 1
        puts("ID を指定してください。")
        exit(1)
    end
    id = parse_number(ARGV[1])
    if id.nil?
        puts "無効な ID です。"
        exit(1)
    end
    delete(id)
else
    puts "無効なコマンドです。"
    exit(1)
end

File.open(FILENAME, "w") do |file|
    JSON.dump($data, file)
end
