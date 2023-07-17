from data import documents
from data import directories

class Command:


    def p(self):
        """Command p - return owner of document"""
        print('Input number of document')
        doc_num = input()
        for doc in documents:
            if doc_num == doc['number']:
                print(f'Owner {doc["name"]}')
                break
        else:
            print('Not found')

        #item.name for item in documents item.name if doc_num==item.number else 'Не найдено'


    def s(self):
        """Command s - return num of directories of document"""
        print('Input number of document')
        doc_num = input()
        for dir in directories:
            if doc_num in directories.get(dir):
                print(f'Directorie {dir}')
                break
        else:
            print('Not found')


    def l(self):
        """Command l - return information about each document"""
        for doc in documents:
            print(f'№: {doc["number"]}, type: {doc["type"]}, owner: {doc["name"]}', end='')
            for dir in directories:
                if doc["number"] in directories.get(dir):
                    print(f', directorie: {dir}')


    def ads(self):
        """Command ads - create a new directory"""
        """Without change records in file data.py"""
        print('Input number of directory')
        dir_num = input()
        if directories.get(dir_num) is None:
            directories[dir_num] = []
            self.print_cur_dir()
        else:
            print('Already exists', end='')
        print()



    def ds(self):
        """Command ds - delete a directory"""
        """Without change records in file data.py"""
        print('Input number of directory')
        dir_num = input()
        if directories.get(dir_num) is not None:
            if len(directories.get(dir_num)) > 0:
                print('That not empty')
            else:
                directories.pop(dir_num)
            self.print_cur_dir()
        else:
            print('That not exists', end='')
        print()


    def ad(self) -> None:
        """
        Collect new data in dict_input_data. Add data in db and print all current data after adding.
        """
        dict_input_data = {}
        query_name = {'type of document': 'type', 'owner': 'name', 'directory where save': 'directories'}
        a = True

        while a:
            print('Input num of document')
            user_input = input()
            if user_input in self.get_all_num_doc('number'):
                print('That number already exist')
            elif user_input=='exit':
                break
            else:
                dict_input_data['number'] = user_input
                a = False
        else:
            for q in query_name:
                print(f'Input {q}')
                user_input = input()
                dict_input_data[f'{query_name.get(q)}'] = user_input

        self.add_record_in_db(dict_input_data)
        self.print_all_data()


    def d(self):
        """
        Communicate with user for Delete document from db by number
        """
        user_input = input('Input num of document\n')

        if not self.delete_doc(user_input):
            print('Input num of document don\'t found')
        self.print_all_data()


    def m(self):
        """
        Change directory of keep for input number of document
        """
        all_docs = self.get_all_num_doc('number')
        all_dir = self.get_all_num_doc('directories')
        right_input = True

        while right_input:
            num_doc = input('Input num of document\n')
            if num_doc not in all_docs:
                print('Input num of document don\'t exist')
                continue
            right_input = False

        right_input = True
        while right_input:
            num_dir = input('Input num of directory\n')
            if num_dir not in all_dir:
                print('Input directory don\'t exist')
                continue
            right_input = False

        self.delete_doc_from_dir(num_doc)
        directories.get(num_dir).append(num_doc)
        self.print_all_data()


    def delete_doc(self, num:int) -> bool:
        """
        Execute delete doc and doc from dir
        """
        list_all_docs = self.get_all_num_doc('number')
        if num in list_all_docs:
            documents.pop(list_all_docs.index(num))
            if self.delete_doc_from_dir(num):
                return True
        return False


    def delete_doc_from_dir(self, num:int) -> bool:
        """
        Execute doc from dir
        """
        for dir in directories:
            if num in directories.get(dir):
                directories.get(dir).remove(num)
                return True
        return False

    def add_record_in_db(self, dict_input_data:dict):
        """
        Add new data in documents and in directories
        """
        documents.append(
            {
                'type': dict_input_data.get('type'),
                'number': dict_input_data.get('number'),
                'name': dict_input_data.get('name')
            }
        )

        if str(dict_input_data.get('directories')) in self.get_all_num_doc('directories'):
            list_from_dir = directories.get(str(dict_input_data.get('directories')))
            list_from_dir.append(dict_input_data.get('number'))
        else:
            directories[dict_input_data.get('directories')] = []
            directories[dict_input_data.get('directories')].append(dict_input_data.get('number'))
        print('Data is added successful')


    def get_all_num_doc(self, field_name:str) -> list:
        """
        Get list of all num documents
        """
        num_doc = []
        if field_name == 'directories':
            for item in directories:
                num_doc.append(item)
            #return num_doc
        else:
            for item in documents:
                num_doc.append(item[f'{field_name}'])
            #return num_doc
        return num_doc


    def print_cur_dir(self) -> None:
        """
        Print current directory
        """
        print('Current list of directories: ', end='')
        for item in directories:
            print(f'{item}, ', end='')

    def print_all_data(self) -> None:
        """
        Print all current data in readable view
        """
        for doc in documents:
            num_doc = doc.get('number')
            type_doc = doc.get('type')
            owner_doc = doc.get('owner')
            num_dir = self.get_dir_of_doc(num_doc)
            print(f'Num of documents: {num_doc}, type of doc: {type_doc}, owner of doc: {owner_doc}, keep directory: {num_dir}')


    def get_dir_of_doc(self, num_doc:str) -> str:
        """
        Return directory where keep num_doc
        """
        for dir in directories:
            if num_doc in directories.get(dir):
                return dir