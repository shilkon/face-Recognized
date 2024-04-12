from identity import *

name_person = {
    1: 'Dany',
   2: 'Igor',
   3: 'Sany'
}

def main():
    #Первые две функции только для загрузки лиц. Дальше для распознования используется только face_rocognation
    face_download("dataset", name_person)

    face_training("dataset", "trainer")

if __name__ == '__main__':
    main()
