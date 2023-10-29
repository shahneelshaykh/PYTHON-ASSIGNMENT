
#SHAHNEEL,      AQIB AND        ASIM 
#F2020266155    F2020266151     F2020266185
class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class LibrarySystem:
    def __init__(self):
        self.publications = []

    def add_publication(self, publication):
        self.publications.append(publication)

    def remove_publication(self, publication):
        if publication in self.publications:
            self.publications.remove(publication)
        else:
            print(f"{publication} is not in the library.")

    def view_publications(self):
        if self.publications:
            print("Available Publications in the Library:")
            for publication in self.publications:
                print(publication)
        else:
            print("The library is empty.")

class LibraryUser(LibrarySystem):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.checked_out_publications = []

    def view_checked_out_publications(self):
        if self.checked_out_publications:
            print(f"{self.name}'s Checked Out Publications:")
            for publication in self.checked_out_publications:
                print(publication)
        else:
            print(f"{self.name} has no publications checked out.")

    def return_publication(self, publication):
        if publication in self.checked_out_publications:
            self.checked_out_publications.remove(publication)
            self.add_publication(publication)
            print(f"{self.name} returned {publication}")
        else:
            print(f"{self.name} did not have {publication} checked out.")


# ... (Previous code)

# Interactive part
library_system = LibrarySystem()
users = {}  # Dictionary to store LibraryUser objects

while True:
    print("\nOptions:")
    print("1. Add a publication to the library")
    print("2. View available publications")
    print("3. Remove a publication from the library")
    print("4. Create a library user")
    print("5. Check out a publication")
    print("6. Return a publication")
    print("7. Quit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        title = input("Enter the title of the publication: ")
        author = input("Enter the author of the publication: ")
        publication = Publication(title, author)
        library_system.add_publication(publication)

    elif choice == "2":
        library_system.view_publications()

    elif choice == "3":
        if not library_system.publications:
            print("The library is empty.")
        else:
            print("Available Publications in the Library:")
            for i, publication in enumerate(library_system.publications):
                print(f"{i + 1}. {publication}")

            publication_index = int(input("Enter the number of the publication to remove: ")) - 1

            if 0 <= publication_index < len(library_system.publications):
                removed_publication = library_system.publications.pop(publication_index)
                print(f"Removed: {removed_publication}")
            else:
                print("Invalid publication number. No publication removed.")

    elif choice == "4":
        user_name = input("Enter the user's name: ")
        users[user_name] = LibraryUser(user_name)

    elif choice == "5":
        user_name = input("Enter the user's name: ")
        title = input("Enter the title of the publication to check out: ")
        author = input("Enter the author of the publication to check out: ")
        user = users.get(user_name)

        if user and any(publication.title == title and publication.author == author for publication in library_system.publications):
            publication_to_checkout = next(publication for publication in library_system.publications if publication.title == title and publication.author == author)
            user.checkout_publication(user, publication_to_checkout)
        else:
            print(f"User {user_name} does not exist or the specified publication is not available in the library.")

    elif choice == "6":
        user_name = input("Enter the user's name: ")
        title = input("Enter the title of the publication to return: ")
        author = input("Enter the author of the publication to return: ")
        publication = Publication(title, author)
        user = users.get(user_name)
        if user:
            user.return_publication(publication)
        else:
            print(f"User {user_name} does not exist.")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a valid option.")
