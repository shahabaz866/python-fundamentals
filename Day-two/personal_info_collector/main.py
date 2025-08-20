from models import Person
import storage

def menu():
    print("\n📋 Personal Info Collector")
    print("1. Add new person")
    print("2. Show all persons")
    print("3. Search person by name/email")
    print("4. Save & Exit")

def main():
    persons = storage.load_from_file()
    print("✅ Data loaded successfully.")

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                name = input("Enter name: ")
                age = input("Enter age: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")

                person = Person(name, age, email, phone)
                persons.append(person)
                print("🎉 Person added successfully!")

            except ValueError as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            if not persons:
                print("⚠ No persons available.")
            else:
                print("\n👥 List of persons:")
                for p in persons:
                    print(" -", p)

        elif choice == "3":
            key = input("Enter name or email to search: ").lower()
            found = [p for p in persons if key in p.name.lower() or key in p.email.lower()]
            if found:
                print("\n🔎 Search Results:")
                for p in found:
                    print(" -", p)
            else:
                print("⚠ No match found.")

        elif choice == "4":
            storage.save_to_file(persons)
            print("💾 Data saved. Exiting program...")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
