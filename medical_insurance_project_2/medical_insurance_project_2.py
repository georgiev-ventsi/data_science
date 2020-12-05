# Add your code here
medical_costs = {
  "Marina": 6607.0,
  "Vinay": 3225.0
}

medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
# print(medical_costs)

medical_costs["Vinay"] = 3325.0

total_cost = 0
for person in medical_costs:
  total_cost += medical_costs[person]

average_cost = total_cost/len(medical_costs)
# print("Average Insurance Cost: {}".format(average_cost))

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

zipped_ages = list(zip(names, ages))
names_to_ages = {key: value for key, value in zipped_ages}
# print(names_to_ages)

marina_age = names_to_ages.get("Marina")
# print("Marina's age is {}".format(marina_age))

medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
# print(medical_records)

print("Connie's insurance cost is {} dollars.".format
(medical_records["Connie"]["Insurance_cost"]))

medical_records.pop("Vinay")

for record in medical_records:
  print("{} is a {} year old {} {} with a BMI of {} and insurance cost of {}".format(record, medical_records[record]["Age"], medical_records[record]["Sex"], medical_records[record]["Smoker"], medical_records[record]["BMI"], medical_records[record]["Insurance_cost"]))
