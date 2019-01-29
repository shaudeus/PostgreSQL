from database import ConnectionPool


# Create a class for users
class User:
    # Initialize
    def __init__(self, email, first_name, last_name, id):
        # set parameters and properties
        # set parameters and properties
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    # Represent object as a string
    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        # Method to Insert data into users table in postgres database
        # Args:
        # email  (text): New user email, first name, last name

        # Open cursor insert command and close cursor
        with ConnectionPool() as cursor:
            # Execute SQL command to insert data into users table(id is running in sequence and is not needed)
            cursor.execute('INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)',
                           (self.email, self.first_name, self.last_name))

    @classmethod  # Do not access bound object
    def load_from_db_by_email(cls, email):  # Use current bound class == User
        # Method to retrieve data from users table in postgres database
        # Args:
        # email  (text): Email associated with data to retrieve

        # Get cursor from pool execute command and close cursor and return connection to pool
        with ConnectionPool() as cursor:
            # Open cursor, execute command, close cursor
            # Execute SQL command to insert data into users table(id is running in sequence and is not needed)
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))  # Email must be set in a tuple
            # Fetch the unique email
            user_data = cursor.fetchone()
            # Return email data
            # Populate new object parameters from table data
            # Commit data(write data to disk)

            return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])
