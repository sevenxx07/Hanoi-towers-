from blockworld import BlockWorldEnv
import random
import numpy as np
 
class QLearning():
    # don't modify the methods' signatures!
    def __init__(self, env: BlockWorldEnv):
        self.env = env
        self.q_func = dict()
 
    def train(self):
        # Use BlockWorldEnv to simulate the environment with reset() and step() methods.
        #break_point = 9000
        #my_point = 0
        while True:
            #my_point += 1
            s = self.env.reset()
            state = s[0]
            goal = s[1]
            done = False
            discount_factor = 0.9
            learning_rate = 0.9
            epsilon = 0.9
            state_dict = dict()
            if goal in self.q_func:
                state_dict = self.q_func[goal]
 
            while done != True:
                action_dict = dict()
 
                if state in state_dict:
                    action_dict = state_dict[state]
                else:
                    for action in state.get_actions():
                        action_dict[action] = 0
                best_action = max(action_dict, key=action_dict.get)
 
                if np.random.random() < epsilon:
                    my_action = best_action
                else:
                    my_action = random.choice(list(action_dict.keys()))
 
                s_, r, done = self.env.step(my_action)
                new_state = s_[0]
 
                action_dict_ = dict()
                if new_state in state_dict:
                    action_dict_ = state_dict[new_state]
                else:
                    for action in new_state.get_actions():
                        action_dict_[action] = 0
 
                my_q = action_dict[my_action]
 
                new_values = action_dict_.values()
                max_new_q = max(new_values)
 
                difference = r +(discount_factor * max_new_q) - my_q
 
                new_q = my_q + (learning_rate * difference)
 
                action_dict[my_action] = new_q
 
                state_dict[state] = action_dict
                state_dict[new_state] = action_dict_
                state = new_state
            self.q_func[goal] = state_dict
 
 
 
 
    def act(self, s):
        state = s[0]
        goal = s[1]
        state_dict = self.q_func[goal]
        if state in state_dict:
            action_dict = state_dict[state]
            return_act = max(action_dict, key=action_dict.get)
        else:
            return_act = random.choice(s[0].get_actions())
        return return_act
 
 
if __name__ == '__main__':
    # Here you can test your algorithm. Stick with N <= 4
    N = 4
 
    env = BlockWorldEnv(N)
    qlearning = QLearning(env)
 
    # Train
    qlearning.train()
 
    # Evaluate
    test_env = BlockWorldEnv(N)
 
    test_problems = 10
    solved = 0
    avg_steps = []
 
    for test_id in range(test_problems):
        s = test_env.reset()
        done = False
 
        print(f"\nProblem {test_id}:")
        print(f"{s[0]} -> {s[1]}")
 
        for step in range(50):  # max 50 steps per problem
            a = qlearning.act(s)
            s_, r, done = test_env.step(a)
 
            print(f"{a}: {s[0]}")
 
            s = s_
 
            if done:
                solved += 1
                avg_steps.append(step + 1)
                break
 
    avg_steps = sum(avg_steps) / len(avg_steps)
    print(f"Solved {solved}/{test_problems} problems, with average number of steps {avg_steps}.")
