import os,time


class Parser:

    def __init__(self):
        self.list_out=[]

    def collect_tests(self):
        os.system('python -m pytest --collect-only -qq >list_tests.txt')
        time.sleep(2)
        with open("list_tests.txt") as file:
            for string in file:
                if 'no tests ran' not in string:
                    self.list_out.append(string.replace('\n',''))
            self.list_out.remove('')
        os.remove("list_tests.txt")
        return self.list_out







