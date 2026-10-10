## **Contact Book Using Dictionaries**



##### **Task 10 – Python Programming**



###### **Project Description**



This project is a simple command-line Contact Book created using Python dictionaries.



The Contact Book allows users to add, search, update, delete, and display contact information.



###### **Objective**



The main objective of this project is to learn how to use Python dictionaries and understand practical key-value data management.



###### **Technologies Used**



\- Python

\- Python Dictionary

\- Conditional Statements

\- While Loop

\- For Loop

\- User Input

###### 

###### **Features**



\- Add a new contact

\- Search for a contact

\- Update an existing contact

\- Delete a contact

\- Display all contacts

\- Check for duplicate contacts

\- Handle contacts that do not exist

\- Simple menu-driven program

###### 

###### **Dictionary Structure**



The phone number is used as the key and the contact name is stored as the value.



###### **CRUD Operations**

**Create**

A new contact can be added using:

contacts\[phone] = name





**Read**

A contact can be searched using:

if phone in contacts:    print(contacts\[phone])





**Update**

An existing contact can be updated using:

contacts\[phone] = name





**Delete**

A contact can be deleted using:

del contacts\[phone]





###### **How the Program Works**

The program displays a menu with different options:

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

The user selects an option and provides the required information.

The program continues running until the user selects the Exit option.



###### **Sample Output**

===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 1

Enter phone number: 9876543210

Enter contact name: Madeena Beebi

Contact added successfully!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 1

Enter phone number: 8765432109

Enter contact name: Sravani

Contact added successfully!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 1

Enter phone number: 6543210987

Enter contact name: Manjula

Contact added successfully!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 1

Enter phone number: 7654321098

Enter contact name: Swathi

Contact added successfully!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 2

Enter phone number to search: 9876543210

Name: Madeena Beebi



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 3

Enter phone number to update: 4

Contact not found!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 5



Contacts:

Phone: 9876543210 Name: Madeena Beebi

Phone: 8765432109 Name: Sravani

Phone: 6543210987 Name: Manjula

Phone: 7654321098 Name: Swathi



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 3

Enter phone number to update: 8765432109

Enter new name: 8877665544

Contact updated successfully!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 5



Contacts:

Phone: 9876543210 Name: Madeena Beebi

Phone: 8765432109 Name: 8877665544

Phone: 6543210987 Name: Manjula

Phone: 7654321098 Name: Swathi



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 3

Enter phone number to update: 87654321009

Contact not found!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 4

Enter phone number to delete: 8765432109

Contact deleted successfully!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 1

Enter phone number: 7766554433

Enter contact name: sravani

Contact added successfully!



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 5



Contacts:

Phone: 9876543210 Name: Madeena Beebi

Phone: 6543210987 Name: Manjula

Phone: 7654321098 Name: Swathi

Phone: 7766554433 Name: sravani



===== CONTACT BOOK =====

1\. Add Contact

2\. Search Contact

3\. Update Contact

4\. Delete Contact

5\. Display Contacts

6\. Exit

Enter your choice: 6

Thank you for using Contact Book!


###### **Concepts Learned**

Through this project, I learned:

\- How to create a dictionary

\- How to store key-value pairs

\- How to add dictionary elements

\- How to search dictionary elements

\- How to update dictionary values

\- How to delete dictionary elements

\- How to use in with dictionaries

\- How to use .items()

\- How to create a menu-driven Python program

\- How to perform CRUD operations


###### **Conclusion**

The Contact Book project helped me understand Python dictionaries and how they can be used to manage real-world data.

It also provided practical knowledge of CRUD operations using Python.

