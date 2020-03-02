#Epidemic Outbreak Terminal App
import random

class Simulation():
    def __init__(self):
        self.day_number = 1
        print("\nTo simulate an epidemic outbreak, we must know the population size.")
        population_size = int(input("Enter the population size: "))
        self.population_size = population_size

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
        for i in range(simulation_obj.population_size):
            person = Person()
            self.population.append(person)

    def initial_infection(self, simulation_obj):
        infected_count = int(round(simulation_obj.infection_percent*simulation_obj.population_size, 0))
        for i in range(infected_count):
            self.population[i].is_infected = True
            self.population[i].days_infected = 1
            
        random.shuffle(self.population)

    def spread_infection(self, simulation_obj):
        for i in range(len(self.population)):
            if self.population[i].is_dead == False:
                if i == 0:
                    if self.population[i+1].is_infected:
                        self.population[i].infect(simulation_obj)
                elif i < len(self.population) - 1:
                    if self.population[i+1].is_infected or self.population[i-1].is_infected:
                        self.population[i].infect(simulation_obj)
                elif i == len(self.population) - 1:
                    if self.population[i-1].is_infected:
                        self.population[i].infect(simulation_obj)

    def update(self, simulation_obj):
        simulation_obj.day_number += 1
        for person in self.population:
            person.update(simulation_obj)

    
    def display_statistics(self, simulation_obj):
        total_infected_count = 0
        total_death_count = 0
        for person in self.population:
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

    def graphics(self):
        status = []
        for person in self.population:
            if person.is_dead:
                char = 'X'
            else:
                if person.is_infected:
                    char = 'I'
                else:
                    char = 'O'
            status.append(char)

        for i in status:
            print(i, end='-')
        
#Main Code
current_simulation = Simulation()
current_population = Population(current_simulation)

current_population.initial_infection(current_simulation)
current_population.display_statistics(current_simulation)
current_population.graphics()

input("\nPlease press enter to being the simulation")

for day in range(1, current_simulation.sim_day):
    current_population.spread_infection(current_simulation)
    current_population.update(current_simulation)
    current_population.display_statistics(current_simulation)
    current_population.graphics()

    if day != current_simulation.sim_day - 1:
        input("\nPress enter to advance to the next day.")
    


            
                
                
        
        
                    
                        
                
                
            
            

    
            





















    
