from ReadJsonFile import ReadJson
from UnionJsonFile import UnionJson
from WriteFIle import WriterJson, WriterXml



def main(students, rooms, format_in):

    students_dict = ReadJson().read_json(students)
    rooms_dict = ReadJson().read_json(rooms)
    dict_rums = UnionJson().result_dict(students_dict, rooms_dict)
    if format_in == 'json':
        WriterJson().write(dict_rums)
    elif format_in == 'xml':
        WriterXml().write(dict_rums)

    else:
        print('')


if __name__ == '__main__':
    rooms = "rooms.json"
    students = "students.json"
    format_in = "json"
    main(students, rooms, format_in)
