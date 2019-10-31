import os
import subprocess as sp
import activ


def main():
    global name, address
    name = input("Enter name of new project:  ")
    address = input('Enter path to new project:  ')
    try:
        name = name.replace(' ', '_')
        if '\\' in address:
            pass
    except:
        address = input("Your input was wrong\nEnter another one:  ")
    try:
        os.mkdir(f'{address}\\{name}')
        print("Creating folder")
        virtualenv()
    except:
        print("This folder is already exists\nCreating virtual environment")
        os.system(f"cd {address}\\{name} & python -m venv {name}_env")
        y_n = input("Do you want to activate python(Y, N)?  ")
        if y_n == 'Y' or 'y':
            activate()
        elif y_n == 'N' or 'n':
            exit()


def virtualenv():
    global address, name
    print('Creating virtual environment\nThis could take few seconds')
    os.system(f"cd {address}\\{name} & python -m venv {name}_env")
    y_n = input("Do you want to activate python and create .py file(Y, N)?  ")
    if y_n == 'Y' or 'y':
        activate()
    else:
        exit()


def create_file_py():
    global name, address
    print('Creating python file')
    os.system(f'cd {address}\\{name} & copy nul "{name}.py"')
    os.system(f"subl {address}\\{name}")
    os.system('exit')
    activ.activ(f'{address}\\{name}')


def activate():
    global name, address
    sp.call(f'cd {address}\\{name}\\ & start {address}\\{name}\\{name}_env\\Scripts\\activate.bat',
            shell=True)
    create_file_py()


if __name__ == '__main__':
    main()
