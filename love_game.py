print("Welcome to my first game better half")
name = input("What is your name ? ")
age = int(input("What is your age? "))
print("hello",name,"you are",age,"years old")

if age >= 18:
        print("You are old enough to date!")
        play = input(print("Do you want to date me?")).lower()
        if play == "yes":
            print("Al ask some questions if you get them right we date!")
            love = input(print("Do you love me?"))
            if love == "yes":
              print("yes..I love you")
              feelings =input(print("Do you have any feelings for me?"))
              if feelings == "yes":
                  print("Thats love at first sight..i aint intrested")
              else:
                  print("i believe you aint sure..please do some soul searching")

            elif love == "no":
                print("we cant force love")
                friends = input(print("can we be friends?"))
                if friends == "yes":
                    print("Its is nice having you as my friend")
                    drink=input(print("Do you drink alcohol"))
                    if drink=="yes":
                        print("sorry we cant be friends.byee")
                    else:
                        print("Hope to have an awsome time ahead as we share ideas")
                else:
                    print("see yah")
        else:
              print('Sorry Darling you ain\'t my type')
else:
    print("thanks for your time,you are just pretty too young to date")


