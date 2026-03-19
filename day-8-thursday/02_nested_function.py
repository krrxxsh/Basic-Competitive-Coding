def outerFunction():
    print("This is my outer Function")
    def innerFunction():
        print("this is the inner Function")
    innerFunction()

outerFunction() #execution starts from here