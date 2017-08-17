def translate(arr):
    return_arr=[]
    for tem in arr:
        return_arr.append(str(tem)+'t')
    return return_arr

def something():
    temperatures=[10,-20,-289,100]
    temperatures=translate(temperatures)

    for tem in temperatures:
        print(tem)

class test:
    def __init__(self,value=0,commit=''):
        self.value = value
        self.commit = commit
    def get_value(self):
        return self.value
    def set_value(v):
        self.value = v
    def get_commit(self):
        return self.commit
    def set_commit(c):
        self.commit = c

if __name__=='__main__':
    tl = [test(),test(commit='Dude'),test(value=87),test(17,'Love')]
    for t_i in tl:
        print(t_i.value)
        print(t_i.commit)
        #print(type(t_i.get_value()))
        #print(t_i.get_value())
        #print(t_i.get_commit())
    for t_i in tl:
        print(t_i.get_value())
        print(t_i.get_commit())
