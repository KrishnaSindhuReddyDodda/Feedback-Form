import sqlite3  
  
con = sqlite3.connect("FEEDBACK.db")  
print("Database opened successfully")  
  
con.execute("create table Feedback (department TEXT, feedback_type TEXT, describe_your_feedback TEXT, name TEXT, email TEXT)")  
  
print("Table created successfully")  
  
con.close()  