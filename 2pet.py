import sqlite3

# Create a connection to the database
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

# Create a table to store pets
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        breed TEXT,
        age INTEGER,
        description TEXT,
        adopted INTEGER DEFAULT 0
    )
''')

# Function to add a new pet to the database
def add_pet(name, breed, age, description):
    cursor.execute('INSERT INTO pets (name, breed, age, description) VALUES (?, ?, ?, ?)', (name, breed, age, description))
    conn.commit()
    print('Pet added successfully!')

# Function to view all available pets
def view_pets():
    cursor.execute('SELECT * FROM pets WHERE adopted = 0')
    pets = cursor.fetchall()
    for pet in pets:
        print(f'ID: {pet[0]}, Name: {pet[1]}, Breed: {pet[2]}, Age: {pet[3]}, Description: {pet[4]}')

# Function to search for pets based on breed
def search_pets_by_breed(breed):
    cursor.execute('SELECT * FROM pets WHERE breed = ? AND adopted = 0', (breed,))
    pets = cursor.fetchall()
    for pet in pets:
        print(f'ID: {pet[0]}, Name: {pet[1]}, Breed: {pet[2]}, Age: {pet[3]}, Description: {pet[4]}')

# Function to mark a pet as adopted
def adopt_pet(pet_id):
    cursor.execute('UPDATE pets SET adopted = 1 WHERE id = ?', (pet_id,))
    conn.commit()
    print('Pet adopted!')

# Main program loop
while True:
    print('\n--- Pet Adoption Center ---')
    print('1. View all available pets')
    print('2. Add a new pet')
    print('3. Search for pets by breed')
    print('4. Adopt a pet')
    print('5. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        view_pets()
    elif choice == '2':
        name = input('Enter pet name: ')
        breed = input('Enter pet breed: ')
        age = int(input('Enter pet age: '))
        description = input('Enter pet description: ')
        add_pet(name, breed, age, description)
    elif choice == '3':
        breed = input('Enter breed to search: ')
        search_pets_by_breed(breed
