import os

class ChangeWatcher:
    def __init__(self, watch_path='.', cache_file='.file_timestamps'):
        self.watch_path = watch_path
        self.cache_file = cache_file
        self.timestamps = self.load_cache()

    def load_cache(self):
        if not os.path.exists(self.cache_file):
            return {}
        with open(self.cache_file, 'r') as f:
            lines = f.readlines()
        return {line.split(',')[0]: float(line.strip().split(',')[1]) for line in lines}

    def save_cache(self):
        with open(self.cache_file, 'w') as f:
            for filepath, mtime in self.timestamps.items():
                f.write(f"{filepath},{mtime}\n")

    def get_changed_files(self):
        changed_files = []
        for dirpath, _, files in os.walk(self.watch_path):
            for fname in files:
                if fname.endswith('.py') and '__pycache__' not in dirpath:
                    full_path = os.path.join(dirpath, fname)
                    mtime = os.path.getmtime(full_path)
                    if full_path not in self.timestamps or self.timestamps[full_path] < mtime:
                        changed_files.append(full_path)
                        self.timestamps[full_path] = mtime
        return changed_files
