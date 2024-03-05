import os, shutil

def get_folder_name(folder_path):
    files = os.listdir(folder_path)
    return files
def rename_mp4_jpg(folder_path):
    jpg = []
    mp4 = []
    files = os.listdir(folder_path)
    for i in range(len(files)):
        if files[i].endswith('.jpg'):
            jpg.append(files[i])
        if files[i].endswith('.mp4'):
            mp4.append(files[i])
    for idx, file in enumerate(jpg, 1):
        new_name = f"{idx:03}.jpg"
        old_file = os.path.join(folder_path, file)
        new_file = os.path.join(folder_path, new_name)
        os.rename(old_file, new_file)
        print(f"Renamed {file} to {new_name}")

    for idx, file in enumerate(mp4, 1):
        new_name = f"{idx:03}.mp4"
        old_file = os.path.join(folder_path, file)
        new_file = os.path.join(folder_path, new_name)
        os.rename(old_file, new_file)
        print(f"Renamed {file} to {new_name}")

    p_directory = os.path.join(folder_path, 'P')
    v_directory = os.path.join(folder_path, 'V')

    if not os.path.exists(p_directory):
        os.makedirs(p_directory)
    if not os.path.exists(v_directory):
        os.makedirs(v_directory)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg'):
            shutil.move(os.path.join(folder_path, filename), p_directory)
        elif filename.lower().endswith('.mp4'):
            shutil.move(os.path.join(folder_path, filename), v_directory)

def rename_files(folder_path, file_type):

    jpg = []
    mp4 = []

    files = os.listdir(folder_path)
    files.sort()
    for i in range(len(files)):
        if files[i].endswith('.jpg'):
            jpg.append(files[i])
        if files[i].endswith('.mp4'):
            mp4.append(files[i])
        
    for idx, file in enumerate(files, 1):
        new_name = f"{idx:03}{file_type}"
        old_file = os.path.join(folder_path, file)
        new_file = os.path.join(folder_path, new_name)
        os.rename(old_file, new_file)
        print(f"Renamed {file} to {new_name}")

# 使用函数
folder_path = ''  # 替换成你的文件夹路径
file_type = ''  # 替换成你想要重命名的文件类型# .jpg/ .mp4
rename_files(folder_path, file_type)