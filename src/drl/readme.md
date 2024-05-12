# Deep Reinforcement Learning in Action

## Model

Simply choosing the best action is called `greedy` method

Epsilon-greedy strategy is to have a small probability of epsilon that we choose an action randomly.

A variance of epsilon-greedy is *softmatch* selection. Where the randomness of picking is not uniform. But it depends on the performance so far.

\\[ Pr(A) = \frac{e^{Q_k(A)/\tau}}{\sum_{i=0}^n e^{Q_k(i)/\tau}} \\]

Probability of choosing an action of A is the value of choosing A over all possible values. Here \\( \tau \\) is called *temperature*. Higher temperature can cause more uniform selection.

A policy \\( \pi \\) is the strategy of an agent in some environments. For example, the strategy of the dealer in Blackjack is to always hit until they reach a card value of 17 or greater. In general, a policy is a function that maps a state to a probability distribution over the set of possible actions in that state.

\\[ \pi: s \rightarrow Pr(A|s) \\]

Optimal policy is the strategy that maximizes the rewards.

\\[ \pi_{optimal} = argmax E(R|\pi) \\]

Value functions are functions that map a state or a state-action pair to the *expected value*.

\\[ V_{\pi}: s \rightarrow E(R|s, \pi) \\]

A more general form of *value* is weighted sum of the rewards. Read as "the expected rewards given a policy \\(\ \pi \\) and a starting state s".

\\[ V_{\pi}(s) = \sum_{i=1}^t w_iR_i \\]

Above value function does not depend on action. A *Q function* or *Q value* means the value after taking action *a*:

\\[ Q_{\pi}: (s|a) \rightarrow E(R|a, s, \pi) \\]

Order of a tensor means how many indices are needed to address a single element. For scalar, no index is needed so it's 0-tensor, vector need one index so it's 1-tensor, etc.

## Deep Q-Networks (DQN)

Q-learning update rule

\\[ Q(S_t, A_t) = Q(S_t, A_t) + \alpha[R_{t+1} + \gamma max Q(S_{t+1}, a) - Q(S_t, A_t) ] \\]

If Q is already optimal, then there will be no update since \\(Q(S_t, A_t) = R_{t+1} + \gamma Q(S_{t+1}, A_{t+1})\\)

English: The Q value a t time t is updated to be the current predicted Q value plus the amount of value we expect in the future, given that we play optimally from our current state. \\( \gamma \\) is the discount factor. \\( max Q(S_{t+1}, a) \\) is the max Q value at state t+1 for all possible actions. This max Q at \\(S_{t+1}\\) is also the prediction from current model, but \\(R_{t+1}\\) will help update our prediction model.

The steps:
1. start the game at state \\(S_t\\)
1. using initial policy to predict next possible action by calculating all possible Q values
1. pick an action and observe a reward \\(R_{t+1}\\)
1. use algorithm to calculate maximum of \\(Q(S_{t+1}, a)\\)
1. update prediction with \\(Q(S_t, A_t) = Q(S_t, A_t) + \alpha[R_{t+1} + \gamma max Q(S_{t+1}, a) - Q(S_t, A_t) ]\\)

Here \\(\alpha\\) is learning rate and \\(\gamma\\) is discount factor.

### PyTorch

```py
a = torch.Tensor([2.0])
a.requires_grad = True
b = torch.Tensor([1.0])
b.requires_grad = True
def linear_model(x, a, b):
    return a * x + b
x = torch.Tensor([4.0])
y = linear_model(x, a, b)
y.grad_fn # will give a AddBackward0 fn
with torch.no_grad():
    y = linear_model(x, a, b)
y.grad_fn # will give None
```

```py
y = linear_model(x, a, b)
y.backward() # do back propagation
a.grad # gives 4
b.grad # gives 1
```
In this case, without `no_grad()`, pytorch will calculate \\(\frac{\partial y}{\partial a}\\) and store it in `a.grad` after calling `backward()`.

### Catastrophic forgetting

In one case, agent go right and win, while in the next case, agent goes left and win. Agent will be very confused on how to play this game.

#### Experience Replay

1. in state s, take action a and observe the new state and reawd
1. store this experience in a tuple \\((s, a, s_{t+1}, r_{t+1})\\) and push to a memory list
1. once the memory is filled, randomly select a subset, iterate through the subset and calculate value updates for each subset. Store these as X and Y.
1. use X and Y as a mini-batch for batch training.

I think this one just reuses limited number of training data to perform more trainings. IDK how it resolves catastrophic forgetting.

### Improving stability with a target network

The agent may be confused because the reward is sparse, e.g. sometimes moving upwards get a large reward but sometimes very low reward. Agent is confused in those cases.

Target network takes snapshots of the Q network every N iterations. The usage of target network is when calculating the gradient, use prediction with target Q instead of Q. This can reduce the effect of recent updates on Q.

