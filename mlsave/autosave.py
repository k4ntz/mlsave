from os import makedirs
from os.path import exists, isdir
import pickle
from sys import modules as sysmodules
from termcolor import colored
from utils import increm
if "pandas" in sysmodules:
    from pandas import DataFrame


def _check_path(path):
    file_exists = False
    if exists(path):
        while exists(path):
            path = increm(path)
        file_exists = True
        msg = f"Path already used, will be saved as {path}"
        return path
    if path[-1] == '/':
        folders = path
    else:
        folders = '/'.join(path.split('/')[:-1])
    if not exists(folders):
        print(colored(f'Creating successive folders: {folders}', 'yellow',
                      attrs=['reverse']))
        makedirs(folders)
    return path


def autosave(object, path):
    path = _check_path(path)
    saved = False
    if "pandas" in sysmodules:
        print("FOUND PANDAS")
        if type(object) is DataFrame:
            if path[-4:] != ".csv":
                path += ".csv"
            object.to_csv(path)
            saved = True
    elif path[-4:] == ".pkl":
            pickle.dump(object, open(path, 'wb'))
            saved = True
    if not 'torch' in sysmodules:
        print("Torch detected")
    if not 'tensorflow' in sysmodules:
        print("TF detected")
    if saved:
        print(colored(f'File saved at {path}', 'green', attrs=['reverse']))
    else:
        path_with_auto = f"{path}_auto.pkl"
        msg = f"Could not save {path}\nSaved it anyway as {path_with_auto}"
        pickle.dump(object, open(path_with_auto, 'wb'))
        print(colored(msg, 'red', attrs=['reverse']))

if __name__ == '__main__':
    autosave(None, "coucou/toi/labas")
