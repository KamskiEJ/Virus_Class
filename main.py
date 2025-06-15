from virus import Virus

virus_1 = Virus("COVID-19",
                "Coronaviridae",
                "Middle",
                ["Fever", "cough", "fatigue"],
                3)

virus_2 = Virus("Influenza",
                "Orthomyxoviridae",
                "Low",
                ["Fever", "sore throat"],
                100)


print(virus_1.display_info())
print(virus_1.birth())

print(virus_1.update_mortality("High"))
print(virus_1.update_time_existence(8))


print("\n--- Virus 2 Info ---")
print(virus_2.display_info())

print(virus_2.update_mortality("Very Low"))