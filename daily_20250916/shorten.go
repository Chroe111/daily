package main

import (
	"bufio"
	"fmt"
	"maps"
	"os"
	"slices"
	"strconv"
	"strings"
)

var data = make(map[int]string)
var lastId = 0

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print("> ")
		scanner.Scan()
		args := strings.Split(scanner.Text(), " ")

		if len(args) < 1 {
			fmt.Println("コマンドを指定してください。")
			continue
		} else if args[0] == "shorten" {
			if len(args) < 2 {
				fmt.Println("URL を指定してください。")
				continue
			}
			if !strings.HasPrefix(args[1], "http://") && !strings.HasPrefix(args[1], "https://") {
				fmt.Println("無効な URL です。")
				continue
			}
			lastId += 1
			data[lastId] = args[1]
			fmt.Printf("短縮 ID: %d を発行しました。\n", lastId)
		} else if args[0] == "lookup" {
			if len(args) < 2 {
				fmt.Println("ID を指定してください。")
				continue
			}
			id, parseErr := strconv.Atoi(args[1])
			if parseErr != nil {
				fmt.Println("不正な ID です")
				continue
			}
			url, exist := data[id]
			if !exist {
				fmt.Println("存在しない ID です")
				continue
			}
			fmt.Println(url)
		} else if args[0] == "list" {
			for _, key := range slices.Sorted(maps.Keys(data)) {
				fmt.Printf("%d: %s\n", key, data[key])
			}
		} else if args[0] == "exit" {
			fmt.Println("終了します。")
			break
		} else {
			fmt.Println("存在しないコマンドです。")
		}
	}
}
