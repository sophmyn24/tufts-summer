
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pygame

from pygame import time
from pygame import mixer

from button import Button

#function to start the music
def start_music():
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("lionking.mp3")
    # Setting the volume
    mixer.music.set_volume(0.7)
    # Start playing the song
    mixer.music.play()

#function to stop the music
def stop_music():
    mixer.music.stop()
    return

#main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((890, 880))
    clock = pygame.time.Clock()
    title_image = pygame.image.load("finalhope.png")
    # def __init__(self, text, width, height, pos, clock, text_font, screen):
    # button1 = Button("Click me", 200, 40,(200, 250))
    text = "Click me"
    width = 200
    height = 40
    pos = (200, 250)
    text_font = pygame.font.Font(None, 30)
    button = Button(text, width, height, pos, clock, text_font, screen)
    button_3 = Button("Start game", width, height, (100, 150), clock, text_font, screen)
    start_music()

    running = True
    while running:
        #title screen
        screen.blit(title_image, (0, 0))

        pygame.display.update()
        #check if music has played for 5 seconds
        time.delay(15000)
        if time.get_ticks() >= 15000:  # 9500
            stop_music()
            screen.fill("pink")
            # screen.blit(button, pos)
            button.draw(screen)
            button_3.draw(screen)
            pygame.display.update()
        #check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ALL GAME CODE FROM GITHUB
        print("Welcome to the Circle of Life! Time to build your character!")
        points = 5
        #this will be a button
        print("Start Now")

        #2 buttons: girl (in pink) and boy (in blue)
        gender = input("Enter a g if you want to be a girl and b if you want to be a boy: ")
        name = input("Enter your name: ")
        print(f"Hi {name}!")

        print("You have now started your life! ")
        print("Here are 5 points to start you off! (Tip: Gain points by answering trivia questions correctly!)")
        print("Points = 5")

        # These show that there is a space in the text, so it is easier for the user to read
        print(" ")

        # sophie wanted the user to press enter before turning 7 so here
        continue1 = input("Type 'next' to continue through the next couple of years!: ")
        print(" ")
        print(" ")

        # 7 years old!
        print("Happy Birthday! You are officially 7 years old!")
        print(" ")

        # eventually will get changed to being able to push individual buttons
        print("What is your personality type? (No wrong answers!)")
        print("a. Introverted")
        print("b. Kind")
        print("c. Outgoing")
        print("d. Funny")

        personality = input("Enter the letter of your choice here: ")
        print(" ")

        # 14 years old!
        print(" ")
        print("Happy Birthday! You are officially 14 years old and starting High School!")
        print(" ")

        # interests question
        print("What are you interested in? (No wrong answers!)")
        print("a. Sports")
        print("b. STEM")
        print("c. Humanities")
        print("d. Art")
        interests = input("Enter the letter of your choice here: ")
        print(" ")

        # if they picked sports
        if (interests.lower() == "a"):
            print("If you know so much about sports, how often are the Olympics held? ")
            print("a. every 3 years")
            print("b. every 4 years")
            print("c. every 6 years")
            print("d. every 5 years")
            olympics = input("Enter the letter of your choice here: ")
            print(" ")
            if (olympics.lower() == "a") or (olympics.lower() == "c") or (olympics.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (olympics.lower() == "b"):
                points += 1
                print(f"Correct! +1 points! Points = {points}")

        # if they picked STEM
        elif (interests.lower() == "b"):
            print("If you know so much about STEM, what is the powerhouse of the cell? ")
            print("a. Nucleus")
            print("b. Ribosomes")
            print("c. Golgi complex")
            print("d. Mitochondria")
            powerhouse = input("Enter the letter of your choice here: ")
            print(" ")
            if (powerhouse.lower() == "a") or (powerhouse.lower() == "b") or (powerhouse.lower() == "c"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (powerhouse.lower() == "d"):
                points += 1
                print(f"Correct! +1 points! Points = {points}")

        # if they picked humanities
        elif (interests.lower() == "c"):
            print("If you know so much about humanities, who is the current Monarch of the UK? ")
            print("a. King Harry")
            print("b. King Philip")
            print("c. King Charles")
            print("d. William")
            monarch = input("Enter the letter of your choice here: ")
            print(" ")
            if (monarch.lower() == "a") or (monarch.lower() == "b") or (powerhouse.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (monarch.lower() == "c"):
                points += 1
                print(f"Correct! +1 points! Points = {points}")

        # if they picked art
        elif (interests.lower() == "d"):
            print("If you know so much about art, who painted the Mona Lisa? ")
            print("a. Pablo Picasso")
            print("b. Leonardo DaVinci")
            print("c. Vincent Van Gogh")
            print("d. Claude Monet")
            Mona_lisa = input("Enter the letter of your choice: ")
            print(" ")
            if (Mona_lisa.lower() == "a") or (Mona_lisa.lower() == "c") or (Mona_lisa.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (Mona_lisa.lower() == "b"):
                points += 1
                print(f"Correct! +1 points! Points = {points}")

        print(" ")
        continue2 = input("Type 'next' to continue through the next couple of years!: ")
        print(" ")
        print(" ")

        # 18 years old!
        print("Happy Birthday! You are officially 18 years old!")
        print(" ")

        # majors question
        print("What are you interested in pursuing in college? (No wrong answers!)")
        print("a. D1 athlete (Sports)")
        print("b. Pre-med (STEM)")
        print("c. Liberal arts (Humanities)")
        print("d. Fine arts (Art)")
        majors = input("Enter the letter of your choice here: ")
        print(" ")

        # if they chose D1 athlete and got their previous question right
        if (majors.lower() == "a"):
            print("If you know so much about sports, which country won the 2022 World Cup? ")
            print("a. France")
            print("b. Brazil")
            print("c. Argentina")
            print("d. Spain")
            world_cup = input("Enter the letter of your choice: ")
            print(" ")
            # if statements to gain points
            if (world_cup.lower() == "a") or (world_cup.lower() == "b") or (world_cup.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (world_cup.lower() == "c"):
                points += 2
                print(f"Correct! +2 points! Points = {points}")

        # if they chose pre-med
        if (majors.lower() == "b"):
            print("If you know so much about STEM, what is “i” squared? ")
            print("a. -1")
            print("b. 5")
            print("c. An irrational number")
            print("d. The diagonal axis on a graph")
            I_squared = input("Enter the letter of your choice: ")
            print(" ")
            if (I_squared.lower() == "a"):
                points += 2
                print(f"Correct! +2 points! Points = {points}")
            elif (I_squared.lower() == "b") or (I_squared.lower() == "c") or (I_squared.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")

        # if they chose liberal arts
        if (majors.lower() == "c"):
            print("If you know so much about humanities, select the correct sentence. ")
            print("a. Its beautiful")
            print("b. It’s beautiful")
            print("c. Their beautiful")
            print("d. There beautiful")
            Grammar = input("Enter the letter of your choice: ")
            print(" ")
            if (Grammar.lower() == "a") or (Grammar.lower() == "c") or (Grammar.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (Grammar.lower() == "b"):
                points += 2
                print(f"Correct! +2 points! Points = {points}")

        # if they chose fine arts
        if (majors.lower() == "d"):
            print("If you know so much about art, who won album of the year at the Grammys in 2022? ")
            print("a. Harry Styles - Harry’s House")
            print("b. Taylor Swift - Midnights")
            print("c. Bad Bunny - Un Verano Sin Ti")
            print("d. Doja Cat - Planet Her")
            Grammys = input("Enter the letter of your choice: ")
            print(" ")
            if (Grammys.lower() == "a"):
                points += 2
                print(f"Correct! +2 points! Points = {points}")
            elif (Grammys.lower() == "b") or (Grammys.lower() == "c") or (Grammys.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")

        print(" ")
        continue3 = input("Type 'next' to continue through the next couple of years!: ")
        print(" ")
        print(" ")

        # 22 years old!
        print("Happy Birthday! You are officially 22 years old!")
        print("You also just graduated college! Congratulations!")
        print(" ")

        # choose a career
        print("What career path would you like to take? (No wrong answers!)")
        print("a. Professional athlete")
        print("b. Doctor")
        print("c. Lawyer")
        print("d. Artist")
        Career = input("Enter the letter of your choice: ")
        print(" ")

        # if they chose athlete
        if (Career.lower() == "a"):
            print("If you know so much about sports, what country won the first Women's World Cup? ")
            print("a. Brazil")
            print("b. Spain")
            print("c. England")
            print("d. United States of America")
            Womens_world_cup = input("Enter the letter of your choice: ")
            print(" ")
            if (Womens_world_cup == "a") or (Womens_world_cup == "b") or (Womens_world_cup == "c"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (Womens_world_cup == "d"):
                points += 3
                print(f"Correct! +3 points! Points = {points}")

        # if they chose doctor
        if (Career.lower() == "b"):
            print("If you know so much about STEM, what is entropy? ")
            print("a. The heat of a system")
            print("b. The electric charge of a molecule")
            print("c. The degree of disorder in a system")
            print("d. The color of a substance")
            Entropy = input("Enter the letter of your choice: ")
            print(" ")
            if (Entropy.lower() == "a") or (Entropy.lower() == "b") or (Entropy.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (Entropy.lower() == "c"):
                points += 3
                print(f"Correct! +3 points! Points = {points}")

        # if they chose lawyer
        if (Career.lower() == "c"):
            print("If you know so much about law, how many members are in the House of Representatives? ")
            print("a. 402")
            print("b. 480")
            print("c. 510")
            print("d. 435")
            house = input("Enter the letter of your choice: ")
            print(" ")
            if (house.lower() == "a") or (house.lower() == "b") or (house.lower() == "c"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (house.lower() == "d"):
                points += 3
                print(f"Correct! +3 points! Points = {points}")

        # if they chose art
        if (Career.lower() == "d"):
            print("If you know so much about art, how many plays did Shakespeare write? ")
            print("a. 72 plays")
            print("b. 38 plays")
            print("c. 26 plays")
            print("d. 108 plays")
            shakespeare = input("Enter the letter of your choice: ")
            print(" ")
            if (shakespeare.lower() == "a") or (shakespeare.lower() == "c") or (shakespeare.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (shakespeare.lower() == "b"):
                points += 3
                print(f"Correct! +3 points! Points = {points}")

        print(" ")
        continue4 = input("Type 'next' to continue through the next couple of years!: ")
        print(" ")

        # 30 years old
        print("Happy Birthday! You are officially 30 years old!")
        print(" ")
        print("Do you want to get married? Type y if yes and n if no. (No wrong answers!)")
        marriage = input("Enter your decision: ")

        # if they want to get married
        if (marriage.lower() == "y"):
            print("Congratulations newly-weds!")
            print(" ")
            print("Here's a quick trivia question: what is the second most popular color for a wedding dress (the first one being white)?")
            print("a. black")
            print("b. light blue")
            print("c. light pink")
            print("d. red")
            wedding_dress = input("Enter the letter of your choice: ")
            print(" ")
            if (wedding_dress.lower() == "a") or (wedding_dress.lower() == "b") or (wedding_dress.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (wedding_dress.lower() == "c"):
                points += 2
                print(f"Correct! +2 points! Points = {points}")

        # if they dont want to get married
        if (marriage.lower() == "n"):
            print("Okay independence!")
            print(" ")
            print("Here's a quick trivia question: How many marriages end in divorce?")
            print("a. 20-30%")
            print("b. 30-40%")
            print("c. 40-50%")
            print("d. 50-60%")
            divorce = input("Enter the letter of your choice: ")
            print(" ")
            if (divorce.lower() == "a") or (divorce.lower() == "b") or (divorce.lower() == "d"):
                print(f"Incorrect. +0 points! Points = {points}")
            elif (divorce.lower() == "c"):
                points += 2
                print(f"Correct! +2 points! Points = {points}")

        print(" ")
        continue5 = input("Type 'next' to continue through the next couple of years!: ")
        print(" ")

        # 32 years old
        print("Happy Birthday! You are officially 32 years old!")
        print(" ")
        print("Do you want to have kids? (No wrong answers!)")
        print("a. No, thanks")
        print("b. Yes, one!")
        print("c. Yes, two!")
        print("d. Yes, three!")
        kids = input("Enter the letter of your choice here: ")
        print(" ")

        # if they want kids
        if (kids.lower() == "b") or (kids.lower() == "c") or (kids.lower() == "d"):
            print("Congratulations!")
            print(" ")
            print("It's time for bed! How should your baby sleep?")
            print("a. on their back")
            print("b. on their left side")
            print("c. on their right side")
            print("d. on their stomach")
            baby_time = input("Enter the letter of your choice here: ")
            if baby_time.lower() == "a":
                points += 2
                print(f"Correct! +2 points! Points = {points}")
            elif baby_time.lower() == "b" or baby_time.lower() == "c" or baby_time.lower() == "d":
                print(f"Incorrect. +0 points! Points = {points}")

        # if they dont want kids
        if kids.lower() == "a":
            print("Okay, you're going to adopt an animal from a shelter instead so you don't get lonely :)")
            print(" ")
            print("What pet would you like to adopt? (No wrong answers!)")
            print("a. puppy")
            print("b. kitten")
            print("c. hamster")
            print("d. parrot")
            pet = input("Enter the letter of your choice: ")
            print("Here's a quick trivia question: what percentage of people in America own a pet?")
            print("a. 28%")
            print("b. 42%")
            print("c. 57%")
            print("d. 66%")
            adoption = input("Enter the letter of your choice here: ")
            if adoption.lower() == "a" or adoption.lower() == "b" or adoption.lower() == "c":
                print(f"Incorrect. +0 points! Points = {points}")
            elif adoption.lower() == "d":
                points += 2
                print(f"Correct answer! +2 points! Points = {points}")

        print(" ")
        continue5 = input("Type 'next' to continue through the next couple of years!: ")
        print(" ")

        # 50 years old
        print("Happy Birthday! You are officially 50 years old!")
        print(" ")

        # mid-life crisis
        print("Uh oh! You're going through a mid-life crisis! Here's a quick trivia question: ")
        print("What percentage of adults claim to have experienced a mid-life crisis?")
        print("a. 10-20%")
        print("b. 20-30%")
        print("c. 30-40%")
        print("d. 40-50%")
        midlife_crisis = input("Enter the letter of your choice: ")

        if midlife_crisis.lower() == "a":
            points += 2
            print(f"Correct answer! +2 points! Points = {points}")
        elif midlife_crisis.lower() == "b" or midlife_crisis.lower() == "c" or midlife_crisis.lower() == "d":
            print(f"Incorrect. +0 points! Points = {points}")

        print(" ")
        print("So, how do you want to deal with your crisis? (No wrong answers!)")
        print("a. Switch jobs")
        print("b. Buy a boat")
        print("c. Dye your hair hot pink")
        print("d. Take a swim in the hudson river")
        midlife_crisis = input("Enter the letter of your choice: ")

        # 65 years old
        print("Okay, you have recovered and it's your birthday! Happy Birthday! You are officially 65 years old!")
        print(" ")
        typing_next = input("Type 'next' to move on: ")

        print("You get to retire in Europe! Where do you want to go? (No wrong answers!)")
        print("a. Paris, France")
        print("b. London, England")
        print("c. Barcelona, Spain")
        print("d. Venice, Italy")
        retirement = input("Enter the letter of your choice: ")

        print(" ")

        # 85 years old
        print("You are having a great time in retirement and now its your birthday again! Happy Birthday! You are officially 85 years old!")
        print(" ")
        print("Since your health may be declining, here's a quick trivia question. If you answer correctly, you will live happily for ten more years. If you answer incorrectly...wait and see!")
        print(" ")

        print("How many bones are in the human body?")
        print("a. 196")
        print("b. 217")
        print("c. 187")
        print("d. 206")
        bones = input("Enter the letter of your choice: ")

        if bones.lower() == "a" or bones.lower() == "b" or bones.lower() == "c":
            print(f"Incorrect. +0 points! Points = {points}")
            print(" ")
            print(f"Oh no! You died, but don't worry -— it's the circle of life!")

        elif bones.lower() == "d":
            points += 5
            print(f"Correct answer! +5 points! Points = {points}")
            print(" ")
            print("You get to live another 10 years!")
            print(" ")
            print(" ")
            print("Happy Birthday! You are officially 95 years old! Wow!")
            print("You died a peaceful death, but don't worry -— it's the circle of life!")

        if points >= 15:
            print(f"You ended up with {points} points, which means you succeeded in life. Good job!")
        elif points < 15:
            print(f"You ended up with {points} points, which means you did not succeed in life. Better luck next time!")

        # flip() the display to put your work on screen [what does this mean help]
    pygame.display.flip()



    clock.tick(60)  # limits FPS to 60

    pygame.quit()

#call the main function
main()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     main('PyCharm')
