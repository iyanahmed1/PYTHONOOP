class Patient():
    def __int__(self,name,age,patient_id,ailment,admitted):
        self.name=name
        self.age=age
        self.patient_id=patient_id
        self.ailment=ailment
        self.admitted=admitted
    def __str__(self):
        print(f'Name{self.name},Age{self.age},Patient_id{self.patient_id},Ailment{self.ailment},Admitted{'Yes'if self.admitted else 'No'}')
class Hospital():
    def __init__(self):
        self.patients=[]