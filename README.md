## VirtualBox VMS AUTOLAUNCHER:
Ce script vous permettra d'automatiser le démarrage de vos différentes machines virtuelles sans avoir à vous soucier du démarrage manuel de VirtualBox.

## Contenu:
* [Technologie](#Technologie)
* [Dépendance](#Dépendances)
* [Installation](#Installation)

## Technologie :
Verion du python:
- ### Python3

## Dépendance :
- `pywin32`
- `vboxapisetup.py(virtualbox SDK)`
- `VirtualBox 6.1.2+`

## Installation :

Pour executer le script:
```
$ pip install pywin32
$ python vboxapisetup.py install
$ python -m pip install virtualbox
$ python autolauncher.py
```
