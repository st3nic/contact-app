import sqlite3

conn = sqlite3.connect('contacts.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE contacts
             (name text, email text, phone long)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()