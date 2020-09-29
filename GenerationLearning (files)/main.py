from fuzzywuzzy import fuzz  #import but just from one part of the librari, just what i need
import random 
import string

#EXPLANATION OF THE CODE: we are trying to prove evolve algorithim we creating indiv. wich have a random.string the ones who match are able to reproduce.
#First step is creating the individual

class Agent: 

	def __init__(self,length): 

		self.string = ''.join(random.choice(string.letters) for _ in xrange(length)) # assigning to a member var.string , we generate a random string with the function random.choice from the librari random, wich picks a random value from a list 												     (string.letters==english alfabet), then the for repits the proces to get a string with the length we give to the class, last thing is .join will put together all the letters

		self.fitness = -1 #it is a score wich says that one individual is better than another, the ones who have higher scores are selected to move on to the next generation
	def __str__(self):
		
		return 'String: '+ str(self.string) + ' Fitness: ' + str(self.fitness)

#Global variables, not recomend to do it this way, is better if u can acces to it and change the values from the console
in_str = None
in_str_len = None
population = 20
generations = 2000

def generic_algor(): #code necesary in order to evolve
	
	agents = init_agents(population, in_str_len)	

	#Four primary fuctions of a generic algorithim:
	
	for generation in xrange(generations):
		
		print 'Generation: '+ str(generation)
	
		agents = fitness(agents)
		agents = selection(agents)
		agents = crossover(agents)
		agents = mutation(agents)
		
		if any(agent.fitness >=90 for agent in agents):
			
			print 'Threshold met!'
			exit(0)

def init_agents(population, length):
	
	return [Agent(length) for _ in xrange(population)]

def fitness(agents):
	
	for agent in agents:
		
		agent.fitness = fuzz.ratio (agent.string, in_str) #give us % how close the agent.string is from the input string(in_str)
 
	return agents	

def selection(agents):

	agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True) #sort the agents for they fitness value with a python fuction, reverse=True appears bc we want the biggest values first so it reverse the sort fuction
	print '\n'.join(map(str, agents)) 
	agents = agents[:int(0.2 * len(agents))] #we're selecting the most convienient agents of the list(20% of the agents will make it to the next gen)
	
	return agents

def crossover(agents):
	
	offspring = []
	
	for _ in xrange((population - len(agents)) / 2): # selects half part of the agents
		
		parent1 = random.choice(agents) #selects randomly their parents
		parent2 = random.choice(agents)
		child1 = Agent(in_str_len)	#generate their childs
		child2 = Agent(in_str_len)
		split =  random.randint(0, in_str_len) #generates a random split (int)
		child1.string = parent1.string[0:split] + parent2.string[split:in_str_len] #with the random split it gives one part of each parent string to the child
		child2.string = parent2.string[0:split] + parent1.string[split:in_str_len]
	
		offspring.append(child1)
		offspring.append(child2)
	
	agents.extend(offspring)
	
	return agents


def mutation(agents):
	
	for agent in agents:
		
		for idx, param in enumerate(agent.string): #chose a random letter from the string
		
			if random.uniform(0.0, 1.0) <= 0.1: # just happens 10% of the time
				
				
				agent.string = agent.string[0:idx] + random.choice(string.letters) + agent.string[idx+1:in_str_len] # if we mutate then what it does is it keeps the same string till that random letter(idx) then changes that letter for random one and keeps 																	the same string wich was at the tail 

	return agents
				
		
		
if __name__ =='__main__':
	
	in_str = 'Aleix'
	in_str_len = len(in_str)
	generic_algor()














