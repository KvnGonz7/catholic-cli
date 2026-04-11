def show_menu():
    print("Catholic CLI")
    print("1. Daily Prayer")
    print("2. Daily Reading")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()


        if choice =="1":
            print("\nOur Father...")
            print()
        elif choice =="2":
            print("\nDaily readings coming soon.")
            print()
        elif choice == "3":
            print("\nGoodbye.")
            break
        else:
            print("\nInvalid choice. Try again.\n")

if __name__ == "__main__":
    main()


                  
