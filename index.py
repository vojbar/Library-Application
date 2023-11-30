#Import vlastní knihovny pro upravený vzhled GUI
import customtkinter

# Nastavení vzhledu aplikace na světlý režim výchozí barevné téma na modrou
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")

# Seznam knih v knihovně s jejich atributy
books = [
    {
        "name": "Válka s Mloky",
        "author": "Karel Čapek",
        "available": True,
        "published": 1936,
        "firstName": None,
        "lastName": None
    },
    {
        "name": "Babička",
        "author": "Božena Němcová",
        "available": False,
        "published": 1855,
        "firstName": "Tomáš",
        "lastName": "Tutko"
    },
    {
        "name": "Krakatit",
        "author": "Karel Čapek",
        "available": False,
        "published": 1924,
        "firstName": "Vilém",
        "lastName": "Otte"
    },
    {
        "name": "Osudy dobrého vojáka Švejka za světové války",
        "author": "Jaroslav Hašek",
        "available": True,
        "published": 1923,
        "firstName": None,
        "lastName": None
    },
    {
        "name": "Mistr a Markétka",
        "author": "Mikuláš Akvinský",
        "available": False,
        "published": 1945,
        "firstName": "Vojtěch",
        "lastName": "Baron"
    },
    {
        "name": "Básně pro děti",
        "author": "Josef Čapek",
        "available": True,
        "published": 1946,
        "firstName": None,
        "lastName": None
    },
    {
        "name": "U nás v Kocourkově",
        "author": "Bohumil Říha",
        "available": True,
        "published": 1962,
        "firstName": None,
        "lastName": None
    },
]


