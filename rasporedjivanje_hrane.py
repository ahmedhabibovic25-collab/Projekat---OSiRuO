import os

def main():
    """Glavni meni aplikacije."""
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
            print("Opcija 1 odabrana (U izradi...)")
            input("Press enter...")
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
