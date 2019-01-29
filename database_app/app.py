# Command line application to inject data into postgres database

# Import Classes
from user import User
from database import Database


####################################
### Change database details here ###
####################################

# Enter your database details, this is an example
Database.init_conn(database="Application",user="postgres",password="Pa$$W0rD",host="localhost")


# Create user object and pass in properties
new_user = User("Jax@gmail.com", "Jackson", "Smith", None)
# Call method to add new user to database
new_user.save_to_db()

# Call method to retrieve specified data
user_from_db = User.load_from_db_by_email("bob@gmail.com")
# print recalled data to screen
print(user_from_db)

