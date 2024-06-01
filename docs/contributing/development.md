# Developer Guide

If you would like to modify/submit a PR for **3dchameleon-klipper**, follow these steps to set up a development environment.

**NOTE that these commands are designed for Mac/Linux and may need to be slightly modified for Windows**

## `main` and `dev`

### Clone the repository

Run in the terminal of your local computer:
```
git clone https://github.com/3dcoded/3dchameleon-klipper
cd 3dchameleon-klipper
```

Next, if using `dev`, run:
```
git checkout dev
```

## `docs`

### Clone the repository

Run in the terminal of your local computer:
```
git clone https://github.com/3dcoded/3dchameleon-klipper
cd 3dchameleon-klipper
git checkout docs
```

### Pipenv

`docs` uses pipenv as a package manager. Run the following in your terminal:
```
pip3 install pipenv
pipenv install
```

### Run webserver

Run in your terminal:
```
pipenv shell
mkdocs serve
```
