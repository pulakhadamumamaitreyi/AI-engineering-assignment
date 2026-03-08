appointments = []

def check_slot(doctor, time):

    for a in appointments:
        if a["doctor"] == doctor and a["time"] == time:
            return False

    return True


def book_slot(patient, doctor, time):

    if not check_slot(doctor, time):
        return "Slot already booked"

    appointments.append({
        "patient": patient,
        "doctor": doctor,
        "time": time
    })

    return "Appointment booked successfully"
