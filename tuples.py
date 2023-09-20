# Ticket information
# (ticket_number, staff_name, staff_id, email_address, description, response, ticket_status)

ticket_info = (2001, "Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working", "Not yet provided", "Open")

ticket_number, staff_name, staff_id, email_address, description, response, ticket_status = ticket_info

# We can either print the command as one lot but that won't show any title for the value.
# for ticket_info in ticket_info:
#print(ticket_info)

# Or can print the command individually if we need to select any heading for the value.
print("Ticket Number =", ticket_number)
print("Staff Name =", staff_name)
print("Staff ID = ", staff_id)
print("Email address = ", email_address)
print("Description =", description)
print("Response =", response)
# Print("Ticket Status =", ticket_status)
# the uppercase Print command threw an error that "Print is not defined" so have to be careful with the uppercase/lowercase sensitivity.
