#Team Mission
def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"

def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}"



total = event_total(10, 800, 200, 5000)
status = budget_status(16000, total)


print(budget_status(16000, total))
print(event_summary("Study Day: total" total "naira.", status ))

"""

Handover note

Component: budget_status

Return: It returns Within budget when total <= budget and Over budget when total > budget

Tests: Below budget
total = event_total(10, 800, 200, 5000)
print(budget_status(16000, total))
Expected result: Within budget

    Exactly equal to budget
total = event_total(10, 800, 200, 6000)
print(budget_status(16000, total))
Expected result: Within budget

    Over budget
total = event_total(10, 800, 200, 15000)
print(budget_status(16000, total))
Expected result: Within budget

Issue: None

Component: Event_summary

Returns: When called it calls budget_status and returns the statement f"{event_name}: total {total} naira. {status}"

Tests: 
Required example
total = event_total(10, 800, 200, 5000)
status = budget_status(16000, total)
print(event_summary("Study Day: total" total "naira.", status ))
expected result: Study Day: total 16000 naira. Within budget

One different event name and total
total = event_total(10, 800, 200, 7000)
status = budget_status(16000, total)
print(event_summary("Study Day: total" total "naira.", status ))
expected result: Study Day: total 17000 naira. Over budget

Issue: None



























