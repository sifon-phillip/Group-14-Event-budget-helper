def participant_cost(attendees, food_per_person, transport_per_person):
    return attendees * (food_per_person + transport_per_person)

print(participant_cost(10, 800, 200))
print(participant_cost( 0, 300, 500))


"""
   component: participant_cost
    return:  attendees * (food_per_person + transport_per_person)
    test : a normal attendees count
        print(participant_cost(10, 800, 200)
          zero attendees
        print(participant_cost(0, 300, 500)
    issue:none





"""

