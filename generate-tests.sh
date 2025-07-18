#!/bin/bash

SRC_DIR="project2/"
OUT_DIR="project2/tests/"

echo "Select test generation mode:"
echo "1) Changed files only"
echo "2) All source files"
echo "3) Specific file"
read -p "Enter option [1-3]: " choice

case $choice in
  1)
    echo "🔍 Generating tests for changed files..."
    python cli.py --on-change --src $SRC_DIR --out $OUT_DIR
    ;;
  2)
    echo "🔁 Generating tests for all source files..."
    python cli.py --all --src $SRC_DIR --out $OUT_DIR
    ;;
  3)
    read -p "Enter the path to the source file (e.g., project2/sample.py): " FILE_PATH
    python cli.py --file $FILE_PATH --out $OUT_DIR
    ;;
  *)
    echo "❌ Invalid option. Exiting."
    ;;
esac
