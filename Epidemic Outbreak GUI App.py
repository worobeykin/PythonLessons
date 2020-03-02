#Epidemic Outbreak GUI App
import random, math, tkinter

class Simulation():
    def __init__(self):
        self.day_number = 1
        print("\nTo simulate an epidemic outbreak, we must know the population size.")
        population_size = int(input("Enter the population size: "))
        self.population_size = population_size

        root = math.sqrt(self.population_size)
        if int(root + .5)**2 != self.population_size: # int(8.881 +.5)**2 = int(9.3881)**2 = 9**2 = 81 != 79
            root = round(root, 0) # round(8.881, 0) = 9.0
            self.grid_size = int(root) #grid_size = 9
            self.population_size = self.grid_size**2 #population_size = 9*9 = 81 the closest PERFECT SQUARE TO 79
            print("Rounding population size to " + str(self.population_size) + " for visual purposes.")
        #The user did enter a perfect square for the population
        else:
            self.grid_size = int(math.sqrt(self.population_size))
        


        

        print("\nWe must first start by infecting a portion of the population.")
        infection_percent = int(input("--Enter the percentage (0-100) of the population to initially infect: ")) / 100
        self.infection_percent = infection_percent

        print("\nWe must know the risk a person has to contract the disease when exposed.")
        infection_probability = int(input("--Enter the probability (0-100) that a person gets infected when exposed to the disease: "))
        self.infection_probability = infection_probability

        print("\nWe must know how long the infection will last when exposed.")
        infection_duration = int(input("--Enter the duration (in days) of the infection: "))
        self.infection_duration = infection_duration

        print("\nWe must know the mortality rate of those infected.")
        mortality_rate = int(input("--Enter the mortality rate (0-100) of the infection: "))
        self.mortality_rate = mortality_rate

        print("\nWe must know how long to run the simulation.")
        sim_day = int(input("--Enter the number of days to simulate: "))
        self.sim_day = sim_day
        
class Person():
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, simulation_obj):
        chance_infected = random.randint(0, 100)
        if chance_infected < simulation_obj.infection_probability:
            self.is_infected = True

    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        self.is_dead = True


    def update(self, simulation_obj):
        if self.is_dead == False:
            if self.is_infected:
                self.days_infected += 1
                die_chance = random.randint(0, 100)
                if die_chance < simulation_obj.mortality_rate:
                    self.die()
                elif self.days_infected == simulation_obj.infection_duration:
                    self.heal()
                
class Population():
    def __init__(self, simulation_obj):
        self.population = []
        for i in range(simulation_obj.grid_size):
            row = []
            for j in range(simulation_obj.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)

    def initial_infection(self, simulation_obj):
        infected_count = int(round(simulation_obj.infection_percent*simulation_obj.population_size, 0))

        infections = 0

        while infections < infected_count:
            x = random.randint(0, simulation_obj.grid_size - 1)
            y = random.randint(0, simulation_obj.grid_size - 1)
            #If the person is not infected, infect them!
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1
            

    def spread_infection(self, simulation_obj):
        #Loop through all rows of the population
        for i in range(simulation_obj.grid_size):
            #Loop through all of the Person objects in a given row
            for j in range(simulation_obj.grid_size):
                #Check to see if this given person self.population[i][j] is not
                if self.population[i][j].is_dead == False:
                    #Check to see if we need to infect this person.
                    #We will try infect the given person if an adjacent person is already infected
                    #If i == 0, we are in the first row so, we can't look above
                    if i == 0:
                        #If j == 0, we are in the first column, so we can't look left.
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)
                        #If we are in the last column, we can't look right
                        elif j == simulation_obj.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)
                        #If we are in any other column, we can look left, right, 160 or below
                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)
                    #If i == simulation.grid_size -1 we are in the last row, so we can't look below
                    elif i == simulation_obj.grid_size-1:
                        #If j == 0, we are in the first column, so we can't look left.
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)
                        #If we are in the last column, we can't look right
                        elif j == simulation_obj.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)
                        #If we are in any other column, we can look left, right, or above
                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)
                    #Otherwise, we are in a row in between, we can look left, right, below or above
                    else:
                        #If j == 0, we are in the first column, so we can't look left.
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)
                        #If we are in the last column, we can't look right
                        elif j == simulation_obj.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)
                        #If we are in any other column, we can look left, right, below, or above
                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation_obj)

    def update(self, simulation_obj):
        simulation_obj.day_number += 1
        for row in self.population:
            #Loop through the row to update each Person
            for person in row:
                person.update(simulation_obj)

    
    def display_statistics(self, simulation_obj):
        total_infected_count = 0
        total_death_count = 0
        for row in self.population:
            for person in row:
                if person.is_infected:
                    total_infected_count += 1
                    if person.is_dead:
                        total_death_count += 1
        infected_percent = round(100*(total_infected_count / simulation_obj.population_size), 4)
        death_percent = round(100*(total_death_count / simulation_obj.population_size), 4)

        print("\n-----Day # " + str(simulation_obj.day_number) + "-----")
        print("Percentage of Population Infected: " + str(infected_percent) + "%")
        print("Percentage of Population Dead: " + str(death_percent) + "%")
        print("Total People Infected: " + str(total_infected_count) + " / " + str(simulation_obj.population_size))
        print("Total Deaths: " + str(total_death_count) + " / " + str(simulation_obj.population_size))

def graphics(simulation_obj, population, canvas):

    square_dimension = 600//simulation_obj.grid_size

    for i in range(simulation_obj.grid_size):
        #y is the starting index of where a given square should be drawn
        y = i*square_dimension
        #Loop through all persons in the row
        for j in range(simulation_obj.grid_size):
            #x is the starting index of where a given square should be drawn.
            x = j*square_dimension
            #Check to see if the given person is dead
            if population.population[i][j].is_dead:
                #Create a red square at the correct location
                canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='red')
            #The current person is not dead, check if they are infected or healthy
            else:
                if population.population[i][j].is_infected:
                    #Create a yellow square at the correct location
                     canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='yellow')
                else:
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='green')

        
#Main Code
current_simulation = Simulation()


WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")
sim_canvas = tkinter.Canvas(sim_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='lightblue')
sim_canvas.pack(side=tkinter.LEFT)

current_population = Population(current_simulation)

current_population.initial_infection(current_simulation)
current_population.display_statistics(current_simulation)


input("\nPlease press enter to being the simulation")

for day in range(1, current_simulation.sim_day):
    current_population.spread_infection(current_simulation)
    current_population.update(current_simulation)
    current_population.display_statistics(current_simulation)
    graphics(current_simulation, current_population, sim_canvas)
    sim_window.update()

    if day != current_simulation.sim_day - 1:
        sim_canvas.delete('all')
