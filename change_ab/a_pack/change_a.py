import os

# заменяет все символы а на строку s и перезаписывает файл
def change_a(s: str) -> None:
    in_dir = './'
    ext = '.txt'
    txt_files = sorted(filter(lambda name: name.endswith(ext), next(os.walk(in_dir))[2]))

    for name_file in txt_files:
        path_file = os.path.join(in_dir, name_file)
        with open(path_file, 'r') as f:
            data = f.read()
        data = data.replace("a", s)
        with open(path_file, 'w') as f:
            f.write(data)
    return


if __name__ == '__main__':
    change_a('Russia')