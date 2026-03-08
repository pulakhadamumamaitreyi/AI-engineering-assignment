from appointments import book_slot, check_slot

def check_tool(doctor, time):

    if check_slot(doctor, time):
        return "Slot available"

    return "Slot not available"


def book_tool(patient, doctor, time):

    return book_slot(patient, doctor, time)
