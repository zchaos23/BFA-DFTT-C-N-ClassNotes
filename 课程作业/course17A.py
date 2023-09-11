import easygui
import keyword
import re
import sys
import builtins


all_builtin_methods = set()

for module_name in dir(builtins):
    module = getattr(builtins, module_name)
    if isinstance(module, type):
        all_builtin_methods.update(dir(module))

builtin_methods = sorted(all_builtin_methods)

builtin_functions = [name for name in dir(__builtins__) if callable(getattr(__builtins__, name))]

builtin_keywords = keyword.kwlist

keywords = builtin_methods + builtin_functions + builtin_keywords


def lower_to_upper(file):
    with open(file, 'r', encoding='utf-8') as f:
        source_code = f.read()
        lines = source_code.split('\n')
        replaced_lines = []

        for line in lines:
            words = re.split('(\W+)', line)
            replaced_word = []

            for word in words:
                if word.isidentifier() and word.lower() not in keywords:
                    replaced_word.append(word.upper())
                else:
                    replaced_word.append(word)

            replaced_lines.append(''.join(replaced_word))

        replaced_source = '\n'.join(replaced_lines)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(replaced_source)


if __name__ == "__main__":
    try:
        file = easygui.fileopenbox('选择 Python 文件', '', '', ['*.py'])
        lower_to_upper(file)

        input("Program finished, please press any key to exit.")
        sys.exit()

    except Exception as e:
        print("Error:", e)

        input("Program finished, please press any key to exit.")
        sys.exit()
