import sys

cislo = sys.argv
total = 0
#print(cislo)
pocetcisel = 0

for e in cislo:
    try:
        #print(e)
        total += int(e)
        pocetcisel = pocetcisel + 1
    except:
        print(f' {e} neni cele cislo!!!!!')


print(f'Prumer je {total/pocetcisel}')