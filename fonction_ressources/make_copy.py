import shutil

def make_copy_dir (path): return shutil.copytree(path, path+"_copy",dirs_exist_ok=True)
    