import os
import queue


def get_subdir(path):
    try:
        dirfiles = os.listdir(path)
    except PermissionError:
        return subdir_list

    subdir_list = []

    for each in dirfiles:
        full_name = path + "/" + each
        if os.path.isdir(full_name):
            subdir_list.append(full_name + "/")
    return subdir_list


dir_queue = queue.Queue()
dir_queue.put("/")

all_dirs=[]
while not dir_queue.empty():
    dir_name = dir_queue.get()
    all_dirs.append(dir_name)

    subdir_names = get_subdir(dir_name)
    for each in subdir_names:
        dir_queue.put(each)

print(all_dirs)