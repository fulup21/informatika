[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/EaI1U_WD)
# Naprogramujte wrapper

Budeme vylepšovat kalkulačku, která umí *jen* počítat. **Ale** nebudeme to dělat tím, že bychom modifikovali zdrojový kód kalkulačky, nýbrž obalováním kalkulačky novými vrstvami.

# Krok 1.

Naprogramujte wrapper, který bude:

- implementovat: `AbstractKalkulator`
- v konstruktoru brát argument typu `AbstractKalkulator`, který uloží do fieldu/pole `self._kalkulator`
- musíte implementovat všechny metody `AbstractKalkulator`:
  - jednoduše se jen provolejte skrz `self._kalkulator` na skutečnou implementaci
- úpravou v `main.py` ověřte že to funguje, kulkulačku koonstruujte takto:

```
kalkulator : AbstractKalkulator = KalkulatorWrapper(Kalkulator())
```

## Krok 2.

Naprogramujte tři různé wrappery.

### Wrapper 1. - logování
- nejjednodušší
- jenom pomocí print vypiště co se provádí za operaci
- následně delegujte na delegáta
- před vrácením výsledku vypište jaký je výsledek
- ověřte úpravou `main.py`

### Wrapper 2. - historie operací
- složitější
- v tomto wrapperu budete potřebovat držet historii prováděných operací (nejlépe jako seznam)
- při každé zavolené operaci si uložíte:
  - jaká operace byla volaná
  - jaké byly operandy
  - jaký byl vrácený výsledek
- uděláte navíc metodu, která vám vrátí uloženou historii operací
- ověřte úpravou `main.py`
- jde o **stavový wrapper**

### Wrapper 3. - cache
- nejsložitější
- v tomto wrapperu budete potřebovat držet cache prováděných operací (nejlépe jako mapu)
- při každé zavolené operaci:
  - podíváte se do cache, zda jste již dříve tuto operaci pro tyto operandy spočítali
  - pokud ano, vrátíte výsledek z cache
  - pokud ne, provoláte delegáta, výsledek operace do cache uložíte a pak ho vrátíte
- ověřte úpravou `main.py`
- jde o **stavový wrapper**

## Bonus :)

Slepte wrappery tak, aby kalkulačka uměla vše, co jste vytvořili: logování, historie operací, cachování (a počítat samozřejmě).
- vrchní vrstva: historie operací
- vrstva pod historií operací: cache
- vrstva pod cachí: logování
- vrstva pod logováním: kalkulačka

Ověřte úpravou `main.py`.
