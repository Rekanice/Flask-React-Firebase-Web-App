import urllib
import pyrebase

firebaseConfig = {
  # DIY 
}

firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
db = firebase.database()
# storage = firebase.storage()

# # Login 
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# try:
#   auth.sign_in_with_email_and_password(email, password)
#   print("Successfully signed in.")
# except:
#   print("Invalid user or password. Try again.")

# # Signup
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# confirm_pw = input("Confirm password: ")   # WEAK_PASSWORD : Password should be at least 6 characters
# if password == confirm_pw: 
#   try:
#     auth.create_user_with_email_and_password(email, password)
#     print("Account successfully created.")
#   except:
#     print("Email already exists.")
  
# # Storage
# filename = input("Enter the name of the file you want to upload: ")
# cloudfilename = input("Enter the name of the file on the cloud: ")
# # Upload
# storage.child(cloudfilename).put(filename)
# # Get
# print(storage.child(cloudfilename).get_url(None))
# # Download
# cloudfilename = input("Enter the name of the file you want to download: ")
# storage.child(cloudfilename).download("", "download.txt")   # Save in current directory using "" with name "download.txt"
# Read file 
# cloudfilename = input("Enter the name of file you want to download:")
# url = storage.child(cloudfilename).get_url(None)
# f = urllib.request.urlopen(url).read()
# print(f)


# Realtime Database
# Create
# data = {'age':23, 'address': "Johor", 'name': 'Jason'}
# db.push(data)  # This pushes the data into a the main tree with random ID as node
# db.child('person').child('bums').push(data)  # This pushes the data into a named node but still has a random ID
# db.child('person').child('my Own ID').set(data)  # Use "set" over "push" to set a meaningful ID name (bye bye random IDs)


# Update 
# # Updates if exist / Create if doesnt exit (Here we specified the ID bcos it is known)
# db.child('person').child('my Own ID').update({'age': 22, 'sex': 'male'})  
# # When the name of IDs are not known & you know their content, we query by their content
# people = db.child("person").get()  # Store the dict under this node into a variable
# for person in people.each():
#   # print(person.key())  # get the node ID
#   print(person.val())  # get the sub-node OR dict under the ID node
  
#   if person.val()['age'] == 22:   # if the dict[key]==query_value
#     db.child('person').child(person.key()).update({'name': 'Jane'})



# Delete
# Known node ID
# db.child('person').child('third ID').child('age').remove()
# Unknown node ID
# people = db.child("person").get()  # Store the dict under this node into a variable
# for person in people.each():
#   # print(person.key())  # get the node ID
#   print(person.val())  # get the sub-node OR dict under the ID node
  
#   if person.val()['age'] == 22:   # if the dict[key]==query_value
#     db.child('person').child(person.key()).child('age').remove()


# Read / Queries
# people = db.child("person").order_by_child("name").equal_to("Jane").get()
# order_by_child("the index to query"), .equal_to("Jane") is the condition => get if "name" == "Jane"
# for person in people.each():
#   print(person.val())
#   print(person.val()['age'])


people = db.child("person").order_by_child("age").start_at(10).limit_to_last(3).get()  # >= 10
for person in people.each():
  print(person.val())
  print(person.val()['age'])
  