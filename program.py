from identity import *

name_person = {1 : 'Dany',
               2 : 'Igor',
               3 : 'Sany',
               4 : 'Danila'}
#Первые две функции только для загрузки лиц. Дальше для распознования используется только face_rocognation
face_download("dataset", name_person)

face_training("dataset", "trainer")

myClass = face_recognation("trainer", name_person)

print(myClass.condition, ' ', myClass.name)



