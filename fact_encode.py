
# reading all fact files under the directory, then store all string to a map from string to id
# then output the map to a file, use the id to replace the string in the fact files and output the new fact files
# in output directory

import os
import sys
import json


def read_fact_file(file_path, output_dir, string_to_id, string_count):
    new_count = string_count
    with open(file_path, 'r') as f:
        with open(os.path.join(output_dir, os.path.basename(file_path)), 'w+') as out:
            for line in f:
                line = line.strip()
                if len(line) == 0:
                    continue
                if line[0] == '#':
                    continue
                parts = line.split('\t')
                new_parts = []
                for part in parts:
                    if part not in string_to_id:
                        string_to_id[part] = new_count
                        new_count += 1
                    new_parts.append(str(string_to_id[part]))
                out.write('\t'.join(new_parts) + '\n')
    return new_count


def main():
    if len(sys.argv) != 3:
        print('Usage: python fact_encode.py fact_dir output_dir')
        return
    fact_dir = sys.argv[1]
    output_dir = sys.argv[2]
    string_to_id = {}
    string_count = 0
    for root, dirs, files in os.walk(fact_dir):
        for file in files:
            if file.endswith('.facts'):
                string_count = read_fact_file(os.path.join(root, file),
                                              output_dir, string_to_id, string_count)
    with open('string_to_id.json', 'w+') as f:
        json.dump(string_to_id, f)


if __name__ == '__main__':
    main()
