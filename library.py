from BookCase import Book

cont = True

#print an introduction to the program
def print_intro():
	print("***********************")
	print("Welcome To Your Library")
	print("***********************")

#checks if the file exists
#create it if it does not
def check_for_file(file_name):
    try:
        myfile = open(file_name)
        print("Opening library file...")

    except FileNotFoundError:
        myfile = open(file_name, 'w+')
        print("Library file not found...")
        print("Creating library file...")

#display the menu to the user of the possible actions allowed
def menu(file_name):
    while cont:

        print("""
1: Add Book           2: View Library
3: Search For a Book  4: Search For an Author
5: Delete an Entry    6: Quit
""")

        selection = input("Selection: ")
        print(selection)
        #global cont
    
        if selection == '1':
            add_book(file_name)

        elif selection == '2':
            view_library(file_name)

        elif selection == '3':
            search_for_book(file_name)

        elif selection == '4':
            search_for_author(file_name)

        elif selection == '5':
            delete_entry(file_name)

        elif selection == '6':
            break

        select_again()

def select_again():
    global cont
    again = ''
    
    while again not in ['yes', 'no']:
        again = input("Would you like to make another choice (yes or no): ").lower()
        
        if again not in ['yes', 'no']:
            print("Please provide an appropriate answer!")

        elif again == 'no':
            cont = False
            print("Goodbye!")

def add_book(file_name):
	#Get the title and author of the book
	title = input("Title: ")
	author = input("Author: ")

	#if the title contains spaces
	#split the name into first and last
	if ' ' in author:
		position = author.find(' ')
		first_name = author[0:position]
		last_name = author[position+1::]

	#if the author is only one name long
	#assign it to first_name
	#assign an empty string to last_name
	else:
		first_name = author
		last_name = ''

	#create the book to be added to the library
	book = Book(title, first_name, last_name)

	#open the file containing the book information
	#add the book to the record along with a new line
	#the new line will be used when adding a new book
	with open(file_name, mode = 'a') as myfile:
		myfile.write(book.__str__())
		myfile.write('\n')

def view_library(file_name):
	#filename must be a .txt file
	with open(file_name) as myfile:
		print(myfile.read())

#allows the user to search their library file
#for books containing specific words
def search_for_book(file_name):
    '''
    #prompt the user for keywords
    #add them to a list to be compared with each book title
    keywords = input("Key words: ").title()
    keywords_list = keywords.split()
    candidates = []

    #open the file containing the book data
    with open(file_name) as myfile:
        #read in each line one by one
        line = myfile.readline().title()
        #split the line into title and author
        title_author_list = line.split(" By ")
        #split the title to test each individual word
        titles_list = title_author_list[0].split()
        if keyword_match(keywords_list, titles_list):
                #might not need .title() function if only looking at title
                # might be better to replace .lower() with .title()
                candidates.append(title_author_list[0])
    '''
    candidates = candidates_list(file_name, "Key words: ")

    print("********")
    print("Results")
    print("********")

    for item in candidates:
        print(item)

def keyword_match(keywords_list, line_list):
    for word in keywords_list:
        if word in line_list:
            return True

#if they only provide one name, find all the authors with that name
#and print their corresponding books
def search_for_author():
    #candidates = candidates_list(file_name, "Author: ")
    pass

#get the list of candidates for your search criteria
def candidates_list(file_name, text):
    #prompt the user for keywords
    #add them to a list to be compared
    keywords = input(text).title()
    keywords_list = keywords.split()
    candidates = []

    with open(file_name) as myfile:
        #read in each line one by one
        line = myfile.readline().title()
        #split the line into title and author
        title_author_list = line.split(" By ")
        #split the title to test each individual word
        titles_list = title_author_list[0].split()
        if keyword_match(keywords_list, titles_list):
            #might not need .title() function if only looking at title
            # might be better to replace .lower() with .title()
            candidates.append(title_author_list[0])

    return candidates

def delete_entry():
	pass

def sort_books():
	pass

def main():
    check_for_file('mylibrary.txt')
    print_intro()
    menu('mylibrary.txt')
    #add_book('mylibrary.txt')
    #view_library('mylibrary.txt')

main()
