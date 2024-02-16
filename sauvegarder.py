#!/usr/bin/env python3
import sys
import os


if __name__ == "__main__":
    # print(sys.argv)
    # bof control not really required.
    if len(sys.argv) < 4:
        print("il manque des arguments a l'appel")
        exit(1)

    polynomes_textes = list(filter(None, (sys.argv[3]).strip().split(';;')))

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
            my_file.write(block.replace(';', '\n'))

            if block != polynomes_textes[-1]:
                my_file.write('\n\n')

        my_file.close()
