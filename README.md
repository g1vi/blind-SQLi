# Blind-SQLi
Python scripts for dumping the entire contents of a mysql database using blind sql injection. Two versions are provided, one for non-interactive shells and the other for interactive shells. Both of them may need to be updated manually to adapt to any specific target db.

Tested on mysql 8 + php 7.4.3

### Non-interactive shells

```python
python3 blindSQLi.py
```

Edit credentials in line 11 and column names in line 25 to adapt the script to any specific target db

### Interactive shells

```python
python3 iblindSQLi.py
```

The target url is intertactively prompted  
Edit the column names in line 25 to adapt the script to any specific target db

Example:
```
Enter target URL: http://localhost:5000/news.php?id=1
```

### License
Feel free to use or modify whenever and wherever you like
