import json

pti = int(input())
ro = input()
age = int(input())
gd = input()
ste = input()
sts = input()

a_file = open('covid_d.json', 'r')
obj = json.load(a_file)
n = len(obj['patientId'])

obj['patientId'][n] = pti
obj['reportedOn'][n] = ro
obj['onsetEstimate'][n] = None
obj['ageEstimate'][n] = age
obj['gender'][n] = gd
obj['state'][n] = ste
obj['status'][n] = sts

a_file = open('covid_d.json', 'w')
json.dump(obj, a_file, indent = 2)

a_file.close()


