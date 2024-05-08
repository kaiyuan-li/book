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

If Q is already optimal, then there will be no update since \\(Q(S_t, A_t) = R_{t+1} + Q(S_{t+1}, A_{t+1})\\)

English: The Q value a t time t is updated to be the current predicted Q value plus the amount of value we expect in the future, given that we play optimally from our current state. \\( \gamma \\) is the discount factor. \\( max Q(S_{t+1}, a) \\) is the max Q value at state t+1 for all possible actions. This max Q at \\(S_{t+1}\\) is also the prediction from current model, but \\(R_{t+1}\\) will help update our prediction model.

The steps:
1. start the game at state \\(S_t\\)
1. using initial policy to predict next possible action by calculating all possible Q values
1. pick an action and observe a reward \\(R_{t+1}\\)
1. use algorithm to calculate maximum of \\(Q(S_{t+1}, a)\\)
1. update prediction with \\(Q(S_t, A_t) = Q(S_t, A_t) + \alpha[R_{t+1} + \gamma max Q(S_{t+1}, a) - Q(S_t, A_t) ]\\)

Here \\(\alpha\\) is learning rate and \\(\gamma\\) is discount factor.