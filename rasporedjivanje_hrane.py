import os

def prikazi_tabelu(podaci):
    print("\n#Br.Narudžbe | T-Dolaska | T-Pripreme | T-Kompletiranja | Ukupno-TAT | T-Čekanja")
    print("-" * 85)
    ukupni_tat = 0
    ukupno_cekanje = 0
    for p in podaci:
        print(f"{p['id']:<12} | {p['at']:<9} | {p['bt']:<10} | {p['ct']:<14} | {p['tat']:<10} | {p['wt']}")
        ukupni_tat = ukupni_tat + p['tat']
        ukupno_cekanje = ukupno_cekanje + p['wt']
    print("-" * 85)
    n = len(podaci)
    print(f"Prosječno vrijeme čekanja = {ukupno_cekanje / n:.2f} (min)")
    print(f"Prosječno ukupno vrijeme izvršavanja (TAT) = {ukupni_tat / n:.2f} (min)")
    input("\nPress any key to continue...")



def sjf_non_preemptive():
    n = int(input("Unesite ukupan broj narudžbi: "))
    procesi = []
    for i in range(n):
        at = int(input(f"Vrijeme dolaska narudžbe {i+1}: "))
        bt = int(input(f"Vrijeme pripreme narudžbe {i+1}: "))
        procesi.append({'id': i+1, 'at': at, 'bt': bt, 'zavrsen': False})
    vrijeme = 0
    zavrseni = 0
    rezultati = []
    while zavrseni < n:
        kandidati = []
        for p in procesi:
            if p['at'] <= vrijeme and p['zavrsen'] == False:
                kandidati.append(p)
        if len(kandidati) == 0:
            vrijeme = vrijeme + 1
            continue
        odabrani = kandidati[0]
        for k in kandidati:
            if k['bt'] < odabrani['bt']:
                odabrani = k
        odabrani['zavrsen'] = True
        vrijeme = vrijeme + odabrani['bt']
        odabrani['ct'] = vrijeme
        odabrani['tat'] = odabrani['ct'] - odabrani['at']
        odabrani['wt'] = odabrani['tat'] - odabrani['bt']
        rezultati.append(odabrani)
        zavrseni = zavrseni + 1
    prikazi_tabelu(rezultati)





def srtf_preemptive():
    n = int(input("Unesite ukupan broj narudžbi: "))
    procesi = []
    for i in range(n):
        at = int(input(f"Vrijeme dolaska {i+1}: "))
        bt = int(input(f"Vrijeme pripreme {i+1}: "))
        procesi.append({'id': i+1, 'at': at, 'bt': bt, 'preostalo': bt})
    vrijeme = 0
    zavrseni = 0
    rezultati = []
    while zavrseni < n:
        kandidati = []
        for p in procesi:
            if p['at'] <= vrijeme and p['preostalo'] > 0:
                kandidati.append(p)
        if len(kandidati) == 0:
            vrijeme = vrijeme + 1
            continue
        odabrani = kandidati[0]
        for k in kandidati:
            if k['preostalo'] < odabrani['preostalo']:
                odabrani = k
        vrijeme = vrijeme + 1
        odabrani['preostalo'] = odabrani['preostalo'] - 1
        if odabrani['preostalo'] == 0:
            odabrani['ct'] = vrijeme
            odabrani['tat'] = odabrani['ct'] - odabrani['at']
            odabrani['wt'] = odabrani['tat'] - odabrani['bt']
            rezultati.append(odabrani)
            zavrseni = zavrseni + 1
    prikazi_tabelu(rezultati)





def priority_scheduling():
    n = int(input("Unesite ukupan broj narudžbi: "))
    procesi = []
    for i in range(n):
        at = int(input(f"Vrijeme dolaska {i+1}: "))
        bt = int(input(f"Vrijeme pripreme {i+1}: "))
        pr = int(input(f"Prioritet (0-Najveći, 2-Najmanji): "))
        procesi.append({'id': i+1, 'at': at, 'bt': bt, 'pr': pr, 'zavrsen': False})
    vrijeme = 0
    zavrseni = 0
    rezultati = []
    while zavrseni < n:
        kandidati = []
        for p in procesi:
            if p['at'] <= vrijeme and p['zavrsen'] == False:
                kandidati.append(p)
        if len(kandidati) == 0:
            vrijeme = vrijeme + 1
            continue
        odabrani = kandidati[0]
        for k in kandidati:
            if k['pr'] < odabrani['pr']:
                odabrani = k
        odabrani['zavrsen'] = True
        vrijeme = vrijeme + odabrani['bt']
        odabrani['ct'] = vrijeme
        odabrani['tat'] = odabrani['ct'] - odabrani['at']
        odabrani['wt'] = odabrani['tat'] - odabrani['bt']
        rezultati.append(odabrani)
        zavrseni = zavrseni + 1
    prikazi_tabelu(rezultati)





def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("====================================================")
        print("   SISTEM ZA AUTOMATIZOVANO RASPOREĐIVANJE HRANE")
        print("====================================================")
        print("Izaberite neki od ponuđenih algoritama:")
        print("[1] Shortest Job First (SJF - Non-Preemptive)")
        print("[2] Shortest Job First preemptive (SRTF)")
        print("[3] Priority Scheduling")
        print("[4] Izlaz iz aplikacije")
        izbor = input("\nVaš izbor: ")
        if izbor == '1':
            sjf_non_preemptive()
        elif izbor == '2':
            srtf_preemptive()
        elif izbor == '3':
            priority_scheduling()
        elif izbor == '4':
            print("Hvala na korištenju sistema. Prijatno!")
            break
        else:
            print("\nGreška: Nevalidna opcija! Pokušajte ponovo sa 1, 2, 3 ili 4.")
            input("Pritisnite Enter za povratak na meni...")

if __name__ == "__main__":
    main()
