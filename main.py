import os


class Cd:
    current_dir = os.getcwd()

    def __init__(self, path):
        if not os.path.isdir(path):
            raise ValueError
        self.path = path

    def __enter__(self):
        os.chdir(self.path)
        print(f"Working directory is changed to {self.path}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Working directory is changed to {self.current_dir}")
