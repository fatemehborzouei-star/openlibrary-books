"""Fetch books from the OpenLibrary API, keep those published after 2000,
and save them to a CSV file."""

import csv

import requests

API_URL = "https://openlibrary.org/search.json"
SEARCH_QUERY = "fiction"
TARGET_BOOK_COUNT = 50
MIN_YEAR_EXCLUSIVE = 2000
PAGE_SIZE = 100
MAX_PAGES = 10
OUTPUT_FILE = "books.csv"
CSV_COLUMNS = ["title", "authors", "first_publish_year", "openlibrary_key"]


def fetch_page(page_number):
    """Request one page of search results and return the list of books."""
    params = {
        "q": SEARCH_QUERY,
        "page": page_number,
        "limit": PAGE_SIZE,
        "fields": "key,title,author_name,first_publish_year",
    }
    response = requests.get(API_URL, params=params, timeout=15)
    response.raise_for_status()
    return response.json().get("docs", [])


def parse_book(raw_book):
    """Convert a raw API record to a clean dict, or None if year is missing."""
    year = raw_book.get("first_publish_year")
    if year is None:
        return None
    return {
        "title": raw_book.get("title", "").strip(),
        "authors": ", ".join(raw_book.get("author_name", [])),
        "first_publish_year": year,
        "openlibrary_key": raw_book.get("key", ""),
    }


def collect_recent_books():
    """Collect books published after MIN_YEAR_EXCLUSIVE until the target is met."""
    books = []
    for page_number in range(1, MAX_PAGES + 1):
        for raw_book in fetch_page(page_number):
            book = parse_book(raw_book)
            if book and book["first_publish_year"] > MIN_YEAR_EXCLUSIVE:
                books.append(book)
                if len(books) == TARGET_BOOK_COUNT:
                    return books
    return books


def save_to_csv(books, file_path):
    """Write the books to a CSV file sorted by year (newest first)."""
    books.sort(key=lambda book: book["first_publish_year"], reverse=True)
    with open(file_path, "w", newline="", encoding="utf-8-sig") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(books)


def main():
    books = collect_recent_books()
    save_to_csv(books, OUTPUT_FILE)
    print(f"Saved {len(books)} books to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
