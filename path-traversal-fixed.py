import os

# fixed code
def safe_path(path):
    """Checks that argument path is a safe file path. If not, returns None.
    If safe, returns the normalized absolute file path.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.normpath(os.path.join(base_dir, path))

    print(f"Base dir = {base_dir}")
    print(f"Filepath = {filepath}")
    print(f"Common path = {os.path.commonpath([base_dir, filepath])}")

    if base_dir != os.path.commonpath([base_dir, filepath]):
        return None
    return filepath

print(safe_path("./../../etc/passwd"))
