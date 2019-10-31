import os


def activ(address):
    print('Creating activate file')
    os.system(f'cd {os.getcwd()} & pyinstaller -y -F activate.py')
    print('Removing useless directories')
    os.system(f'cd {os.getcwd()} & rmdir /Q /S build')
    os.system(f'move "{os.getcwd()}\\dist\\activate.exe" "{address}\\"')
    os.system(f'cd {os.getcwd()} & del /f activate.spec')
    os.system(f"cd {os.getcwd()} & rmdir dist")


if __name__ == '__main__':
    user_inp = input("Do you want to create file that will activate the virtual environment(Y or N)")
    if user_inp == 'Y' or 'y':
        activ(os.getcwd())
    else:
        exit()
