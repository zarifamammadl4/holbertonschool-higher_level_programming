import os

def generate_invitations(template, attendees):
    """
    Generates invitation files based on a template and list of attendee dictionaries.
    Handles error cases such as invalid input types, empty template, empty attendee list,
    and missing fields by substituting N/A.
    """

    # ---------- Input Type Validation ----------
    if not isinstance(template, isinstance(template, str)):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # ---------- Empty Template Check ----------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # ---------- Empty List Check ----------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---------- Process Each Attendee ----------
    for index, attendee in enumerate(attendees, start=1):
        processed = template

        # Replace each placeholder safely
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            processed = processed.replace(f"{{{placeholder}}}", str(value))

        # Output filename
        filename = f"output_{index}.txt"

        try:
            # Write the processed text to a new invitation file
            with open(filename, "w") as file:
                file.write(processed)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            return
