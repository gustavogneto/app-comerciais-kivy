a=0
def func1():
    b =5
    def func2():
        nonlocal b #acessa b do escopo da func1
        #b = 10
        print(b)
    func2() ## executa func2
func1() #executa func1