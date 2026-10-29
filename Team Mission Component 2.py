
def event_total (attendees,food_per_person, transport_per_person, venue_cost):
    return participant_cost(attendees, food_per_person, transport_per_person ) + venue_cost


# Normal Attendee plus cost venue
print(event_total(10,800,5000))

# Zero Attendee
print(event_total(0,800,0))








