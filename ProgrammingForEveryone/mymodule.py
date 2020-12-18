def code_for_module():
    print("I am  a function inside my module")


def main():
    print("this is the exmaple of main function")
    # code_for_module()


if __name__ == '__main__':  # function only run when it called from this sector
    main()  # In same file if any function not relation with this file then that file not execute
# else:
#     code_for_module()  # it can be import from any file but not above this
