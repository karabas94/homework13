"""
1. Инициализация класса с одним параметром - имя директории.

2. Написать метод класса, который создает атрибут класса в ввиде словаря
{'filenames': [список файлов в папке], 'dirnames': [список всех подпапок в папке]}.
Подпапки учитывать только первого уровня вложения. Папка в папке в папке - такое не брать ))
{'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}

2. Написать метод класса, которая получает булевое значение (True/False).
Функция возвращает тот же словарь, но с отсортированными именами файлов и папок в соответствующих списках.
Булевое значение True означает, что порядок сортировки алфавитный, False - обратный порядок.

3. Написать метод класса, которая получает строку, которая может быть
или именем файла, или именем папки. (В имени файла должна быть точка).
В зависимости от того, что функция получила (имя файла или имя папки) - записать его
в соответствующий список и вернуть обновленный словарь.

4* (*сдавать не обязательно, но если будете сдавать, то ошибки будут учитываться тоже).
Написать метод класса, которая получает имя директори и словарь по примеру из задания 1.
Функция проверяет соответствие полученного словаря и реальной файловой системы в полученной папке и,
если надо, создает нужные папки и пустые файлы, в соответствии со структурой словаря.
Пример:
создали на основании данных в папке -> {'filenames': [файл1, файл2, файл7], 'dirnames': [папка1, папка2]}
передали в метод -> {'filenames': [файл1, файл7, файл13], 'dirnames': [папка11, папка2]}
в результате необходимо создать файл13 и папка11
"""
import os


class Folder:

    def __init__(self, dirname: str):
        """
        Initial class with parameter name of folder
        """
        self.dirname = dirname

    def my_dict(self):
        """
        Create dictionary with attribute for names of files and names of folder incide initial folder
        """
        dictionary = {}.fromkeys(["filenames", "dirnames"])
        filenames = []
        dirnames = []
        for elements in os.listdir(self.dirname):
            if not os.path.isdir(os.path.join(self.dirname, elements)):
                filenames.append(elements)
            else:
                dirnames.append(elements)
        dictionary["filenames"] = filenames
        dictionary["dirnames"] = dirnames
        return dictionary

    def sort_dict(self, bo_ol: bool):
        """
        Sorted dictionary by bool parameter
        """
        new_dict = {}
        val_lists = self.my_dict().values()
        for val_list in val_lists:
            val_list.sort(reverse=bo_ol)
            for key, value in self.my_dict().items():
                if value == val_list:
                    new_dict[key] = value
        return new_dict

    def new_dict(self, name: str):
        """
        Created new dictionary with new file or new folder
        """
        new_dict = self.my_dict()
        new_file = self.my_dict()["filenames"]
        new_folder = self.my_dict()["filenames"]
        if "." in name:
            new_file.append(name)
        else:
            new_folder.append(name)
        new_dict["filenames"] = new_file
        new_dict["dirnames"] = new_folder
        return new_dict


obj = Folder("test")
print(obj.my_dict())
print(obj.sort_dict(False))
print(obj.new_dict("tt.txt"))
