from pathlib import Path
import os
import shutil


# # Создать тестовую папку
# folder_name = "test_folder"
# folder_path = os.path.join(os.getcwd(), folder_name)
# if os.path.exists(folder_path):
#     shutil.rmtree(folder_path)
# os.makedirs(folder_path)
#
# # Заполнить тестовую папку
# file_name = "test1.txt"
# file_path = os.path.join(folder_path, file_name)
# with open(file_path, "w") as file:
#     file.write("This is a test file.\n")
# file.close()

# def rename_files(directory="test_folder", desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc", **kwargs):
#     files_path = Path().cwd() / directory
#     count = 1
#     for obj in files_path.iterdir():
#         if obj.is_file() and str(obj).split(".")[-1] == source_ext:
#             new_obj = f'{desired_name}{str(count).zfill(num_digits)}.{target_ext}'
#             obj.rename(files_path / new_obj)
#             count += 1

def rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc"):
    files_path = Path().cwd() / "test_folder"
    count = 1
    for obj in files_path.iterdir():
        if obj.is_file() and str(obj).split(".")[-1] == source_ext:
            new_obj = f'{desired_name}{str(count).zfill(num_digits)}.{target_ext}'
            obj.rename(files_path / new_obj)
            count += 1


rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")
