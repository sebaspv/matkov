import numpy as np
from enum import Enum
import random

initialX = 0
initialY = 2
targetX = 3
targetY = 1
maxx = 4
maxy = 3
x = 0
y = 0

Dir = Enum("Dir", ["UP", "DOWN", "LEFT", "RIGHT"])

actions = [Dir.UP, Dir.DOWN, Dir.LEFT, Dir.RIGHT]

q = {}
for i in range(maxx):
    for j in range(maxy):
        q.update({(i, j): {Dir.UP: 0, Dir.DOWN: 0, Dir.LEFT: 0, Dir.RIGHT: 0}})

ACTIONS = {
    Dir.UP: (0, -1),
    Dir.DOWN: (0, 1),
    Dir.LEFT: (-1, 0),
    Dir.RIGHT: (1, 0)
}

def reset():
    global x, y
    x = initialX
    y = initialY
    return (x, y)

def in_target(newx, newy):
    return newx == targetX and newy == targetY

def in_bound(newx, newy):
    return (newx >= 0 and newx < maxx and
            newy >= 0 and newy < maxy)

def get_reward(newx, newy):
    if not in_bound(newx, newy):
        return -0.1
    if in_target(newx, newy):
        return 1.0
    else:
        return -0.01

def step(action):
    global x, y
    xx, yy = ACTIONS[action]
    done = False
    next_x = x + xx
    next_y = y + yy

    reward = get_reward(next_x, next_y)
    if in_bound(next_x, next_y):
        x, y = next_x, next_y
        if in_target(next_x, next_y):
            done = True

    return (x, y), reward, done

episodes = 20001

learning_rate_a = 0.9 # alpha/learning rate
discount_factor_g = 0.9 # gamma/discount factor.

epsilon = 0.8  # 1 = 100% Random walk
epsilon_decay_rate = 0.0001

rewards_per_episode = np.zeros(episodes)

for i in range(episodes):
    state = reset()

    terminated = False

    max_q_val = 0
    stepcount = 0
    while(not terminated):
        if np.random.uniform(0,1) <= epsilon:
            action = random.choice(actions)
        else:
            for a in actions:
                q_val = q[state][a]
                if q_val >= max_q_val:
                    action = a
                    max_q_val = q_val

        new_state,reward,terminated = step(action)
        stepcount+=1
        if reward == 1:
            rewards_per_episode[i] = stepcount
        q[state][action] = q[state][action] + learning_rate_a * (
                reward + discount_factor_g * np.max([v for k, v in q[new_state].items()]) - q[state][action]
            )
        state = new_state

    epsilon = max(epsilon - epsilon_decay_rate, 0)
    if(epsilon==0):
        learning_rate_a = 0.0001
    if i % 1000 == 0:
        print("Camino más corto de episodio", i, rewards_per_episode[i])

print("done")
