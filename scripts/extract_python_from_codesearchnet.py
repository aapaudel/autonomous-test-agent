import ir_datasets
import os

def extract_python_functions(limit=10, output_dir='application'):
    os.makedirs(output_dir, exist_ok=True)
    ds = ir_datasets.load("codesearchnet")

    count = 0
    saved = 0
    print(f"Streaming Python functions from CodeSearchNet...")

    output_file = os.path.join(output_dir, 'python_functions_sample.py')
    with open(output_file, 'w') as f:
        for doc in ds.docs_iter():
            if doc.language == 'python' and doc.code:
                f.write(f"\n# From repo: {doc.repo}\n")
                f.write(doc.code + "\n")
                saved += 1
            count += 1
            if saved >= limit:
                break

    print(f"Saved {saved} Python functions (scanned {count} entries).")
    print(f"Output file: {output_file}")

if __name__ == "__main__":
    extract_python_functions(limit=20)
