import argparse
import os
from ai_test_generator.core.test_generator import (
    generate_tests_for_file,
    generate_tests_for_changed_files,
    generate_tests_for_all_files,
)


def main():
    parser = argparse.ArgumentParser(description="AI-based Test Generator CLI")
    parser.add_argument("--file", type=str, help="Generate tests for a specific file")
    parser.add_argument("--on-change", action="store_true", help="Generate tests for changed files only")
    parser.add_argument("--all", action="store_true", help="Generate tests for all source files")
    parser.add_argument("--src", type=str, default="project2/", help="Source directory to scan")
    parser.add_argument("--out", type=str, default="project2/tests/", help="Directory to save generated tests")

    args = parser.parse_args()

    if args.file:
        file_path = args.file
        if not os.path.isfile(file_path):
            file_path = os.path.join(args.src, file_path)
        generate_tests_for_file(file_path, args.out)
    elif args.on_change:
        generate_tests_for_changed_files(args.src, args.out)
    elif args.all:
        generate_tests_for_all_files(args.src, args.out)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()