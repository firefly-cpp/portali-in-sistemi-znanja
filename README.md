# Portali in sistemi znanja 2022/2023

Dodatno gradivo za predmet Portali in sistemi znanja

## Namestitev Pythona in IDE-ja 

### Windows
Možnosti za namestitev programskega jezika je zelo veliko, nekaj izmed njih vključuje:
* https://www.anaconda.com/ (Anaconda, vzpostavitev okolja je iz Anaconda Prompt enaka kot pri Linux, iz Anaconda s pomočjo GUI, glej [Podrobna navodila za Windows](./podrobna-navodila/README.md))
* https://www.python.org/downloads/windows/ (Samo Python - priporočena je zadnja verzija 3.x.x, trenutno je na voljo 3.10.6)
* PyCharm - JetBrains-ov IDE za Python 

Za uporabo JetBrains paketa je potrebna licenca. Pridobi se s pomočjo @student.um.si maila.
* https://account.jetbrains.com/licenses

Ob izbiri PyCharm-a se priporoča namestitev preko JetBrains ToolBox-a. Tako je lažje upravljati z večimi IDEji, licencami, posodobitvami, projekti...
* https://www.jetbrains.com/toolbox-app/ (namestitev IDE s pomočjo JetBrains ToolBox-a)
* https://www.jetbrains.com/pycharm/ (samo PyCharm IDE)

[Podrobna navodila za Windows](./podrobna-navodila/README.md)

## Namestitev okolja Miniconda

### Linux

#### 1. Pridobimo paket
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

#### 2. Zaženemo .sh datoteko
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```
## Vzpostavitev okolja

#### 1. Ustvarimo okolje conda
```bash
conda create -n portali python=3.10
```

#### 2. Aktiviramo ustvarjeno okolje
```bash
conda activate portali
```

#### 3. Namestitev paketov

```bash
(portali) repository_root$ python -m pip install -r requirements.txt
```

## Literatura

[1] Karakatič, Sašo, and Fister Jr., Iztok. "[Strojno učenje: s Pythonom do prvega klasifikatorja](https://press.um.si/index.php/ump/catalog/book/643)." (2022). Univerza v Mariboru, Univerzitetna založba.

[2] https://machinelearningmastery.com/

## Povezave do dokumentacije knjižnic

[1] [NiaPy](www.niapy.org)

[2] [scikit-learn](https://scikit-learn.org/stable/)

[3] [NiaAML](https://github.com/lukapecnik/NiaAML#readme)


Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Material in this folder is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
