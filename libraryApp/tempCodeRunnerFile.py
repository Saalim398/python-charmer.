with open("books.json", "r") as file:
    books = json.dumps(file)

# Print
for book in books:
    print(book)
