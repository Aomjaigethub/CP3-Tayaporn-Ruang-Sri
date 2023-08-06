class EggHatchingGame:
    def __init__(self):
        self.eggshell = 20                                          # the number of eggshells that need to be pecked before the egg hatches
        self.eggtype = ["brown egg", "white egg", "big white egg"]  # a list that contains three types of eggs
        self.baby = ["Chicken", "Duck", "Goose"]                    # a list that contains three types of baby animals
        self.playeregg = None                                       # will store the type of egg chosen by the player (initialized as None)
        self.game_over = False                                      # Will be a flag to indicate whether the game is over (False initially)

    def pick_an_egg(self):
        print("There are 3 eggs at your front door")
        print("1. Brown egg")
        print("2. White egg")
        print("3. Big white egg")
        selected_egg_index = int(input("Pick an egg you want (1/2/3): ")) - 1
        self.playeregg = self.eggtype[selected_egg_index] #นำค่าอินเด็กของชนิดไข่ มาเก็บในตัวแปร'playeregg'

    def start_hatching(self):
        if self.game_over:
            return

        while self.eggshell > 0:
            if self.eggshell == 15:
                print("----------------------------")
                print("Egg started to crack!")
                print("----------------------------")
                print("Keep pecking")
            elif self.eggshell == 8:
                print("----------------------------")
                print("The crack is getting bigger!")
                print("----------------------------")
                print("Keep pecking, Don't give up")
            elif self.eggshell == 1:
                print("----------------------------")
                print("The egg hatched!")
                print("----------------------------")
                self.end_game()
                self.game_over = True
                return
            else:
                # Wait for the player to type 'p' and press Enter to peck
                input("Type 'p' and press 'Enter' to peck!")

            self.eggshell -= 1


        print("You got a rotted egg")
        print("Try restarting the game")
        self.game_over = True

    def end_game(self):
        if self.playeregg == self.eggtype[0]:
            print("You got a", self.baby[0])
        elif self.playeregg == self.eggtype[1]:
            print("You got a", self.baby[1])
        elif self.playeregg == self.eggtype[2]:
            print("You got a", self.baby[2])
        else:
            print("Alien baby species")

    class BabyChick:
        def __init__(self):
            self.name = ""

        def peck(self):
            print("peck! peck!")
            self.eggshell -= 1

    def play(self):
        self.pick_an_egg()
        self.start_hatching()
        self.name = input("What would you like to name the baby?: ") #นำค่าชื่อที่ผู้ใช้ตั้งในไปเก็บในclass
        print("----------------------------")
        print("welcome to the world,", self.name)
        print("---------Game over----------")


if __name__ == "__main__":
    game = EggHatchingGame()
    game.play()
