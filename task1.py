contacts = {
    "charli": "9876543210",
    "Riya": "9123456780",
    "Karan": "9988776655"
}
contacts["Megha"] = "9001122334"
contacts["Riya"] = "7000000001"
found = contacts.get("charli", "Contact not found")
not_found = contacts.get("Rahul", "Contact not found")
print ("safe LookupResults: ")
print("charli's number:", found)
print("Rahul's number:", not_found)
print("\nAll Contacts:")
for name, phone in contacts.items():
    print("Contact:", name, "| Phone:", phone)