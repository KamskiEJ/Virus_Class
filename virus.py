class Virus:
    def __init__(self, name: str, virus_family: str, mortality_rate: str, symptoms: list, time_existence: int):
        self.name = name
        self.virus_family = virus_family
        self.mortality_rate = mortality_rate
        self.symptoms = symptoms
        self.time_existence = time_existence

    def birth(self):
        return f"This virus ({self.name}) from China."

    def update_mortality(self, new_mortality):
        self.mortality_rate = new_mortality
        return f"Updated mortality rate: {self.mortality_rate}"

    def update_time_existence(self, years):
        self.time_existence += years
        return f"Update existance time: {self.time_existence} years"

    def display_info(self):
        return (
            f"Virus: {self.name}."
            f"\nFamily: {self.virus_family}."
            f"\nSymptoms: {" , ".join(self.symptoms)}."
            f"\nMortality: {self.mortality_rate}."
            f"\nExistance: {self.time_existence}"
                )





