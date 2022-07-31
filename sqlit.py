import sqlite3
conn=sqlite3.connect("sqlite.db")
# 
# conn.execute('''

#            create table student( st_id INT AUTO_INCREMENT PRIMARY KEY,
#             st_name VARCHAR(50),
#             st_class VARCHAR(50),
#             st_email VARCHAR(50)
           
           
           
#            )
  
# ''')
# conn.close()
ins='''   
      insert into student (st_name,st_class,st_email) VALUES 
      ('RAVI','11th',"ravi@gmail.com")
    
    '''

conn.execute(ins)
conn.commit()
conn.close()