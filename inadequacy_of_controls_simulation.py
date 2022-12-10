import numpy as np
from scipy.stats import ttest_ind

""" setup random number generator for reproducibility """
rng = np.random.default_rng(seed=42)

""" define constants """
num_measurements = 5
control_x = 1
experiment_x = control_x + 1

""" 
real relationship of the system is a multiplicative interaction: z = y*x

'y' is an unknown variable to the experimenter, which is attempted to be controlled for with a control group.
In the first environment, y = 2 while in the second environment y = 1.

The experimental group receives an increased level of the independent variable x, and the dependent variable z is measured with noise.

"""

""" environment 1 """
y = 2

control_group_1 = control_x*np.ones(num_measurements)*y+rng.standard_normal(size=num_measurements)
experimental_group_1 = experiment_x*np.ones(num_measurements)*y+rng.standard_normal(size=num_measurements)


environment_1_results = ttest_ind(control_group_1,experimental_group_1)


""" environment 2 """
y = 1

control_group_2 = control_x*np.ones(num_measurements)*y+rng.standard_normal(size=num_measurements)
experimental_group_2 = experiment_x*np.ones(num_measurements)*y+rng.standard_normal(size=num_measurements)


environment_2_results = ttest_ind(control_group_2,experimental_group_2)

""" results """
print('Environment 1 p-value: ' + str(environment_1_results[1])+'\n'+'Environment 2 p-value: ' + str(environment_2_results[1]))