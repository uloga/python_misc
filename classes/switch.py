#simple switch class

class Switch:
    def __init__(self, case=None):
        self.case = case

    def __iter__(self):
        yield self.match #yield match once 
        raise StopIteration

    def match(self, *args):
        if self.case in args: 
            return True
        else:
            return False

def main():

    value = 'three'
    for case in Switch(value):
        if case('one'):
            print('this is first')
            break
        if case('two'):
            print('this is second')
            break
        if case('three'):
            print('this is third')
            break
        if case('four'):
            print('tis is fourth')
            break
        else: 
            print("This is a default")


if __name__ == '__main__': main()
