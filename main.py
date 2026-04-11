from prayers import show_our_father, show_hail_mary

def show_menu():
    print("Catholic CLI")
    print("1. Daily Prayer")
    print("2. Daily Reading")
    print("3. Hail Mary")
    print("4. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()


        if choice =="1":
            show_our_father()
            print()
        elif choice == "2":
            print("\nDaily readings coming soon.")
            print()
        elif choice == "3":
            show_hail_mary()
        elif choice == "4":
            print("\nGoodbye.")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    main()


                  
