# Specyfikacja Projektu: Sklep AI - Zielony Kąt

## 1. Opis funkcjonalności
* **Katalog produktów:** Użytkownik widzi dostępne rośliny na stronie głównej.
* **Kategorie:** Rośliny przypisane są do kategorii.
* **Panel Administratora:** Pełne zarządzanie produktami z poziomu panelu Django.

## 2. Wygląd aplikacji
* Minimalistyczny interfejs oparty na Bootstrap 5.
* Responsywna siatka produktów (karty ze zdjęciem, nazwą, opisem i ceną).

## 3. Wymagania techniczne
* Backend: Python 3.13, Django 5.x
* Baza danych: SQLite3
* Frontend: HTML5, Bootstrap 5

## 4. Schemat bazy danych
* **Category:** id (PK), name (CharField)
* **Product:** id (PK), category_id (FK), name (CharField), description (TextField), price (DecimalField), image (ImageField)