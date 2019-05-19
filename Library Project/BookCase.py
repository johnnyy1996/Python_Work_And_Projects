class Book():
    def __init__(self, isbn, title, authors, publisher, description, pages, category):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.description = description
        self.pages = pages
        self.category = category
        self.rating = 0
        self.reading = False

    def __str__(self):
        return (self.title + "\n" + self.authors + "\n" + self.publisher + "\n" + self.description + "\n" + self.pages + "\n" + self.category + "\n")

    def attributes(self):
        return [self.title, self.authors, self.publisher, self.description, self.pages, self.category]
