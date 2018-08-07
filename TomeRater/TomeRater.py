class User(object):
    def __init__(self, name, email):
        self.name,self.email=name,email
        self.books={}
        return

    def get_email(self):
        return self.email
        
    def change_email(self, address):
        self.email=address
        print("The email for {} has been successfully changed.".format(self.name))
        return
    
    def __repr__(self):
        return "Name: {}, Email: {}, Books reviewed: {}".format(self.name,self.email,len(self.books.keys()))
        

    def __eq__(self, other_user):
        print("Eq called")
        return (self.name,self.email)==(other_user.name,other_user.email)

    def read_book(self,book,rating=None):
        self.books[book]=rating
        return

    def get_average_rating(self):
        j=0
        k=0
        for i in self.books.values():
            if i!=None:
                j+=i
                k+=1
        return j/k
            

class Book(object):
    def __init__(self,title,isbn):
        self.title,self.isbn=title,isbn
        self.ratings=[]
        

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self,new_isbn):
        self.isbn=new_isbn
        print("The isbn of {} has been successfully changed.".format(self.title))
        return

    def add_rating(self,rating):
        if type(rating) is not int or 0<rating>4:
            return "Not a valid rating"
        self.ratings.append(rating)
        return

    def __eq__(self,other):
        return(self.title,self.isbn)==(other.title,other.isbn)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        if len(self.ratings)==0:
            return 0
        return sum(self.ratings)/len(self.ratings)



  
class Fiction(Book):
    def __init__(self,title,author,isbn):
        super().__init__(title,isbn)
        self.author=author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title,self.author)

class Non_Fiction(Book):
    def __init__(self,title,subject,level,isbn):
        super().__init__(title,isbn)
        self.subject=subject
        self.level=level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title,self.level,self.subject)
    


class TomeRater():
    
    def __init__(self):
        self.users={}
        self.books={}

    def create_book(self,title,isbn):
        return Book(title,isbn)

    def create_novel(self,title,author,isbn):
        return Fiction(title,author,isbn)

    def create_non_fiction(self,title,subject,level,isbn):
        return Non_Fiction(title,subject,level,isbn)

    def add_book_to_user(self,book,email,rating=None):
        if email not in self.users:
            return "No user with email {}!".format(email)
        self.users[email].read_book(book,rating)
        book.add_rating(rating)
        if book not in self.books:
            self.books[book]=1
        elif book in self.books:
            self.books[book]+=1

    def add_user(self,name,email,user_books=None):
        self.users[email]=User(name,email)
        if user_books!=None:
            for i in user_books:
                self.add_book_to_user(i,email)
        
    def print_catalog(self):
        for i in self.books.keys():
            print(i)
        
    def print_users(self):
        for i in self.users.values():
            print(i)

    def most_read_book(self):
        m=0
        for i in self.books:
           if self.books[i]>m:
               m=self.books[i]
               b=i
        return "The most read book is {}.".format(b.title)

    def highest_rated_book(self):
        h=0
        for i in self.books:
            if i.get_average_rating()>h:
                h=i.get_average_rating()
                b=i
        return "The highest rated book is {}.".format(b.title)

    def most_positive_user(self):
        h=0
        for i in self.users.values():
            if i.get_average_rating()>h:
                h=i.get_average_rating()
                b=i
        return "The user with the highest ratings is {}.".format(b.name)
        
    
