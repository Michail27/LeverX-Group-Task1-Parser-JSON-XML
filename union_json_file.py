from abc import ABC, abstractmethod


class AbstractUnion(ABC):
    @abstractmethod
    def get_result_dict(self, students_dict, rooms_dict):
        pass


class JsonUnion(AbstractUnion):
    def get_result_dict(self, students_dict, rooms_dict):
        dict_rooms = dict()
        for room in rooms_dict:
            room['students'] = []
            dict_rooms[room['id']] = room
        for student in students_dict:
            dict_rooms[student['room']]['students'].append({'id': student['id'], 'name': student['name']})
        return [*dict_rooms.values()]
