#!/bin/sh

# 作業用ディレクトリ作成
mkdir -p testdir/docs
mkdir -p testdir/notes
mkdir -p testdir/src

# docs
echo "This file contains important keyword notes." > testdir/docs/keyword_notes.txt
echo "General documentation." > testdir/docs/readme.txt

# notes
echo "TODO: remember to include the keyword in tomorrow's task." > testdir/notes/todo.txt
echo "Just a memo, nothing special." > testdir/notes/memo.txt

# src
echo "print('Hello World')" > testdir/src/main.py
echo "# utility functions for keyword handling" > testdir/src/keyword_util.py
