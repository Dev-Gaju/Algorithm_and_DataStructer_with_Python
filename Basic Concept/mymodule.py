def code_for_module():
    print("I am  a function inside my module")


#without main function import could not possible to on class to another

def main():
    print("this is the exmaple of main function")
    # code_for_module()


if __name__ == '__main__':  # function only run when it called from this sector
    code_for_module()  # In same file if any function not relation with this file then that file not execute
else:
    main()  # it can be import from any file but not above this
