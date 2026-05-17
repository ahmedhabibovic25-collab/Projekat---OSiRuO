import os

def prikazi_tabelu(podaci):
    print("\n#Br.Narudžbe | T-Dolaska | T-Pripreme | T-Kompletiranja | Ukupno-TAT | T-Čekanja")
    print("-" * 85)
    
    ukupni_tat = 0
    ukupno_cekanje = 0
    n = len(podaci)

    
    
    for p in podaci:
        print(f"{p['id']:<12} | {p['at']:<9} | {p['bt']:<10} | {p['ct']:<14} | {p['tat']:<10} | {p['wt']}")
        ukupni_tat += p['tat']
        ukupno_cekanje += p['wt']
        
    
    print("-" * 85)
    print(f"Prosječno vrijeme čekanja = {ukupno_cekanje / n:.2f} (min)")
    print(f"Prosječno ukupno vrijeme izvršavanja (TAT) = {ukupni_tat / n:.2f} (min)")
    input("\nPress any key to continue...")



def sjf_non_preemptive():
    print("\n--- SJF Non-Preemptive (Dostava hrane) ---")
    n = int(input("Unesite ukupan broj narudžbi: "))
    procesi = []
    
    for i in range(n):
        print(f"Narudžba {i+1}:")
        at = int(input("  Vrijeme dolaska/dobivanja narudžbe: "))
        bt = int(input("  Vrijeme pripremanja (izraženo u minutama): "))
        procesi.append({'id': i+1, 'at': at, 'bt': bt, 'zavrsen': False})

    vrijeme = 0
    zavrseni_broj = 0
    rezultati = []

    while zavrseni_broj < n:
        kandidati = [p for p in procesi if p['at'] <= vrijeme and not p['zavrsen']]
        
        if not kandidati:
            vrijeme += 1
            continue
        
        odabrani = min(kandidati, key=lambda x: x['bt'])
        
        odabrani['zavrsen'] = True
        vrijeme += odabrani['bt']
        
        odabrani['ct'] = vrijeme
        odabrani['tat'] = odabrani['ct'] - odabrani['at']
        odabrani['wt'] = odabrani['tat'] - odabrani['bt']
        
        rezultati.append(odabrani)
        zavrseni_broj += 1
    
    rezultati.sort(key=lambda x: x['id'])
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
            print("Opcija 2 odabrana (U izradi...)")
            input("Press enter...")
        elif izbor == '3':
            print("Opcija 3 odabrana (U izradi...)")
            input("Press enter...")
        elif izbor == '4':
            print("Hvala na korištenju sistema. Prijatno!")
            break
        else:
            print("Nevalidna opcija, pokušajte ponovo.")
            input("Press enter...")

if __name__ == "__main__":
    main()
