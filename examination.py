def show_examination_menu():
    print("\nExamanation of Conscience")
    print("1. Duties to God")
    print("2. Speech")
    print("3. Charity and Duties")
    print("4. Back")

def show_duties_to_god():
    print("\nDuties to God")
    print("Have I neglected prayer?")
    print("Have I missed Mass without a serious reason?")
    print("Have I treated holy things with reverence?\n")
    print("\nScripture:")
    print(""Pray without ceasing." -1 Thessalonians 5:17\n")

def show_speech_examination():
    print("\nSpeech")
    print("Have I lied?")
    print("Have I gossiped?")
    print("Have I spoken harshly or without charity?\n")
    print(""Let no evil talk come out of your mouths..." - Ephesians 4:29\n")

def show_charity_examination():
    print("\nCharity and Duties")
    print("Have I failed to help others when I could?")
    print("Have I been impatient or selfish?")
    print("Have I neglected my responsibilities?\n")
    print("\"Love one another as I have loved you." - John 13:34\n")

def examination_menu():
    while True:
        show_examination_menu()
        choice = input("Choose a category ").strip()

        if choice == "1":
            show_duties_to_god()
        elif choice == "2":
            show_speech_examination()
        elif choice == "3":
            show_charity_examination()
        elif choice == "4":
            break
        else: 
            print("\nInvalid choice. Try again.\n")


