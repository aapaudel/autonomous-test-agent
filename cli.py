import sys
import os

# Add the current directory (project root) to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ai_test_generator.core.agent import create_test_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cli.py <path_to_source_code>")
        sys.exit(1)

    source_path = sys.argv[1]
    create_test_file(source_path)
