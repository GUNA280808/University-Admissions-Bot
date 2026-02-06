import json

class AdmissionsChatbot:
    def __init__(self, data_file):
        with open(data_file) as f:
            self.data = json.load(f)
        self.current_program = None
        self.current_university = None

    def find_program(self, query):
        query = query.lower()
        for uni, uni_data in self.data["universities"].items():
            for program in uni_data["programs"]:
                if program in query:
                    self.current_program = program
                    self.current_university = uni
                    return program, uni
        return self.current_program, self.current_university

    def get_response(self, query):
        query = query.lower()
        program, university = self.find_program(query)

        if not program:
            return "Please mention a program like Computer Science, MBA, or BDes."

        info = self.data["universities"][university]["programs"][program]
        uni_info = self.data["universities"][university]

        if "eligibility" in query or "marks" in query:
            return f"Eligibility for {program.title()} at {university.title()}: {info['eligibility']}"

        elif "fee" in query:
            return f"Annual fee for {program.title()} is {info['fees_per_year']}."

        elif "career" in query or "job" in query:
            return "Career options: " + ", ".join(info["career_paths"])

        elif "exam" in query:
            return "Required entrance exams: " + ", ".join(info["entrance_exams"])

        elif "document" in query:
            return "Required documents: " + ", ".join(info["documents"])

        elif "step" in query or "apply" in query or "process" in query:
            return "Application steps:\n- " + "\n- ".join(info["application_steps"])

        elif "deadline" in query or "last date" in query:
            return f"Application deadline: {info['deadline']}"

        elif "where" in query or "location" in query:
            return f"{university.title()} is located in {uni_info['location']}."

        else:
            return (
                f"{program.title()} at {university.title()} is a "
                f"{info['degree']} program of {info['duration']} duration. "
                f"Annual fee: {info['fees_per_year']}."
            )
