from midtermstrategyclasses import ReturnList
import pandas as pd
import csv

userinp = raw_input("How would you like to sort your books? Author, Title, Year Published, and Summary are the accepted phrases: ")
choice = ReturnList()

if userinp == 'Author':
    choice.Author_List()
elif userinp == "Title":
    choice.Title_List()
elif userinp == "YearPublished":
    choice.Year_Published()
elif userinp == "Summary":
    choice.Book_Summary()
else:
     print('Invalid Option')

