import xml_to_dict.xmltodict as xml_to_dict_


def get_xml_content(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        xml = xml_to_dict_.parse(f.read(), encoding='utf-8')
    return xml


def save_new_content_to_xml(file_name, xml_lines):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(xml_lines)


def replace_tabs_to_spaces(xml_lines):
    for i in range(len(xml_lines)):
        old_len = len(xml_lines[i])
        xml_lines[i] = xml_lines[i].lstrip()
        new_len = len(xml_lines[i])
        diff = old_len - new_len  # count of tabs in the start of a string
        xml_lines[i] = ' ' * diff * 2 + xml_lines[i]


def add_space_in_front_of_slash(xml_lines):
    for i in range(len(xml_lines)):
        xml_lines[i] = xml_lines[i].replace('/>', ' />')


def add_newline_char_to_end(xml_lines):
    # len(xml_lines) - 1 -- except the last line
    for i in range(len(xml_lines) - 1):
        xml_lines[i] += '\n'
