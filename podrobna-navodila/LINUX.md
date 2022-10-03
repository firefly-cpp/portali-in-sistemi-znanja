# Podrobnejša navodila za namestitev Pythona oziroma orodij za delo z njim na Linux OS

## Pure Python

## Anaconda ali Miniconda

## NeuroFedora: Free software for Free neuroscience

<p align="center">
  <img width="200" src="https://docs.fedoraproject.org/en-US/neurofedora/_images/NeuroFedoraLogo01.png">
</p>

- Veliko orodij za predmet je že obstoječih tudi v distribuciji NeuroFedora
- Povezava: https://docs.fedoraproject.org/en-US/neurofedora/install-media/
- Celotno okolje je lahko vzpostavljeno v približno 30 minutah
- Dodatne pakete lahko namestimo z enostavnim ukazom dnf install

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

