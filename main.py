def show_menu():
    print("Catholic CLI")
    print("1. Daily Prayer")
    print("2. Daily Reading")
    print("3. Hail Mary")
    print("4. Exit")


def show_our_father():
    print("\nOur Father, who art in heaven, hallowed be thy name.")
    print("Thy kingdom come, thy will be done, on earth as it is in heaven.")
    print("Give us this day our daily bread,")
    print("and forgive us our trespasses,")
    print("as we forgive those who trespass against us,")
    print("and lead us not into temptation,")
    print("but deliver us from evil. Amen. \n")


def show_hail_mary():
    print("\nHail Mary, full of grace, the Lord is with thee.")
    print("Blessed art thou among women,")
    print("and blessed is the fruit of thy womb, Jesus.")
    print("Holy Mary, Mother of God,")
    print("pray for us sinners,")
    print("now and at the hour of our death. Amen.\n")

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


                  
