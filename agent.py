from tools import check_tool, book_tool

def agent_response(text):

    text = text.lower()

    if "book" in text:

        doctor = "cardiologist"
        time = "10am"
        patient = "user"

        slot = check_tool(doctor, time)

        if slot == "Slot available":

            return book_tool(patient, doctor, time)

        else:
            return "Doctor is not available at that time"

    return "Please ask about booking appointment"
