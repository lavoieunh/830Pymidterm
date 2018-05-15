from 830classes import ReturnList
import pandas as pd
import csv

userinp = raw_input("How would you like to sort your books? Author, Title, Year Published, and Summary are the accepted phrases: ")

if userinp == 'Author':
    choice = ReturnList()
    choice.Author_List()
elif userinp == "Title":
    choice = ReturnList()
    choice.Title_List()
elif userinp == "YearPublished":
    choice = ReturnList()
    choice.Year_Published()
elif userinp == "Summary":
    choice = ReturnList()
    choice.Book_Summary()
else:
     print('Invalid Option')
