# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 09:44:26 2024

@author: engeb
"""
import random
import math

#2.1

#Function for bernulli trial
def bernoulli_trial(p):
    rand = random.random() #generate a numeber between 1 and 0
    if rand <= p:  # if its a success
        return 1
    else:          # if its a failure
        return 0

trial2_1 = bernoulli_trial(0.5)
print(f"The results of the trial is {'a succsess' if trial2_1 == 1 else 'a failure'}")

#2.2
def trial_success(p,n):
    successes = 0
    for _ in range (n):
        if bernoulli_trial(p) == 1:
            successes += 1
    return successes

print(f"The number of successes is {trial_success(0.5, 10)}")

#2.3

#function to calculate expectations and standard deviations
def theoretical_trials_value(p, n):
    E = n*p #to calculate expectations
    #i couldnt find a way to properly import these functions from compulsory one.
    standard_dev = math.sqrt(n*p*(1-p)) #instead, i got some help from erik
    return E, standard_dev


def simulate_theoretical_trials(p, n_theo):
    for n in n_theo:
        E, standard_dev = theoretical_trials_value(p, n)
        print(f"For {n} trials")
        print(f"The theoretical expectations of the trials are {E}")
        print(f"while the theoretical standard deviation is {standard_dev}")
        #now to 
        sim_succ = trial_success(p, n) #to calculate the success of the trials
        #unfortunate naming conventions, i know, but its easier to write short
        print(f"The number of simulated successes is {sim_succ}")


#input for the probability and the number of trials
p = float(input("What is the probabilty? "))
if p < 0 or p > 1:
    #So the user doesn't go either over or under 1 and 0
    raise ValueError("Probability must be between 0 and 1.")
        

n = int(input("How many trials? "))
#theoretical number of trials
n_theo = [30,100]
#simulates repeated trials
simulate_theoretical_trials(p, n_theo)

trial2_3 = bernoulli_trial(p)
success = trial_success(p, n)

print() #for spacing
#display the final number of successes
print(f"The number of successes in {n} trials is {success}")
