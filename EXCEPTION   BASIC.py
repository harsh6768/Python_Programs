def main():
    try:
        n1,n2=eval(input("enter two no seprated by comma:"))
        res=n1/n2
        print("results is",res)
    except ZeroDivisionError:
        print("division by zero")
    except SyntaxError:
        print("comma missing in input")
    except:
        print("something wrong in input")
    else:
        print("no exceptions")
    finally:
        print("final clause is executed")
main()