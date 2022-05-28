import os

PATH = os.getcwd()
directories = list(filter(os.path.isdir, os.listdir(PATH)))
FILE_NAME = 'text.txt'

for directory in directories:
    if directory == 'txt_for_v.3':
        path_to_files = os.path.join(PATH, directory)
        files = os.listdir(path_to_files)
        all_files = {}
        for file in files:
            path_to_file = os.path.join(path_to_files, file)
            with open(path_to_file, encoding='utf-8') as text:
                all_files[file] = text.readlines()
        sorted_files = sorted(all_files, key=lambda x: len(all_files[x]))
        for file in sorted_files:
            with open('text.txt', 'a') as new_text:
                new_text.write(file + '\n')
                new_text.write(str(len(all_files[file])) + '\n')
                new_text.writelines(all_files[file] + ['\n'])
    else:
        print("Can not find the folder txt_for_v.3 with files")