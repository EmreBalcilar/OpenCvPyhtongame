import cv2  # for window
import random  # random number

scale_percent = 50
picture1 = cv2.imread("jupyter.jpg")  # add image
picture2 = cv2.imread("mars.jpg")
picture3 = cv2.imread("merkur.jpg")
picture4 = cv2.imread("neptun.jpg")
picture5 = cv2.imread("saturn.jpg")
picture6 = cv2.imread("uranus.jpg")
picture7 = cv2.imread("venus.jpg")
picture8 = cv2.imread("world.jpg")

life = 0
while life <= 10:  # life you can try 10 times
    number = random.randint(1, 8)  # Generates 1 to 8 random numbers
    if number == 1:
        # cv2.waitKey(1)
        img = cv2.resize(picture1, (400, 400))  # resize window
        cv2.imshow("Question", img)
        cv2.waitKey(1)
        name = str(input("What is the name of planet :"))
        if name == "Jupiter":
            print("Correct")
            cv2.destroyAllWindows()
        else:
            print("Wrong Correct Answer is Jupiter ")
            life = life + 1

    if number == 2:
        img = cv2.resize(picture2, (400, 400))
        cv2.imshow("Question", img)
        cv2.waitKey(1)
        name = str(input("What is the name of planet :"))
        if name == "Mars":
            print("Correct")
            cv2.destroyAllWindows()
        else:
            print("Wrong Correct Answer is Mars ")
            life = life + 1

    if number == 3:
        img = cv2.resize(picture3, (400, 400))
        cv2.imshow("Question", img)
        cv2.waitKey(1)
        name = str(input("What is the name of planet :"))
        if name == "Mercury":
            print("Correct")
            cv2.destroyAllWindows()
        else:
            print("Wrong Correct Answer is Mercury ")
            life = life + 1

    if number == 4:
        img = cv2.resize(picture4, (400, 400))
        cv2.imshow("Question", img)
        cv2.waitKey(1)
        name = str(input("What is the name of planet :"))
        if name == "Neptune":
            print("Correct")
            cv2.destroyAllWindows()
        else:
            print("Wrong Correct Answer is Neptune ")
            life = life + 1

    if number == 5:
        img = cv2.resize(picture5, (400, 400))
        cv2.imshow("Question", img)
        cv2.waitKey(1)
        name = str(input("What is the name of planet :"))
        if name == "Saturn":
            print("Correct")
            cv2.destroyAllWindows()
        else:
            print("Wrong Correct Answer is Saturn ")
            life = life + 1

    if number == 6:
        img = cv2.resize(picture6, (400, 400))
        cv2.imshow("Question", img)
        cv2.waitKey(1)
        name = str(input("What is the name of planet :"))
        if name == "Uranus":
            print("Correct")
            cv2.destroyAllWindows()
        else:
            print("Wrong Correct Answer is Uranus ")
            life = life + 1

    if number == 7:
        img = cv2.resize(picture7, (400, 400))
        cv2.imshow("Question", img)
        cv2.waitKey(1)
        name = str(input("What is the name of planet :"))
        if name == "Venus":
            print("Correct")
            cv2.destroyAllWindows()
        else:
            print("Wrong Correct Answer is Venus ")
            life = life + 1

    if number == 8:
        img = cv2.resize(picture8, (400, 400))
        cv2.imshow("Question", img)
        cv2.waitKey(1)
        name = str(input("What is the name of planet :"))
        if name == "Earth":
            print("Correct")
            cv2.destroyAllWindows()
        else:
            print("Wrong Correct Answer is Earth ")
            life = life + 1
