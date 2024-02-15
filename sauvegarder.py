#!/usr/bin/env python3
import sys
import os


if __name__ == "__main__":
    # bof control not really required.
    if len(sys.argv) < 4:
        print("il manque des arguments a l'appel")

    polynomes_textes = (sys.argv[3]).strip('[]')

    print(sys.argv[3])
    print(polynomes_textes)

    (folder_path, file_name) = (sys.argv[1], sys.argv[2])

    entire_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_path + file_name + '.polynome')

    if os.path.exists(entire_file_path):
        append_write_option = 'a+'  # append if already exists
    else:
        full_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_path)
        if not os.path.isdir(full_folder_path):
            os.mkdir(full_folder_path)
        append_write_option = 'w+'  # make a new file if not exists

    with open(entire_file_path, append_write_option) as my_file:
        for block in polynomes_textes:
            print(block)
            my_file.write(block.replace(r'\n', '\n'))
        my_file.close()
'''
for line in block.split('\n'):
    f.write(line)
f.write('\n')
f.close()
'''

