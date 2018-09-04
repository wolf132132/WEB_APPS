import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']
students = collection.find({})
print(students)

#use list generation
student = [student for student in collection.find({})]
print(student)

# student = [student['mark'] for student in collection.find({}) if student['mark'] == 99.00]
# print(student)
# for student in students:
#     print(student)