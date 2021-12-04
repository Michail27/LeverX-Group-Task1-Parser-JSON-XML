import json
from abc import ABC, abstractmethod
from xml.dom.minidom import parseString

from dicttoxml import dicttoxml


class AbstractWriter(ABC):
    @abstractmethod
    def write(self, dict_rums):
        pass


class WriterJson(AbstractWriter):
    def write(self, dict_rums):
        with open('answer.json', 'w') as f:
            f.write(json.dumps(dict_rums, indent=6))


class WriterXml(AbstractWriter):
    def write(self, dict_rums):
        xml_doc = dicttoxml(dict_rums, custom_root='Rooms', attr_type=False).decode('utf-8')
        pars_xml = parseString(xml_doc)
        with open("answer.xml", "w") as f:
            pars_xml.writexml(f, indent='\n', addindent='\t')
