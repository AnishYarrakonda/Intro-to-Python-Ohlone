# Programmer: Anish Yarrakonda
# Lab 6: Dictionary

# imports
from printMeFirst import print_me_first
import json

"""
Function name: create_my_contact
Function description:   This function creates a dictionary containing contact records.
                        It encapsulates the creation of the my_contact dictionary,
                        which holds details for 3 people.
@param: None
@return: my_contact (dict) - dictionary containing all the contact records.
"""
def create_my_contact():
    my_contact = {
        "01": {
            "firstName": "John",
            "lastName": "Smith",
            "DOB": "1/20/1991",
            "phoneNum": {
                "number": "510-600-5400",
                "type": "cell"
            },
            "address": {
                "street": "100 main street",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94536"
            }
        },
        "02": {
            "firstName": "Ron",
            "lastName": "Robertson",
            "DOB": "5/23/1991",
            "phoneNum": {
                "number": "510-600-8800",
                "type": "cell"
            },
            "address": {
                "street": "4600 Ohlone Way",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94539"
            }
        },
        "03": {
            "firstName": "Paul",
            "lastName": "Washington",
            "DOB": "6/15/1995",
            "phoneNum": {
                "number": "510-688-1241",
                "type": "cell"
            },
            "address": {
                "street": "8543 Ohlone Plaza",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94539"
            }
        }
    }
    return my_contact

"""
Function name: save_json_file
Function description:   This function outputs the contents of a dictionary to a JSON file.
                        It takes the file name and the contact list dictionary as input
                        and writes the contact records to the specified JSON file.
@param fileName (str):      The name of the JSON file to be created.
@param contact_list (dict): A dictionary containing the contact records to be saved.
@return: None
"""
def save_json_file(fileName, contact_list):
    with open(fileName, 'w') as file:
        json.dump(contact_list, file, indent=4) # Use indent=4 for 4 spaces to look nice
    print(f"Contact list successfully saved to '{fileName}'")

"""
Function name: open_json_file
Function description:   This function opens a specified JSON file and
                        loads its content into a Python dictionary.
@param fileName (str):      The name of the JSON file to be opened.
@return json_data (dict):   A dictionary containing the data from the JSON file.
"""
def open_json_file(fileName):
    with open(fileName, 'r') as file:
        json_data = json.load(file)
    return json_data

"""
Function name: find_my_contact_key
Function description:   This function searches for a contact record in the
                        given dictionary based on a search key (first or last name).
                        If found, it prints the contact's details in a formatted way.
                        If not found, it prints a 'not found' message.
@param searchKey (str):     The name (first or last) to search for.
@param my_contact (dict):   The dictionary containing all contact records.
                            This is typically loaded from the JSON file.
@return: None
"""
def find_my_contact_key(searchKey, my_contact):
    for contact_id, contact_info in my_contact.items():
        # Convert both searchKey and names to lowercase for comparison
        if searchKey.lower() == contact_info["firstName"].lower() or searchKey.lower() == contact_info["lastName"].lower():
            found = True
            print(f"Contact Found: {contact_info['firstName']} {contact_info['lastName']}")
            print(f"  DOB: {contact_info['DOB']}")
            print(f"  Phone: {contact_info['phoneNum']['number']} ({contact_info['phoneNum']['type']})")
            print(f"  Address:")
            print(f"    Street: {contact_info['address']['street']}")
            print(f"    City: {contact_info['address']['city']}")
            print(f"    State: {contact_info['address']['state']}")
            print(f"    Zipcode: {contact_info['address']['zipcode']}")
            print("-" * 30) # 30 dash symbols to separate searches for readabilty
            break
    else:
        print(f"'{searchKey}' not found.")
        print("-" * 30) # separater

if __name__ == "__main__":
    # print me first
    print_me_first.print_me_first(
        lab_info = "CNET-142 Lab 6 Dictionary - Anish Yarrakonda",
        program_name = "dictionary.py"
        )
    
    contact_list = create_my_contact() # create dictionary
    
    save_json_file("/Users/anish/Documents/Python Coding Practice/Intro_to_Python_Course_@Ohlone/dictionary/my_contact.json", contact_list) # save disctionary to JSON file
    json_data = open_json_file('/Users/anish/Documents/Python Coding Practice/Intro_to_Python_Course_@Ohlone/dictionary/my_contact.json') #open JSON file load to dictionary
    
    print("***BEGINNING OF JSON List: \n", contact_list, \
          "\n***END OF JSON LIST\n\n")
    
    find_my_contact_key("Ron", json_data) # find record 'Ron'
    find_my_contact_key("Sha", json_data) # find record 'Sha'