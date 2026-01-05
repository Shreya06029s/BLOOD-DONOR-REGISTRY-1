from datetime import datetime
donors = []
def add_donor():
    donor = {}
    donor["id"] = len(donors) + 1 
    donor["name"] = input("Enter name: ")
    donor["age"] = int(input("Enter age: "))
    donor["weight"] = int(input("Enter weight: "))
    donor["blood"] = input("Enter blood group: ").upper()
    donor["phone"] = input("Phone number: ")
    donor["city"] = input("City: ").title()
    donor["last_donation"] = input("Last donation date (YYYY-MM-DD): ")
    donors.append(donor)
    print("Donor added successfully. Donor ID =", donor["id"])
    
def check_eligibility():
    age = int(input("Enter age: "))
    weight = int(input("Enter weight: "))
    illness = input("Any recent illness? (yes/no): ").lower()
    last = input("Last donation date (YYYY-MM-DD): ")
    if age >= 18 and weight >= 50 and illness == "no" and days >= 90:
        print("The donor is ELIGIBLE.")
    else:
        print("The donor is NOT eligible.")
def search_by_blood():
    bg = input("Enter required blood group: ").upper()
    for d in donors:
        if d["blood"] == bg:
            print(d)
        else:
            print("Donor not found") 
def emergency_search():
    bg = input("Enter blood group: ").upper()
    city = input("Enter city: ").title()
    for d in donors:
        if d["blood"] == bg and d["city"] == city:
            print("Contact:", d["name"], d["phone"])
def update_donor():
    did = int(input("Enter donor ID to update: "))
    for d in donors:
        if d["id"] == did:
            d["phone"] = input("New phone: ")
            d["city"] = input("New city: ").title()
            d["last_donation"] = input("New last donation date (YYYY-MM-DD): ")
            print("Updated successfully.")
            return
    print("Donor not found.")
def delete_donor():
    did = int(input("Enter donor ID to delete: "))
    for d in donors:
        if d["id"] == did:
            donors.remove(d)
            print("Deleted successfully.")
            return
    print("Donor not found.")
    for d in donors:
        if d["blood"] in comp.get(req, []):
            print(d["name"], "-", d["blood"])
def sort_donors():
    donors.sort(key=lambda x: x["name"])
    print("Donors sorted by name.")
    for d in donors:
        print(d["id"], d["name"])
while True:
    print("""
1. Add Donor
2. Check Eligibility
3. Search by Blood Group
4. Emergency Search
5. Update Donor
6. Delete Donor
7. Sort Donors
8. Exit""")
    ch = int(input("Enter choice: "))
    if ch == 1:
        add_donor()
    elif ch == 2:
        check_eligibility()
    elif ch == 3:
        search_by_blood()
    elif ch == 4:
        emergency_search()
    elif ch == 5:
        update_donor()
    elif ch == 6:
        delete_donor()
    elif ch ==7 :
        sort_donors()
    elif ch == 8:
        print("Thank you")
        break
    else:
        print("Invalid choice")
