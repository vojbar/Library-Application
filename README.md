## Úvod
Tato dokumentace poskytuje podrobný přehled projektu "Aplikace knihovny", který byl vytvořen jako součást školního zadání do hodiny programování. Projekt je realizován v programovacím jazyce Python s využitím knihoven Tkinter a customtkinter pro tvorbu grafického uživatelského rozhraní.

## Popis aplikace
"Aplikace knihovny" slouží k efektivní správě knih v knihovně. Základní funkce aplikace zahrnují přidání knihy, odstranění knihy, vypůjčení knihy, vrácení knihy a zobrazení seznamu dostupných knih. Aplikace umožňuje uživatelům interagovat s knihami prostřednictvím grafického rozhraní, což zajišťuje snadnou a intuitivní obsluhu.

## Funkční požadavky
### 1. Přidání knihy
Uživatel může přidat novou knihu zadáním názvu, autora a roku vydání. Nově přidaná kniha je automaticky nastavena jako dostupná.

### 2. Odstranění knihy
Uživatel může odstranit existující knihu ze seznamu knih.

### 3. Vypůjčení knihy
Uživatel může označit knihu jako vypůjčenou, zadáním jména a příjmení vypůjčitele.

### 4. Vrácení knihy
Uživatel může vrátit vypůjčenou knihu, což aktualizuje informace o dostupnosti a vypůjčení.

### 5. Zobrazení dostupných knih
Uživatel má možnost zobrazit seznam všech knih, pouze dostupných knih nebo vypůjčených knih.

## Technická specifikace
Aplikace byla implementována v programovacím jazyce Python s využitím knihoven Tkinter a customtkinter pro tvorbu grafického rozhraní. Žádná externí databáze nebyla použita, a všechny informace jsou ukládány v paměti programu v podobě seznamu knih.

## Uživatelské rozhraní
Uživatelské rozhraní je navrženo tak, aby bylo intuitivní a přehledné. Snímky obrazovky a popisy v dokumentaci vizualizují navigaci a interakci uživatele s aplikací.

## Postup implementace
Projekt byl implementován v několika krocích. Nejprve byla vytvořena kostra aplikace s pomocí knihoven Tkinter a customtkinter. Následně byly implementovány jednotlivé funkce aplikace, včetně přidání knihy, odstranění knihy, vypůjčení a vrácení knihy.

### Chronologie implementace:
#### 1.Vytvoření kostry aplikace v Tkinter a customtkinter.

#### 2. Implementace přidání knihy:
Vytvoření formuláře pro zadání informací o knize.
Ošetření vstupů a aktualizace seznamu knih.
Implementace odstranění knihy:

#### 3. Vytvoření rozhraní pro výběr knihy k odstranění.
Ošetření vstupů a aktualizace seznamu knih.
Implementace vypůjčení knihy:

#### 4. Vytvoření formuláře pro zadání informací o vypůjčení knihy.
Ošetření vstupů a aktualizace seznamu knih.
Implementace vrácení knihy:

5. Vytvoření rozhraní pro výběr vrácené knihy.
Ošetření vstupů a aktualizace seznamu knih.
Testování
Provedená testování zahrnovala ověření správné funkcionality jednotlivých částí aplikace. Byly testovány scénáře, jako je přidání knihy, odstranění knihy, vypůjčení a vrácení knihy. Všechny testy byly úspěšné a potvrdily správnou funkcionalitu aplikace.

## Závěr a budoucí rozvoj
Celkově je projekt "Aplikace knihovny" úspěšným řešením zadání s funkcionalitou odpovídající požadavkům. Pro budoucí rozvoj by bylo možné zvážit implementaci dalších funkcí, jako je možnost rezervace knihy, filtrování knih podle různých kritérií nebo rozšíření možností uživatelského rozhraní pro ještě pohodlnější používání aplikace.
