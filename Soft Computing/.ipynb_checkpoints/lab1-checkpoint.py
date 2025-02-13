import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create Antecedent/Consequent objects for temperature and fan speed.
temp=ctrl.Antecedent(np.arange(0,101,1),'temperature')
fan_speed=ctrl.Consequent(np.arange(0,101,1),'fan_speed')

# Define membership functions for temperature.
temp['low']=fuzz.trimf(temp.universe,[0,0,50])
temp['medium']=fuzz.trimf(temp.universe,[0,50,100])
temp['high']=fuzz.trimf(temp.universe,[50,100,100])

# Define membership functions for fan_speed.
fan_speed['low']=fuzz.trimf(fan_speed.universe,[0,0,50])
fan_speed['medium']=fuzz.trimf(fan_speed.universe,[0,50,100])
fan_speed['high']=fuzz.trimf(fan_speed.universe,[50,100,100])

# Define Fuzzy Rule.
rule1=ctrl.Rule(temp['low'],fan_speed['low'])
rule2=ctrl.Rule(temp['medium'],fan_speed['medium'])
rule3=ctrl.Rule(temp['high'],fan_speed['high'])

# Create control system and add rule.
fan_ctrl=ctrl.ControlSystem([rule1,rule2,rule3])
fan_speed_ctrl=ctrl.ControlSystemSimulation(fan_ctrl)

# Input the tempurature value.
temp_value=75

# Pass the input to the control system.
fan_speed_ctrl.input['temperature']=temp_value

# Compute the result.
fan_speed_ctrl.compute()

# Print the output.
print('Fan Speed:- ',fan_speed_ctrl.output['fan_speed'])
# Plot membership functions and output.
temp.view()
fan_speed.view()
fan_speed.view(sim=fan_speed_ctrl)