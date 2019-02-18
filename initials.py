def get_initials(fullname):
    initials = ''
    for name in fullname.split():
        name = name.upper()
        initials += name[0] + ''
    return initials

def main():
    print(get_initials(input("Please Enter Your Full Name:")))
if __name__ == '__main__':
    main()

