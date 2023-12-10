from buzzer import *
from identity import *
from svetodiod import *
from train import name_person


def main():
    while True:
        myClass = face_recognation("trainer", name_person)

        print(myClass.condition, ' ', myClass.name)

        if myClass.condition == Condition.RECOGNIZED:
            Buzz(400, 2)
            Led(500, 2)

        else:
            Buzz(400, 2)

if __name__ == '__main__':
    main()