# Definice třídy pro hlavní aplikaci
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Nastavení základních vlastností okna aplikace
        self.title("Library Application")
        self.geometry(f"{600}x{780}")

        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((1), weight=1)
        self.grid_rowconfigure((2), weight=0)

        # Inicializace textboxu pro zobrazení seznamu knih
        self.bookList = customtkinter.CTkTextbox(self, width=250, state="disabled", spacing1=6)
        self.bookList.grid(row=1, column=1, padx=(20, 20), pady=(60, 0), sticky="nsew")

        # Inicializace tlačítka pro výběr zobrazení seznamu knih
        self.bookListOptions = customtkinter.CTkSegmentedButton(self, values=["All books", "Only available", "Borrowed books"], command=self.writeBooks)
        self.bookListOptions.grid(row=1, column=1, padx=(48, 48), pady=(20, 10), sticky="new")
        self.bookListOptions.set("All books")
        self.writeBooks("All books")

        # Inicializace oddělovače na levý a pravý panel pro lepší organizaci rozvržení
        self.frameSeparator  = customtkinter.CTkFrame(self, width=800, fg_color="transparent")
        self.frameSeparator.grid(row=2, column=1, padx=(20, 20), pady=(10, 20), sticky="nsew")
        self.frameSeparator.grid_columnconfigure((1, 2), weight=1)
        self.frameSeparator.grid_rowconfigure((1), weight=1)

        # Inicializace levého panelu pro půjčování a vracení knih
        self.leftFrame = customtkinter.CTkTabview(self.frameSeparator)
        self.leftFrame.grid(row=1, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")

        # Přidání dvou záložek do levého panelu, společně s nastavením sloupců
        self.leftFrame.add("Borrow a book")
        self.leftFrame.add("Return a book")
        self.leftFrame.tab("Borrow a book").grid_columnconfigure(0, weight=1)
        self.leftFrame.tab("Return a book").grid_columnconfigure(0, weight=1)

        # Dropdown menu pro výběr knihy pro půjčení
        self.selectBookBorrow = customtkinter.CTkOptionMenu(self.leftFrame.tab("Borrow a book"), dynamic_resizing=False)
        self.selectBookBorrow.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nsew")
        self.selectBookBorrow.set(value="Choose a book")
        self.writeBorrowList()

        # Popisek pro vstup jména půjčovatele
        self.label = customtkinter.CTkLabel(self.leftFrame.tab("Borrow a book"), text="Enter borrower's name", justify="left", anchor="w")
        self.label.grid(row=2, column=0, padx=26, pady=(0, 0), sticky="nsew")
        
        # Vstup pro zadání jména půjčovatele
        self.nameEntry = customtkinter.CTkEntry(self.leftFrame.tab("Borrow a book"))
        self.nameEntry.grid(row=3, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")

        # Popisek pro vstup příjmení půjčovatele
        self.label = customtkinter.CTkLabel(self.leftFrame.tab("Borrow a book"), text="Enter borrower's surname", justify="left", anchor="w")
        self.label.grid(row=4, column=0, padx=26, pady=0, sticky="nsew")

        # Vstup pro zadání příjmení půjčovatele
        self.surnameEntry = customtkinter.CTkEntry(self.leftFrame.tab("Borrow a book"))
        self.surnameEntry.grid(row=5, column=0,  padx=(20, 20), pady=(0, 0), sticky="nsew")

        # Tlačítko pro potvrzení půjčení knihy
        self.confirmButton = customtkinter.CTkButton(self.leftFrame.tab("Borrow a book"), text="Confirm borrowing a book", command=self.updateBookAvailabilityBorrow)
        self.confirmButton.grid(row=6, column=0, padx=20, pady=(28, 10), sticky="nsew")

        # Dropdown menu pro výběr knihy pro vrácení
        self.selectBookReturn = customtkinter.CTkOptionMenu(self.leftFrame.tab("Return a book"), dynamic_resizing=False, command=self.writeBookAvailabilityReturn)
        self.selectBookReturn.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nsew")
        self.selectBookReturn.set(value="Choose a book")
        self.writeReturnList()

        # Popisek pro zobrazení jména půjčovatele
        self.label = customtkinter.CTkLabel(self.leftFrame.tab("Return a book"), text="Borrower's name", justify="left", anchor="w")
        self.label.grid(row=2, column=0, padx=26, pady=(0, 0), sticky="nsew")

        # Vstup pro zobrazení jména půjčovatele
        self.name = customtkinter.CTkEntry(self.leftFrame.tab("Return a book"), state="disabled")
        self.name.grid(row=3, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")

        # Popisek pro zobrazení příjmení půjčovatele
        self.label = customtkinter.CTkLabel(self.leftFrame.tab("Return a book"), text="Borrower's surname", justify="left", anchor="w")
        self.label.grid(row=4, column=0, padx=26, pady=0, sticky="nsew")

        # Vstup pro zobrazení příjmení půjčovatele
        self.surname = customtkinter.CTkEntry(self.leftFrame.tab("Return a book"), state="disabled")
        self.surname.grid(row=5, column=0,  padx=(20, 20), pady=(0, 0), sticky="nsew")

        
        # Tlačítko pro potvrzení vrácení knihy
        self.confirmButton = customtkinter.CTkButton(self.leftFrame.tab("Return a book"), text="Confirm returing a book", command=self.updateBookAvailabilityReturn)
        self.confirmButton.grid(row=6, column=0, padx=20, pady=(28, 10), sticky="nsew")

        # Inicializace pravého panelu pro přidání a odstránění knih
        self.rightFrame = customtkinter.CTkTabview(self.frameSeparator)
        self.rightFrame.grid(row=1, column=2, padx=(20, 0), pady=(0, 0), sticky="nsew")

        # Přidání dvou záložek do pravého panelu, společně s nastavením sloupců
        self.rightFrame.add("Add a book")
        self.rightFrame.add("Remove a book")
        self.rightFrame.tab("Add a book").grid_columnconfigure(0, weight=1)
        self.rightFrame.tab("Remove a book").grid_columnconfigure(0, weight=1)

        # Popisek pro zadání názvu knihy k přidání
        self.label = customtkinter.CTkLabel(self.rightFrame.tab("Add a book"), text="Book's name", justify="left", anchor="w")
        self.label.grid(row=1, column=0, padx=26, pady=(0, 0), sticky="nsew")

        # Vstup pro zadání názvu knihy k přidání
        self.bookNameEntry = customtkinter.CTkEntry(self.rightFrame.tab("Add a book"), state="normal")
        self.bookNameEntry.grid(row=2, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")

        # Popisek pro zadání autora knihy k přidání
        self.label = customtkinter.CTkLabel(self.rightFrame.tab("Add a book"), text="Author's publication", justify="left", anchor="w")
        self.label.grid(row=3, column=0, padx=26, pady=0, sticky="nsew")

        # Vstup pro zadání autora knihy k přidání
        self.authorEntry = customtkinter.CTkEntry(self.rightFrame.tab("Add a book"), state="normal")
        self.authorEntry.grid(row=4, column=0,  padx=(20, 20), pady=(0, 0), sticky="nsew")


        # Popisek pro zadání roku publikace knihy k přidání
        self.label = customtkinter.CTkLabel(self.rightFrame.tab("Add a book"), text="Year of publication", justify="left", anchor="w")
        self.label.grid(row=5, column=0, padx=26, pady=0, sticky="nsew")

        # Vstup pro zadání roku publikace knihy k přidání
        self.yearEntry = customtkinter.CTkEntry(self.rightFrame.tab("Add a book"), state="normal")
        self.yearEntry.grid(row=6, column=0,  padx=(20, 20), pady=(0, 0), sticky="nsew")

        # Tlačítko pro potvrzení přidání knihy
        self.confirmButton = customtkinter.CTkButton(self.rightFrame.tab("Add a book"), text="Confirm adding a book", command=self.addBook)
        self.confirmButton.grid(row=7, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # Dropdown menu pro výběr knihy k odstranění
        self.selectBookDelete = customtkinter.CTkOptionMenu(self.rightFrame.tab("Remove a book"), dynamic_resizing=False, command=self.writeRemoveBook)
        self.selectBookDelete.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nsew")
        self.selectBookDelete.set(value="Choose a book")
        self.writeDeleteList()

        # Popisek pro zobrazení jména autora knihy k odstranění
        self.label = customtkinter.CTkLabel(self.rightFrame.tab("Remove a book"), text="Author's name", justify="left", anchor="w")
        self.label.grid(row=2, column=0, padx=26, pady=(0, 0), sticky="nsew")

        # Vstup pro zobrazení jména autora knihy k odstranění
        self.author = customtkinter.CTkEntry(self.rightFrame.tab("Remove a book"), state="disabled")
        self.author.grid(row=3, column=0, padx=(20, 20), pady=(0, 0), sticky="nsew")


        # Popisek pro zobrazení roku publikace knihy k odstranění
        self.label = customtkinter.CTkLabel(self.rightFrame.tab("Remove a book"), text="Year of publication", justify="left", anchor="w")
        self.label.grid(row=4, column=0, padx=26, pady=0, sticky="nsew")

        # Vstup pro zobrazení roku publikace knihy k odstranění
        self.year = customtkinter.CTkEntry(self.rightFrame.tab("Remove a book"), state="disabled")
        self.year.grid(row=5, column=0,  padx=(20, 20), pady=(0, 0), sticky="nsew")

        # Tlačítko pro potvrzení odstranění knihy
        self.confirmButton = customtkinter.CTkButton(self.rightFrame.tab("Remove a book"), text="Confirm removing a book", command=self.removeBook)
        self.confirmButton.grid(row=6, column=0, padx=20, pady=(28, 10), sticky="nsew")

    # Funkce pro zobrazení informací o knihách na základě vybraného filtru
    def writeBooks(self, option):
        # Přepnutí stavu na editovatelný
        self.bookList.configure(state="normal")

        # Vymazání obsahu pole pro zobrazení knih
        self.bookList.delete("0.0", "end")

        if (option == "All books"):
            # Zobrazení všech knih v knihovně
            for book in books:
                self.bookList.insert("0.0", f"Book name: {book['name']}\nBook author: {book['author']}\nYear of publication: {book['published']}\nAvailability: {'available' if book['available'] == True else 'unavailable'}\n\n")
        elif (option == "Only available"):
            # Zobrazení pouze dostupných knih
            for book in books:
                if (book['available'] == True):
                    self.bookList.insert("0.0", f"Book name: {book['name']}\nBook author: {book['author']}\nYear of publication: {book['published']}\n\n")
        elif (option == "Borrowed books"):
            # Zobrazení vypůjčených knih a informací o vypůjčení
            for book in books:
                if (book['available'] == False):
                    self.bookList.insert("0.0", f"Book name: {book['name']}\nBook author: {book['author']}\nYear of publication: {book['published']}\nBorrower's name: {book['firstName']}\nBorrower's surname: {book['lastName']}\n\n")

        # Nastavení pole na needitovatelný stav           
        self.bookList.configure(state="disabled")
 
    # Funkce pro aktualizaci seznamu dostupných knih pro výpůjčku
    def writeBorrowList(self):
        borrowList = []
        for book in books:
            if (book['available'] == True):
                borrowList.append(book['name'])
            self.selectBookBorrow.configure(values=borrowList)

    # Funkce pro aktualizaci seznamu knih pro vrácení
    def writeReturnList(self):
        returnList = []
        for book in books:
            if (book['available'] == False):
                returnList.append(book['name'])
        self.selectBookReturn.configure(values=returnList)
    
    # Funkce pro aktualizaci seznamu knih k odstranění
    def writeDeleteList(self):
        bookList = []
        for book in books:
            bookList.append(book['name'])
        self.selectBookDelete.configure(values=bookList)

    # Funkce pro aktualizaci knihy po výpůjčce
    def updateBookAvailabilityBorrow(self):
        # Získání vybrané knihy k vypůjčení
        selectedBook = self.selectBookBorrow.get()

        # Najdi knihu v seznamu knih
        book = next((book for book in books if book['name'] == selectedBook), None)

        # Získání informací o vypůjčení od uživatele
        firstName = self.nameEntry.get()
        lastName = self.surnameEntry.get()

        # Aktualizace stavu knihy a přidání informací o vypůjčení
        book['available'] = False
        book['firstName'] = firstName
        book['lastName'] = lastName
            
        # Nastavení výchozí hodnoty v rozhraní
        self.selectBookBorrow.set(value="Choose a book")
        self.nameEntry.delete('0', 'end')
        self.surnameEntry.delete('0', 'end')

        # Aktualizace seznamů v uživatelském rozhraní
        booksList = self.bookListOptions.get()
        self.writeBooks(booksList)
        self.writeBorrowList()
        self.writeReturnList()
        self.writeDeleteList()

    # Funkce pro aktualizaci knihy po vrácení
    def updateBookAvailabilityReturn(self):
        # Získání vybrané knihy k vrácení
        selectedBook = self.selectBookReturn.get()

        # Najdi knihu v seznamu knih
        book = next((book for book in books if book['name'] == selectedBook), None)

        # Nastavení stavu knihy jako dostupné a vymazání informací o vypůjčení
        book['available'] = True
        book['firstName'] = None
        book['lastName'] = None
        
        # Nastavení výchozí hodnoty v rozhraní
        self.selectBookReturn.set(value="Choose a book")

        # Vyčištění informací o knize v rozhraní
        self.name.configure(state="normal")
        self.name.delete('0', 'end')
        self.name.configure(state="disabled")

        self.surname.configure(state="normal")
        self.surname.delete('0', 'end')
        self.surname.configure(state="disabled")

        # Aktualizace seznamů v uživatelském rozhraní
        booksList = self.bookListOptions.get()
        self.writeBooks(booksList)
        self.writeBorrowList()
        self.writeReturnList()
        self.writeDeleteList()
    
    # Funkce pro zobrazení informací o knize při výběru ze seznamu knih k vrácení
    def writeBookAvailabilityReturn(self, selectedBook):
        # Najdi knihu v seznamu knih
        book = next((book for book in books if book['name'] == selectedBook), None)

        # Nastavení zvolené hodnoty v rozhraní
        self.selectBookReturn.set(value=selectedBook)

        # Výpis informací o knize
        self.name.configure(state="normal")
        self.name.delete('0', 'end')
        self.name.insert(0, book['firstName'])
        self.name.configure(state="disabled")

        self.surname.configure(state="normal")
        self.surname.delete('0', 'end')
        self.surname.insert(0, book['lastName'])
        self.surname.configure(state="disabled")

    # Funkce pro přidání nové knihy do knihovn
    def addBook(self):
        # Získání hodnot z uživatelského vstupu
        name = self.bookNameEntry.get()
        author = self.authorEntry.get()
        year = self.yearEntry.get()

        # Vytvoření nového objektu knihy
        book = {
            "name": name,
            "author": author,
            "available": True,
            "published": year,
            "firstName": None,
            "lastName": None
        }

        # Přidání knihy do seznamu knih
        books.append(book)

        # Vyčištění vstupních polí po přidání knihy
        self.bookNameEntry.delete('0', 'end')
        self.authorEntry.delete('0', 'end')
        self.yearEntry.delete('0', 'end')

        # Aktualizace seznamů v uživatelském rozhraní
        booksList = self.bookListOptions.get()
        self.writeBooks(booksList)
        self.writeBorrowList()
        self.writeReturnList()
        self.writeDeleteList()

    # Funkce pro zobrazení informací o knize při výběru ze seznamu knih k odstranění
    def writeRemoveBook(self, selectedBook):
        # Najdi knihu v seznamu knih
        book = next((book for book in books if book['name'] == selectedBook), None)

        # Nastavení zvolené hodnoty v rozhraní
        self.selectBookDelete.set(value=selectedBook)

        # Výpis informací o knize
        self.author.configure(state="normal")
        self.author.delete('0', 'end')
        self.author.insert(0, book['author'])
        self.author.configure(state="disabled")

        self.year.configure(state="normal")
        self.year.delete('0', 'end')
        self.year.insert(0, book['published'])
        self.year.configure(state="disabled")

    # Funkce pro odstranění knihy z knihovny
    def removeBook(self):
        # Získání názvu vybrané knihy k odstranění
        selectedBook = self.selectBookDelete.get()

        # Najdi knihu v seznamu knih
        book = next((book for book in books if book['name'] == selectedBook), None)

        # Odebrání knihy ze seznamu knih
        books.remove(book)

        # Nastavení výchozí hodnoty v rozhraní
        self.selectBookDelete.set(value="Choose a book")

        # Vyčištění informací o knize v rozhraní
        self.author.configure(state="normal")
        self.author.delete('0', 'end')
        self.author.configure(state="disabled")

        self.year.configure(state="normal")
        self.year.delete('0', 'end')
        self.year.configure(state="disabled")

        # Aktualizace seznamů v uživatelském rozhraní
        booksList = self.bookListOptions.get()
        self.writeBooks(booksList)
        self.writeBorrowList()
        self.writeReturnList()
        self.writeDeleteList()

if __name__ == "__main__":
    # Vytvoření instance třídy App
    app = App()

    # Spuštění smyčky
    app.mainloop()