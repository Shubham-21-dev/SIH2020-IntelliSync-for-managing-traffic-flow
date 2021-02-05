# traffic_management_M
We developed a software solution for smart management of traffic which leads to better travel plans, less stress due to driving, and optimized travel time.

Sync traffic signal timings to optimize split, cycle, and offset time.

It uses deep reinforcement learning to come with a policy function to identify pairs or groups of traffic signals which can be coordinated. Image Recognition is used to detect the presence of vehicles. One traffic signal will be aware of its adjacent traffic signal state and the number of vehicles arriving and departing there, which will help it make efficient decisions about when to release traffic, in which direction, and for how much time.

Whereas reinforcement learning is still a very active research area significant progress has been made to advance the field and apply it in real life. 

Application of Reinforcement Learning :
Reinforcement Learning in Gaming: 
Let’s look at an application in the gaming frontier, specifically AlphaGo Zero. Using reinforcement learning, AlphaGo Zero was able to learn the game of Go from scratch. It learned by playing against itself. After 40 days of self-training, Alpha Go Zero was able to outperform the version of Alpha Go known as Master that has defeated world number one Ke Jie. It only used black and white stones from the board as input features and a single neural network. A simple tree search that relies on the single neural network is used to evaluate positions moves and sample moves without using any Monte Carlo rollouts. 

Applications in Self Driving Cars:
Various papers have proposed Deep Reinforcement Learning for autonomous driving. In self-driving cars, there are various aspects to consider, such as speed limits at various places, drivable zones, avoiding collisions — just to mention a few. 
Some of the autonomous driving tasks where reinforcement learning could be applied include trajectory optimization, motion planning, dynamic pathing, controller optimization, and scenario-based learning policies for highways. 
For example, parking can be achieved by learning automatic parking policies. Lane changing can be achieved using Q-Learning while overtaking can be implemented by learning an overtaking policy while avoiding collision and maintaining a steady speed thereafter.

Application in NLP (Natural Language Processing):
In NLP, RL can be used in text summarization, question answering, and machine translation.

Applications in Healthcare:
In healthcare, patients can receive treatment from policies learned from RL systems. RL is able to find optimal policies using previous experiences without the need for previous information on the mathematical model of biological systems. It makes this approach more applicable than other control-based systems in healthcare. 
RL in healthcare is categorized as dynamic treatment regimes(DTRs) in chronic disease or critical care, automated medical diagnosis, and other general domains.
In DTRs the input is a set of clinical observations and assessments of a patient. The outputs are the treatment options for every stage. These are similar to states in RL. Application of RL in DTRs is advantageous because it is capable of determining time-dependent decisions for the best treatment for a patient at a specific time. 
The use of RL in healthcare also enables improvement of long-term outcomes by factoring the delayed effects of treatments. 

