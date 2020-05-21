# Crate new python project

Simply creates new directory in your path with virtualenv and git

## Installation

```bash
git clone https://github.com/logotip4ik/Create-new-project-Python.git
```

## Usage

```bash
python3 create_proj.py your-project-name
```
### Options
``path`` - path to your new project

``-nv`` or ``--novenv`` - program wont create virtualenv

``-nf`` or ``--nofile`` - program wont create new file in specified directory

``-ng`` or ``--nogit`` - program wont create a git

``-na`` or ``--noactivation`` - program wont create a `.sh` file which can activate virualenv

``-in`` or ``--install`` - after this should go [Pypi](https://pypi.org/) packages

So you can use it like this:
```bash
python3 create_proj.py test ../test/test  -na -in colorama
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
