class Book:
    def __init__ (self, name, author, illustrator, price, genre, Group, sales, rating):
        self.Book_name = name
        self.Book_author = author
        self.Book_illustrator = illustrator
        self.Book_price = price
        self.Book_genre = genre
        self.Book_Group = Group
        self.Book_sales = sales
        self.Book_rating = rating
        
    def add_Book(self):
        print("Name - " + self.Book_name)
        print("Author - " + self.Book_author)
        print("Illustrator - " + self.Book_illustrator)
        print("Price - " + self.Book_price)
        print("Genre - " + self.Book_genre)
        print("Age Group - " + self.Book_Group)
        print("Sales - " + self.Book_sales)
        print("Rating - " + self.Book_rating)
        print("Book details added !")
        
book1 = Book("Diary of a Wimpy Kid : Diper Overlode", "Jeff Kinney", "Jeff Kinney", "£12.00", "Children's Literature", "8 - 12 years old", "250,000,000", "4.7")
book1.add_Book()