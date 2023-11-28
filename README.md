## Úvod
Tato dokumentace poskytuje podrobný přehled projektu "Aplikace knihovny", který byl vytvořen jako součást školního zadání do hodiny programování. Projekt je realizován v programovacím jazyce Python s využitím knihoven Tkinter a customtkinter pro tvorbu grafického uživatelského rozhraní.

## Popis aplikace
Aplikace slouží k efektivní správě knih v knihovně. Základní funkce aplikace zahrnují přidání knihy, odstranění knihy, vypůjčení knihy, vrácení knihy a zobrazení seznamu dostupných knih. Aplikace umožňuje uživatelům interagovat s knihami prostřednictvím grafického rozhraní, což zajišťuje snadné a intuitivní ovládání.

## Funkční požadavky
### 1. Přidání knihy
#### Kódový vzor:
```python
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
```
#### Komentář:
Funkce addBook slouží k přidání nové knihy do knihovny. Získává informace z uživatelského vstupu (název, autor, rok vydání), vytváří nový objekt knihy a přidá ho do seznamu knih. Následně vyčistí vstupní pole a aktualizuje seznamy v uživatelském rozhraní.

### 2. Odstranění knihy
#### Kódový vzor:
```python
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
```
#### Komentář:
Funkce removeBook slouží k odstranění knihy z knihovny. Získává název vybrané knihy k odstranění, najde odpovídající objekt v seznamu knih, provede odstranění a aktualizuje seznamy v uživatelském rozhraní.

### 3. Vypůjčení knihy
#### Kódový vzor:
```python
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
```
#### Komentář:
Funkce updateBookAvailabilityBorrow slouží k označení knihy jako vypůjčené a přidání informací o vypůjčení od uživatele. Získává vybranou knihu, informace o vypůjčení a provede aktualizaci stavu knihy.

### 4. Vrácení knihy
#### Kódový vzor:
```python
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
```
#### Komentář:
Funkce updateBookAvailabilityReturn slouží k označení knihy jako vrácené a vymazání informací o vypůjčení. Získává vybranou knihu a provede aktualizaci stavu knihy.

### 5. Zobrazení dostupných knih
#### Kódový vzor:
```python
def writeBooks(self, option):
    self.bookList.configure(state="normal")
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
    
    self.bookList.configure(state="disabled")
```
#### Komentář:
Funkce writeBooks slouží k zobrazení informací o knihách v uživatelském rozhraní podle zvoleného kritéria. Má tři možnosti: zobrazení všech knih, zobrazení pouze dostupných knih a zobrazení vypůjčených knih s informacemi o vypůjčení.

## Technická specifikace
Aplikace je napsána v programovacím jazyce Python, využívající knihoven Tkinter a customtkinter pro snadnou a efektivní tvorbu grafického uživatelského rozhraní. Tato volba knihoven umožňuje plynulý běh a zajišťuje, že uživatelé budou mít konzistentní a intuitivní používání aplikace.

Jedním z významných rozhodnutí při návrhu aplikace bylo záměrné vyhnutí se použití externí databáze. Namísto toho jsou všechny informace o knihách ukládány přímo v paměti programu ve formě seznamu knih. To zjednodušuje implementaci a udržování aplikace, zároveň však zachovává dostatečnou efektivitu pro účely tohoto projektu.

## Uživatelské rozhraní
Uživatelské rozhraní bylo pečlivě navrženo s důrazem na jednoduchost, přehlednost a intuitivnost. Tento přístup umožňuje uživatelům snadno a rychle porozumět funkcím a možnostem aplikace. Celkový design je koncipován tak, aby uživatelé rychle a efektivně zvládli správu knih v knihovně pomocí jednoduchých a intuitivních akcí.

## Postup implementace
Projekt byl implementován v několika krocích. Nejprve byla vytvořena kostra aplikace s pomocí knihoven Tkinter a customtkinter. Následně byly implementovány jednotlivé funkce aplikace, včetně přidání knihy, odstranění knihy, vypůjčení a vrácení knihy.

### Chronologie implementace:
**1. Vytvoření kostry aplikace v Tkinter a customtkinter.**

**2. Implementace přidání knihy:**
- Vytvoření formuláře pro zadání informací o knize.
- Ošetření vstupů a aktualizace seznamu knih.

**3. Implementace odstranění knihy:**
- Vytvoření rozhraní pro výběr knihy k odstranění.
- Ošetření vstupů a aktualizace seznamu knih.

**4. Implementace vypůjčení knihy:**
- Vytvoření formuláře pro zadání informací o vypůjčení knihy.
- Ošetření vstupů a aktualizace seznamu knih.

**5. Implementace vrácení knihy:**
- Vytvoření rozhraní pro výběr vrácené knihy.
- Ošetření vstupů a aktualizace seznamu knih.

## Testování
Provedená testování zahrnovala ověření správné funkcionality jednotlivých částí aplikace. Byly testovány scénáře, jako je přidání knihy, odstranění knihy, vypůjčení a vrácení knihy. Všechny testy byly úspěšné a potvrdily správnou funkcionalitu aplikace.

## Závěr a budoucí rozvoj
Celkově je projekt "Aplikace knihovny" úspěšným řešením zadání s funkcionalitou odpovídající požadavkům. Pro budoucí rozvoj by bylo možné zvážit implementaci dalších funkcí, jako je možnost rezervace knihy nebo filtrování knih podle různých kritérií.

### Rezervace knihy
**Popis:** Implementace možnosti rezervovat knihu umožní uživatelům zajistit si dostupnost určité knihy předem.
<br>**Technické aspekty:** Nová databázová struktura pro sledování rezervací, rozšíření uživatelského rozhraní pro jednoduchou rezervaci.

### Filtrování knih
**Popis:** Přidání funkcionality filtrování knih podle různých kritérií (např., žánr, autor, rok vydání) zlepší uživatelský zážitek při procházení knižního katalogu.
<br>**Technické aspekty:** Implementace filtrů a rozšíření vyhledávacích funkcí.
