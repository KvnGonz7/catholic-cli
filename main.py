from prayers import show_our_father, show_hail_mary, show_glory_be
from readings import show_daily_reading 
from examination import examination_menu

def show_menu():
    print("Catholic CLI")
    print("1. Prayers")
    print("2. Daily Reading")
    print("3. Examination of Conscience")
    print("4. Exit")

def show_prayer_menu():
    print("\nPrayer Menu")
    print("1. Our Father")
    print("2. Hail Mary")
    print("3. Glory Be")
    print("4. Back")

def prayer_menu():
    while True:
        show_prayer_menu()
        choice = input ("Choose a prayer: ").strip()

        if choice == "1":
            show_our_father()
        elif choice == "2":
            show_hail_mary()
        elif choice == "3":
            show_glory_be()
        elif choice == "4":
            break
        else: 
            print("\nInvalid choice. Try again.\n")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            prayer_menu()
        elif choice == "2":
            show_daily_reading()
        elif choice == "3":
            examination_menu()
        elif choice == "4":
            print("\nGoodbye.")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    main()


                  
