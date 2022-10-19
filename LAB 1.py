import psutil
import os

from MENU import menu
from FILE_MANAGER import (file_manager, zip_manager, FILE_TYPE)


def print_disk_info():
  for part in psutil.disk_partitions(all=False):
    if os.name == 'nt':
      if 'cdrom' in part.opts or part.fstype == '':
        continue

    usage = psutil.disk_usage(part.mountpoint)

    print()
    print("Диски:", part.device)
    print("Объём:", usage.total)
    print("Тип файловой системы:", part.fstype)
    print("Метка тома:", part.mountpoint)
    input()


def text_menu():
  text_menu = menu("Текстовый файл")

  txt = file_manager(FILE_TYPE.TXT)

  text_menu.add_item("Создать", txt.create)
  text_menu.add_item("Запись в файл", txt.write)
  text_menu.add_item("Прочесть файл", txt.read)
  text_menu.add_item("Удалить", txt.delete)

  return text_menu


def json_menu():
  json_menu = menu("JSON файл")

  json = file_manager(FILE_TYPE.JSON)

  json_menu.add_item("Создать", json.create)
  json_menu.add_item("Записать JSON", json.write)
  json_menu.add_item("Прочесть JSON", json.read)
  json_menu.add_item("Удалить", json.delete)

  return json_menu

def xml_menu():
  xml_menu = menu("XML файл")

  xml = file_manager(FILE_TYPE.XML)

  xml_menu.add_item("Создать", xml.create)
  xml_menu.add_item("Записать XML", xml.write)
  xml_menu.add_item("Прочесть XML", xml.read)
  xml_menu.add_item("Удалить", xml.delete)

  return xml_menu


def zip_menu():
  zip_menu = menu("ZIP файл")

  zip = zip_manager()
  
  zip_menu.add_item("Создать", zip.create_zip)
  zip_menu.add_item("Добавить файл в архив", zip.add_file_to_zip)
  zip_menu.add_item("Открыть файл из архива", zip.get_file_from_zip)
  zip_menu.add_item("Удалить", zip.delete)

  return zip_menu


def main_menu():
  main_menu = menu("Главное меню")

  main_menu.add_item("Информация о логических дисках", print_disk_info)
  main_menu.add_item("Работа с файлами", text_menu())
  main_menu.add_item("Работа с форматом JSON", json_menu())
  main_menu.add_item("Работа с форматом XML", xml_menu())
  main_menu.add_item("Работа с архивом ZIP", zip_menu())

  return main_menu


def main():
  menu = main_menu()
  menu.show()

if __name__ == "__main__":
  main()


