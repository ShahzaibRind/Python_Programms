def dec1(func1):
    def nowexec():
        print("Excuting")
        func1()
        print("Excuted")
        return nowexec()

@dec1
def who_is_harry():
    print("Shazzy is programmer")
who_is_harry()
# who_is_harry() = dec1(who_is_harry())
