import argparse
import os

# TODO properly sourcing user's bash


class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'+'\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class CreateProject:
    def __init__(self, name, path, nogit, novenv, nofile, noactivate, install):
        self.name = name
        self.path = path
        self.nogit = nogit
        self.novenv = novenv
        self.nofile = nofile
        self.noactivate = noactivate
        self.install = install

        self.what_to_open = "gnome-terminal"  # < Change this to your(KDE - konsole)
        self.sh_script = f"source ../test/env/bin/activate && {self.what_to_open}"

        self.start()

    def novenv_(self):
        print(color.OKGREEN + "Creating virtualenv...")
        os.system(f"cd {os.getcwd() + '/' + self.path + self.name} && python3 -m venv env")

    def to_install(self):
        print(color.OKGREEN + "Installing packages..." + color.END)
        for i in range(len(self.install)):
            try:
                os.system(
                    f"source {os.getcwd() + '/' + self.path + self.name}/env/bin/activate && pip3 install "
                    f"{self.install[i]}")
            except:
                print(color.FAIL+color.BOLD+f"Could not install package: {self.install[i]}")

    def nogit_(self):
        print(color.OKGREEN + "Creating git in directory..." + color.END)
        os.system(f"cd {os.getcwd() + '/' + self.path + self.name} && git init")

    def nofile_(self):
        print(color.OKGREEN + "Creating main file..." + color.END)
        os.system(f"cd {os.getcwd() + '/' + self.path + self.name} && touch {self.name.lower().replace('-', '_')}.py")

    def noactivate_(self):
        print(color.OKGREEN + "Creating activation file..." + color.END)
        os.system(f'cd {os.getcwd() + "/" + self.path + self.name}; touch actv.sh; echo "{self.sh_script}" > '
                  f'actv.sh; chmod +x actv.sh')

    def start(self):
        try:
            os.mkdir(os.getcwd() + "/" + self.path + self.name)
        except FileExistsError:
            raise Exception(color.BOLD + color.FAIL + "Directory already exists!" + color.END)
        print(color.OKGREEN + "Created directory!" + color.END)
        if not self.novenv:
            self.novenv_()
        elif self.novenv:
            print(color.OKGREEN + "Skipping creating venv..." + color.END)
        if self.install is not None:
            self.to_install()
        elif self.install is None:
            print(color.OKGREEN + "Skipping installation of packages..." + color.END)
        if not self.nogit:
            self.nogit_()
        elif self.nogit:
            print(color.OKGREEN + "Skipping initialisation of git..." + color.END)
        if not self.nofile:
            self.nofile_()
        elif self.nofile:
            print(color.OKGREEN + "Skipping creating main file..." + color.END)
        if not self.noactivate:
            self.noactivate_()
        elif self.noactivate:
            print(color.OKGREEN + "Skipping creating activation file...")
        if self.noactivate:
            print(color.OKGREEN + "Skipping activating env..." + color.END)
        elif self.novenv:
            print(color.WARNING + "Skipping activating env..." + color.END)
        elif not self.noactivate and self.novenv:
            print(color.WARNING + "Skipping activating, because you didn't supply proper flag..." + color.END)
        elif not self.noactivate and not self.novenv:
            print(color.OKGREEN + "Activating env..." + color.END)
            os.system(self.sh_script)
        else:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creates new directory and venv in it", allow_abbrev=False)
    parser.add_argument("name", type=str, help="Names your directory")
    parser.add_argument("path", type=str, default='./', nargs='?', help="Path to your project, default is ./")
    parser.add_argument("-nv", "--novenv", action="store_true", help="Do not create venv")
    parser.add_argument("-nf", "--nofile", action="store_true", help="Do not create main file")
    parser.add_argument("-ng", "--nogit", action="store_true", help="Do not create git")
    parser.add_argument("-na", "--noactivate", action="store_true", help="Do not create an activation .sh file")
    parser.add_argument("-in", "--install", type=str, nargs="+", help="Pip installs in venv what you enter")
    args = parser.parse_known_args()[0]
    if args.novenv and args.install is not None:
        raise Exception(color.FAIL + color.BOLD + "You process to install some packages, "
                                                  "but no venv would be created!" + color.END)
    else:
        project = CreateProject(args.name, args.path, args.nogit, args.novenv, args.nofile, args.noactivate,
                                args.install)
