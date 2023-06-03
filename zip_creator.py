import zipfile
import pathlib

def make_archive(filepaths, dest_dir, zip_name):
    directory = pathlib.Path(dest_dir, zip_name)
    
    with zipfile.ZipFile(directory, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname = filepath.name)
    
