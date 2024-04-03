def merge_files(file_list, output_filename):
    files_content = []
    for file_name in file_list:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            files_content.append((file_name, len(lines), lines))
    files_content.sort(key=lambda x: x[1])

    with open(output_filename, 'w', encoding='utf-8') as output_file:
        for file_name, lines_count, lines in files_content:
            output_file.write(f'{file_name}\n{lines_count}\n')
            output_file.writelines(lines)
            output_file.write('\n')


# Пример списка файлов для объединения
file_list = ['1.txt', '2.txt']
merge_files(file_list, 'merged_file.txt')
