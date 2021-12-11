import argparse

from read_json_file import JsonLoad
from union_json_file import JsonUnion
from write_fIle import JsonWriter, XmlWriter


def args_parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument('students_path', type=str, help='Path students file.')
    parser.add_argument('rooms_path', type=str, help='Path rooms file.')
    parser.add_argument('out_format', type=str, help='Source file format(json/xml).')
    args = parser.parse_args()
    return args


def main():
    args = args_parsing()
    rooms = args.rooms_path
    students = args.students_path
    format_out = args.out_format

    students_dict = JsonLoad().load_json(students)
    rooms_dict = JsonLoad().load_json(rooms)
    dict_rums = JsonUnion().get_result_dict(students_dict, rooms_dict)
    if format_out == 'json':
        JsonWriter().write(dict_rums)
    elif format_out == 'xml':
        XmlWriter().write(dict_rums)
    else:
        raise ValueError('This format is not supported')


if __name__ == '__main__':
    main()
