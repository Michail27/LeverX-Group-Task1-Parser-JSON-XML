from read_json_file import JsonLoad
from union_json_file import JsonUnion
from write_fIle import JsonWriter, XmlWriter


def main(students, rooms, format_out):

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
    rooms = "rooms.json"
    students = "students.json"
    format_out = "json"
    main(students, rooms, format_out)
