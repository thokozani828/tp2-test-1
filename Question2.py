#1 Write a python function named “register_party” that takes a list of parties.
#Each party must be presented by key value pairs. The keys should be “party_name”, “reg_number”, “member_count”).

def register_party(parties):
    registered_parties = []

    for party in parties:
        if party_registered(party['member_count']):
            registered_parties.append(party)

    return registered_parties

#The function should check if the new party has acceptable number of members for it to be registered as per the requirements narrated in the scenario.

def party_registered(member_count):
   
    MIN_MEMBERS = 10
    MAX_MEMBERS = 100

    return MIN_MEMBERS <= member_count <= MAX_MEMBERS


parties = [
    {"party_name": "EFF", "reg_number": 123, "member_count": 15},
    {"party_name": "IFP", "reg_number": 456, "member_count": 5},
    {"party_name": "ANC", "reg_number": 789, "member_count": 80}
]

registered_parties = register_party(parties)
print("Registered parties:")
for n in registered_parties:
    print(n)

#Now a new party called MK party which has 5300 members wants to apply to register the party for the next election.

# Function to generate a new registration number
def new_registration_number(last_registration_number):
    return last_registration_number + 1

# List of existing parties
existing_parties = [
    {"party_name": "EFF", "reg_number": 10003318, "member_count": 15},
    {"party_name": "IFP", "reg_number": 10003319, "member_count": 5},
    {"party_name": "ANC", "reg_number": 10003320, "member_count": 80}
]

# Details of the new party

new_party_name = "MK party"
new_member_count = 5300
last_registration_number = existing_parties[1]["reg_number"]

# Generate new registration number

new_registration_number = new_registration_number(last_registration_number)

# Create dictionary for the new party
new_party = {"party_name": new_party_name, "reg_number": new_registration_number, "member_count": new_member_count}

# Register the new party if it meets the criteria
registered_parties = register_party(existing_parties + [new_party])

# Print registered parties
print("Registered parties:")
for party in registered_parties:
    print(party)
#This code will create a new party called "MK party" with 5300 members, generate a new registration number, and then register the new party using the register_party function. If the new party meets the criteria, it will be added to the list of registered parties. Finally, it prints out the registered parties including the newly registered "MK party".




def update_voter_info(voters_info, voter_id, name, voting_district, has_voted):
    
    if voter_id in voters_info:
        voters_info[voter_id]["name"] = name
        voters_info[voter_id]["voting_district"] = voting_district
        if not voters_info[voter_id]["has_voted"]:
            voters_info[voter_id]["has_voted"] = has_voted
    else:
        voters_info[voter_id] = {
            "name": name,
            "voting_district": voting_district,
            "has_voted": has_voted
        }
    return voters_info

voters_info = {
    1: {"name": "John Doe", "voting_district": "District A", "has_voted": False},
    2: {"name": "Jane Smith", "voting_district": "District B", "has_voted": True}
}

# Update voter information or add new voter
voters_info = update_voter_info(voters_info, 3, "Alice Johnson", "District C", True)
voters_info = update_voter_info(voters_info, 1, "John Doe", "District A", True)

# Print updated voter information
print("Updated voter information:")
for voter_id, info in voters_info.items():
    print(f"Voter ID: {voter_id}, Name: {info['name']}, District: {info['voting_district']}, Voted: {info['has_voted']}")


        


