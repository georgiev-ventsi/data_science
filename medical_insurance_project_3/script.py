class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print('{name}’s estimated insurance costs is {cost} dollars.'.format(name= self.name,cost = estimated_cost))
  def  update_age(self, new_age):
    self.age = new_age
    print('{name} is now {new_age} years old.'.format(name = self.name, new_age = self.age))
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print('{name} has {num_of_children} child.'.format(name = self.name, num_of_children = self.num_of_children))
    else:
      print('{name} has {num_of_children} children.'.format(name = self.name, num_of_children = self.num_of_children))
  def patient_profile(self):
    patient_information = {}
    patient_information["Name"] = self.name
    patient_information["Age"] = self.age
    patient_information["Sex"] = self.sex
    patient_information["BMI"] = self.bmi
    patient_information["Number of Children"] = self.num_of_children
    patient_information["Smoker"] = self.smoker
    return patient_information
    
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
# print(patient1.name, patient1.age, patient1.sex)
# patient1.estimated_insurance_cost()
# patient1.update_age(26)
# patient1.estimated_insurance_cost()
# patient1.update_num_children(1)
# patient1.estimated_insurance_cost()
# patient1.update_num_children(2)
# patient1.estimated_insurance_cost()
print(patient1.patient_profile())
