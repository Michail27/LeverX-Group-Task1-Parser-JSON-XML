from abc import ABC, abstractmethod


class AbstractUnion(ABC):
    @abstractmethod
    def result_dict(self, students_dict, rooms_dict):
        pass


class UnionJson(AbstractUnion):
    def result_dict(self, students_dict, rooms_dict):
        for room in rooms_dict:
            room['students'] = []
        dict_rooms = {room['id']: room for room in rooms_dict}
        for student in students_dict:
            student_room = student['room']
            student_dict = dict()
            student_dict['id'] = student['id']
            student_dict['name'] = student['name']
            dict_rooms[student_room]['students'].append(student_dict)
        return [i for i in dict_rooms.values()]
