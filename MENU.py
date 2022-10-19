import os


class menu():
  def __init__(self, title):
    self.title = title
    self.items = [menu_item("Выйти", self._back)]
    self.back = False
    self.max_item_title_len = 0

  def add_item(self, item_title, func):
    if (self.max_item_title_len < len(item_title)):
      self.max_item_title_len = len(item_title)
    self.items.insert(
      len(self.items) - 1, 
      menu_item(item_title, func)
    )

  def _print_title(self):
    length = self.max_item_title_len + len(self.items) % 10 + 2
    left_margin = (length - len(self.title) - 10) / 2
    for i in range(int(left_margin)):
      print(' ', end='')
    print("--==", self.title, "==--")

  def _print_line(self, symbol):
    length = self.max_item_title_len + len(self.items) % 10 + 2
    title_len = len(self.title) + 10
    if (title_len > length):
      length = title_len
    for i in range(length):
      print(symbol, end='')
    print()

  def _print_items(self, items):
    for index, item in enumerate(items):
      print(index + 1, ": ", item, sep='')

  def _command_input(self):
    self._print_line("-")
    command = False
    try:
      command = int(input("Введите команду: ")) - 1
      if (command > len(self.items) or command < 0):
        print('\033[91m' + "Неизвестная команда." + '\033[0m')
        input()
        return False
    except:
      print('\033[93m' + "Пожалуйста введите номер команды." + '\033[0m')
      input()
    return command

  def _back(self):
    self.back = True

  def show(self):
    os.system("CLS")
    items = self.items
    while(True):
      self._print_title()
      self._print_line("=")
      self._print_items(items)
      command = self._command_input()
      if (not command and command != 0): continue
      item = self.items[command]
      item.run()
      os.system("CLS")
      if (self.back):
        return



class menu_item():
  def __init__(self, title, func):
    self.title = title
    self.func = func

  def __str__(self):
    return self.title

  def run(self):
    func = self.func
    if (type(func) is menu):
      func.show()
    else:
      func()
