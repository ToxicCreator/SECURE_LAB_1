import os
import json
import zipfile
import xml.etree.ElementTree as ET


class FILE_TYPE:
  TXT = "txt"
  XML = "xml"
  ZIP = "zip"
  JSON = "json"


class person_object():
  def __init__(self, id, name, phone):
    self.id = id
    self.name = name
    self.phone = phone

def create_person_object():
  id = input("id = ")
  name = input("name = ")
  phone = input("phone = ")

  return person_object(id, name, phone)


class file_manager:
  _filename_error = "Некорректное имя файла."
  
  def __init__(self, file_type):
    self.file_type = file_type

  def _file_name_input(self, text="Введите имя файла: "):
    file_name = input(text)
    return file_name + "." + self.file_type

  def _open_file(self, flag, path=False):
    try:
      if (not path):
        path = self._file_name_input()
      return open(path, flag)
    except:
      print(self._filename_error)
      input()
    return False

  def _write_json(self, file):
    person = create_person_object()
    file.write(json.dumps(person.__dict__))

  def _write_xml(self, file):
    person = create_person_object()
    data = ET.Element("person")

    id_element = ET.SubElement(data, "id")
    id_element.text = person.id

    name_element = ET.SubElement(data, "name")
    name_element.text = person.name

    phone_element = ET.SubElement(data, "name")
    phone_element.text = person.phone

    file.write(ET.tostring(data).decode())

  def create(self):
    file = self._open_file("w+")
    if (not file): return
    file.close()

  def write(self):
    file = self._open_file("w+")
    if (not file): return
    if (self.file_type == FILE_TYPE.JSON):
      self._write_json(file)
    elif (self.file_type == FILE_TYPE.XML):
      self._write_xml(file)
    else:
      file.write(input("Введите текст: "))
    file.close()

  def read(self):
    file = self._open_file("r")
    if (not file): return
    print(file.read())
    file.close()
    input()

  def delete(self):
    try:
      os.remove(self._file_name_input())
    except:
      print(self._filename_error)



class zip_manager(file_manager):
  def __init__(self):
    super().__init__(FILE_TYPE.ZIP)

  def _open_zip(self, flag):
    try:
      return zipfile.ZipFile(
        self._file_name_input("Введите имя архива: "), 
        flag
      )
    except:
      print(self._filename_error)
      input()
    return False

  def create_zip(self):
    file = self._open_zip("w")
    file.close()

  def add_file_to_zip(self):
    file = self._open_zip("a")
    path = input("Введите имя файла целиком: ")
    try:
      file.write(path, os.path.basename(path))
    except:
      print(self._filename_error)
      input()
    file.close()

  def get_file_from_zip(self):
    archive = self._open_zip("r")

    filename = input("Введите имя файла целиком: ")
    try:
      data = archive.read(filename)
    except:
      print(self._filename_error)
      archive.close()
      input()
      return
    archive.close()
      
    file = self._open_file("w+b", filename)
    file.write(data)
    file.close()

    print("Размер:", os.path.getsize(filename))
    print("Дата изменения:", os.path.getmtime(filename))
    input()