import os


def get_path(folder, file):
    file_path = os.path.join(folder, file)
    return file_path
