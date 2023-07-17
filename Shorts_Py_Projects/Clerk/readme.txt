Description:
You need to help the secretary to automate the work. To do this, you need to write a program that will execute user commands based on the stored data.

The initial data has the following structure:

list of all documents
documents = [
     {'type': 'passport', 'number': '2207 876234', 'name': 'Vasily Gupkin'},
     {'type': 'invoice', 'number': '11-2', 'name': 'Pokémon Gennady'},
     {'type': 'insurance', 'number': '10006', 'name': 'Aristarkh Pavlov'}
]
a list of shelves where documents are stored (if the document is in documents, then it must also be in directories)
directories = {
     '1': ['2207 876234', '11-2'],
     '2': ['10006'],
     '3': []
}

General requirements for the program:

the code must be correctly decomposed (each function is responsible for its specific task, duplicate functionality is reused, and its code is not repeated);
there are no global variables in the code (with the exception of documents and directories);
user input is processed in a while loop until the user explicitly terminates the program (by entering the "q" command).
Exercise 1
Item 1. The user can use the "p" command to recognize the owner of the document by its number
Work examples:

Enter the command:
p

Enter document number:
10006
Result:
Document owner: Aristarkh Pavlov

Enter the command:
p

Enter document number:
12345
Result:
Document not found in database

Point 2. The user can use the "s" command to find out on which shelf it is stored by the number of the document
Work examples:

Enter the command:
s

Enter document number:
10006
Result:
Document stored on shelf: 2

Enter the command:
s

Enter document number:
12345
Result:
Document not found in database

Item 3. The user can see the full information on all documents by the command "l"
Work example:

Enter the command:
l
Result:

№: 2207 876234, type: passport, owner: Vasily Gupkin, storage shelf: 1
№: 11-2, type: invoice, owner: Gennady Pokemonov, storage shelf: 1
№: 10006, type: insurance, owner: Aristarkh Pavlov, storage shelf: 2
Point 4. The user can add a new shelf using the "ads" command
Work examples:

Enter the command:
ads

Enter shelf number:
10
Result:
Shelf added. Current list of shelves: 1, 2, 3, 10.

Enter the command:
ads

Enter shelf number:
1
Result:
Such a shelf already exists. Current list of shelves: 1, 2, 3.

Point 5. The user can delete an existing shelf from the data using the "ds" command (only if it is empty)
Work examples:

Enter the command:
ds

Enter shelf number:
3
Result:
The shelf has been removed. Current list of shelves: 1, 2.

Enter the command:
ds

Enter shelf number:
1
Result:
There are documents on the shelf, remove them before removing the shelf. Current list of shelves: 1, 2, 3.

Enter the command:
ds

Enter shelf number:
4
Result:
Such a shelf does not exist. Current list of shelves: 1, 2, 3.

Task 2 (optional)
You need to complete the program from task 1 with more advanced commands.

Point 1. The user can add a new document to the data using the "ad" command
Work examples:

Enter the command:
ad

Enter document number:
42
Enter document type:
multipassport
Enter document owner:
R2D2
Enter Storage Shelf:
3
Result:

The document has been added. Current list of documents:
№: 2207 876234, type: passport, owner: Vasily Gupkin, storage shelf: 1
№: 11-2, type: invoice, owner: Gennady Pokemonov, storage shelf: 1
№: 10006, type: insurance, owner: Aristarkh Pavlov, storage shelf: 2
no: 42, type: multipassport, owner: R2D2, storage shelf: 3
Enter the command:
ad

Enter document number:
42
Enter document type:
multipassport
Enter document owner:
R2D2
Enter Storage Shelf:
4
Result:

Such a shelf does not exist. Add a shelf with the as command.
Current list of documents:
№: 2207 876234, type: passport, owner: Vasily Gupkin, storage shelf: 1
№: 11-2, type: invoice, owner: Gennady Pokemonov, storage shelf: 1
№: 10006, type: insurance, owner: Aristarkh Pavlov, storage shelf: 2
Point 2. The user can delete the document from the data by command "d"
Work examples:

Enter the command:
d

Enter document number:
10006
Result:

The document has been deleted.
Current list of documents:
№: 2207 876234, type: passport, owner: Vasily Gupkin, storage shelf: 1
№: 11-2, type: invoice, owner: Gennady Pokemonov, storage shelf: 1
Enter the command:
d

Enter document number:
123456
Result:

The document was not found in the database.
Current list of documents:
№: 2207 876234, type: passport, owner: Vasily Gupkin, storage shelf: 1
№: 11-2, type: invoice, owner: Gennady Pokemonov, storage shelf: 1
№: 10006, type: insurance, owner: Aristarkh Pavlov, storage shelf: 2
Item 3. The user can move the document from the shelf to the shelf using the "m" command
Work examples:

Enter the command:
m

Enter document number:
11-2
Enter shelf number:
3
Result:

The document has been moved.
Current list of documents:
№: 2207 876234, type: passport, owner: Vasily Gupkin,storage shelf: 1
№: 11-2, type: invoice, owner: Gennady Pokemonov, storage shelf: 3
№: 10006, type: insurance, owner: Aristarkh Pavlov, storage shelf: 2
Enter the command:
m

Enter document number:
11-2
Enter shelf number:
10
Result:
Such a shelf does not exist. Current list of shelves: 1, 2, 3.

Enter the command:
m

Enter document number:
42
Enter shelf number:
2
Result:

The document was not found in the database.
Current list of documents:
№: 2207 876234, type: passport, owner: Vasily Gupkin, storage shelf: 1
№: 11-2, type: invoice, owner: Gennady Pokemonov, storage shelf: 1
№: 10006, type: insurance, owner: Aristarkh Pavlov, storage shelf: 2