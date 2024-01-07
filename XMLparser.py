import re
import os
from fnmatch import fnmatch
import PySimpleGUI as sg

def find_files(directory, pattern):
    files = []
    for root, dirs, filenames in os.walk(directory):
        for filename in [f for f in filenames if fnmatch(f, pattern)]:
            files.append(os.path.join(root, filename))
    return files

def parse_files(directory_path,  file_pattern = '*island*.xml', size = 400):
    result = find_files(directory_path, file_pattern)
    if len(result) == 0:
        sg.popup('Exception:', 'Wrong path or incorrect additional params!')
        return
    try:
        for file_path in result:
            with open(file_path, "r", encoding="utf-8") as file:
                xml_data = file.read()

            start_index = xml_data.find("<edit_areas>")
            end_index = xml_data.find("</edit_areas>", start_index)

            if start_index != -1 and end_index != -1:
                edit_areas_block = xml_data[start_index:end_index + len("</edit_areas>")]
                replacement = f'<size x="{size}" y="{size}" z="{size}"/>'
                modified_edit_areas_block = re.sub(r'<size x="[^"]+" y="[^"]+" z="[^"]+"\/>', rf'{replacement}', edit_areas_block, flags=re.DOTALL)
                replacement = r'grid_size="0"'
                modified_edit_areas_block = re.sub(r'grid_size="[^"]+"', rf'{replacement}', modified_edit_areas_block, flags=re.DOTALL)
                modified_xml_data = xml_data[:start_index] + modified_edit_areas_block + xml_data[end_index + len("</edit_areas>"):]

                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(modified_xml_data)
                fileName = file_path.split("\\")[-1]
                print(f'File {fileName} has been modified.')
            else:
                pass
        sg.popup('Notifiaction:', 'Files parsed!')
    except:
        sg.popup('Exception:', 'Broken files')

def read_file():
    try:
        with open(f"{os.getenv('APPDATA')}\\xml_parser\\xml_parser.cfg", "r+", encoding="utf-8") as cfg_file:
            return cfg_file.read()
    except:
        print("read_exception")
        return ""

def change_file(content):
    if not os.path.exists(f"{os.getenv('APPDATA')}\\xml_parser"):
        os.makedirs(f"{os.getenv('APPDATA')}\\xml_parser")

    with open(f"{os.getenv('APPDATA')}\\xml_parser\\xml_parser.cfg", "a+", encoding="utf-8") as cfg_file:
        cfg_file.truncate(0);cfg_file.seek(0)
        cfg_file.write(content)

def window():
    sg.theme('DarkAmber')

    layout = [  [sg.Text('Path to tiles folder:')],
                [sg.InputText(read_file())],
                [sg.Text("Size:")],
                [sg.InputText("400")],
                [sg.Text("Additional params (not to use if you don't know):")],
                [sg.InputText()],
                [sg.Button('Parse'), sg.Button('Exit')] 
            ]

    window = sg.Window('xml parser', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Parse":
            if os.path.exists(values[0]) and len(values[0].split(".")) <= 2 and values[0] != ".":
                change_file(values[0])
                if values[2] != "":
                    parse_files(values[0], file_pattern = values[2], size = values[1])
                else:
                    parse_files(values[0], size = values[1])
            else:
                sg.popup('Exception:', 'Please enter correct path to tiles folder!')
    window.close()

if __name__ == "__main__":
    window()
