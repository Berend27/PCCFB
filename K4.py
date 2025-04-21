# Chapter 4 Final Boss - Confronting the Key-Guardian
# Kapitel 4 befasst sich mit Wörterbüchern.
# This code creates a simple contacts application using
# a nested dictionary

# Step 1: Adding Data to the Dictionary
def add_contact(contacts, name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}

# Step 2: Searching for Data
def search_contact(contacts, name):
    return contacts.get(name, 'Contact not found')

# Step 3: Updating Data
def update_contact(contacts, name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
    else:
        return 'Contact not found'

# Step 4: Removing Data
def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
    else:
        return 'Contact not found'

# Step 5: Displaying All Data
def display_contacts(contacts):
    for name, details in contacts.items():
        print(f'Name: {name}, Phone: {details["phone"]}, Email: {details["email"]}')

# Step 6: Bringing It All Together
if __name__ == "__main__":
    contacts = {}
    add_contact(contacts, 'Marie Lou', '555-555-1111', 'marie.lou@example.com')
    add_contact(contacts, 'Bryan Luke', '555-555-2222', 'bryan.luke@example.com')
    add_contact(contacts, 'Kobe Bryant', '555-555-2223', 'kobe@lakers.com')
print(search_contact(contacts, 'Marie Lou'))

update_contact(contacts, 'Marie Lou', email='marielou@example.com')
display_contacts(contacts)

contacts['Luke Bryan'] = contacts.pop('Bryan Luke')
display_contacts(contacts)

remove_contact(contacts, 'Kobe Bryant')
display_contacts(contacts)
