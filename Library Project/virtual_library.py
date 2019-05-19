from BookCase import Book
import pdb
import os
import urllib.request
import json
import textwrap
import csv
import re

cont = True

#print an introduction to the program
def print_intro():
    print("***********************")
    print("Welcome To Your Library")
    print("***********************")

#checks that the file passed as an argument exists
#if it does not exist, then create the file
#display the appropriate message
#use the i parameter to determine if additional text should be printed
def check_for_file(file_name, description, i):
    #check if the file exists
    try:
        myfile = open(file_name)
        if i:
            print("Opening {} file...".format(description.upper()))

    #in the event that the file does not exist, create it
    except FileNotFoundError:
        myfile = open(file_name, 'w+')
        if i:
            print("{} file not found...".format(description.upper()))
            print("Creating {} file...".format(description))

#print a menu for the user
#the action performed is based on the user input
def menu(file_name):
    #continue to ask for inputs as long
    #as the cont variable continues to be true
    while cont:
        
        #print the available options
        print("""
1: Add Book           2: View Library
3: Search For a Book  4: Search For an Author
5: Delete an Entry    6: Quit
        """)
        
        #get user input
        selection = input("Selection: ")

        #if option 1 is chosen, the add_book function will be called
        #this will add a book to the csv file containing the library data
        if selection == '1':
            add_book(file_name)

        #if option 2 is chosen, the view_library function will be called
        #this will display the contents of the csv file containing the library data
        elif selection == '2':
            view_library(file_name)
        
        #if option 3 is chosen, the search_for_book function will be called
        #this will search the csv file for book titles containing the keywords
        #entered by the user
        elif selection == '3':
            search_for_book(file_name)
        
        elif selection == '4':
            search_for_author(file_name)
        
        elif selection == '5':
            delete_entry(file_name, 'newfile.csv')
        
        elif selection == '6':
            break

#select_again()

#adds a book to the csv file containing the library data
def add_book(file_name):
    #get the api link from where to obtain the data from
    API_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    
    #prompt the user for the isbn of the book they would like to add
    print("Enter the isbn of the book you want to add.")
    #strip any whitespace from the input
    ISBN = input("ISBN: ").strip()

    #concatenate the api link with the isbn to create complete the URL
    #use the urllib.request module to open the URL
    with urllib.request.urlopen(API_link + ISBN) as f:
        text = f.read()
    
    decoded_text = text.decode("utf-8") #decode using utf-8
    obj = json.loads(decoded_text) #deserializes decoded_text to a usable python object
    volume_info = obj["items"][0]["volumeInfo"] #main source of desired information
    title = volume_info["title"] #extract title
    authors = ', '.join(volume_info["authors"]) #extract authors (focusing on one author for now)
    publisher = volume_info["publisher"] #extract publisher
    description = volume_info["description"] #extract description
    pages = str(volume_info["pageCount"]) #extract number of pages
    category = volume_info["categories"][0] #extract category (ocusing on one category for now)

    #create a book object that will be added to the unread list of books
    #the object is created with the extracted data from the JSON file used above
    mybook = Book(ISBN, title, authors, publisher, description, pages, category)

    #open the csv file that contains the data
    #and write the data of the new book into it
    with open(file_name, 'a') as myfile:
        writer = csv.writer(myfile) #create a writer object that will write to the csv file
        writer.writerow(mybook.attributes()) #write the row of data to the csv file

#prints the data contained in the csv file
#prints labels along with the information for each book
def view_library(file_name):
    #print the name of the shelf that is being viewed
    print("*************")
    print("Current Shelf")
    print("*************")
    print('\n') #add a newline for readability

    #open the csv file to read the data it contains
    with open(file_name, newline = '') as myfile:
        #convert the data into a list to make it easier to read the cells
        data = list(csv.reader(myfile))

        #read each row and print each cell with the appropriate title
        #do this for each row containing data
        for i in range(len(data)):
            print("Title: " + data[i][0]) #prints the title
            print("Author: " + data[i][1]) #prints the author
            print("Publisher: " + data[i][2]) #prints the publisher
            print("Description: " + data[i][3]) #prints the description
            print("Pages: " + data[i][4]) #prints the number of pages
            print("Category: " + data[i][5]) #prints the category the book belongs to
            print('\n') #prints a newline for readability

#allows the user to search their library for titles that match the entered keywords
def search_for_book(file_name):
    #use the candidates_list function to get the acceptable candidates
    candidates = candidates_list(file_name, "Key words: ", 0)
    
    #print the header of the results
    print("********")
    print("Results")
    print("********")

    #print the list of books obtained
    for book in candidates:
        print(book)

#check each piece of data with the keywords to determine a match
def keyword_match(keywords_list, data):
    for word in keywords_list:
        if re.search(word, data):
            return True #return true if a match is found

    return False #return false if no match is found

def candidates_list(file_name, text, i):
    #create a n empty list that will contain the candidates
    candidates = []
    
    #ask the user for the words they would like to use in the search
    keywords = input(text).title()
    
    #if i = 0 then the candidate list will be populated for books
    if i == 0:
        #split the words entered by the user to test each one
        keywords_list = keywords.split()
        
        with open(file_name, newline = '') as myfile:
            data = list(csv.reader(myfile))
            for j in range(len(data)):
                if keyword_match(keywords_list, data[j][0]):
                    candidates.append(data[j][0])

    elif i == 1:
        keywords_list = keywords.strip().title()
        
        with open(file_name, newline = '') as myfile:
            data = list(csv.reader(myfile))

            if len(keywords_list.split()) > 1:
                for j in range(len(data)):
                    if keywords_list == data[j][1]:
                        candidates.append(data[j][1])

            elif len(keywords_list.split()) == 1:
                for j in range(len(data)):
                    if re.search(keywords_list, data[j][1]):
                        candidates.append(data[j][1])

    return candidates

def search_for_author(file_name):
    candidates = candidates_list(file_name, "Author: ", 1)

    #print the header of the results
    print("********")
    print("Results")
    print("********")

    #print the list of authors obtained
    for author in candidates:
        print(author)

def delete_entry(file_name, newfile_name):
    print("Provide the data for the entry to be deleted")
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    
    check_for_file(newfile_name, 'updated', 0)
    
    with open(newfile_name, 'a') as newfile:
        with open(file_name, newline = '') as myfile:
            data = list(csv.reader(myfile))
            writer = csv.writer(newfile) #create a writer object that will write to the csv file
            for j in range(len(data)):
                #pdb.set_trace()
                if title == data[j][0] and author == data[j][1]:
                    continue
                else:
                    writer.writerow(data[j]) #write the row of data to the csv file

    #remove and rename files accordingly
    os.remove(file_name)
    os.rename(newfile_name, file_name)

def main():
    
    check_for_file('bookInfo.csv', 'library', 1)
    print_intro()
    menu('bookInfo.csv')

main()
