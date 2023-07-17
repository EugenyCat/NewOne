from commands.Command import Command


class Console:

    def __init__(self):
        com = Command()
        self.__commands = [
            com.p,
            com.s,
            com.l,
            com.ads,
            com.ds,
            com.ad,
            com.d,
            com.m
        ]


    def communicate(self):

        while True:
            print('Input command')
            command = input()
            if command == 'exit':
                break
            for item in self.__commands:
                if command == item.__name__:
                    item()
                    break
            else:
                print('Unknown command')
