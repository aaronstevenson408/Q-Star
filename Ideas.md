
# Building Blocks

## Create an A* algorithm
- Understand how it works
    * Implement the algorithm
    * Test on sample data

## Understand Q-Learning
- Learn the Q-Learning algorithm
    * Understand how it works
    * Tune hyperparameters
    
## Combine Q-Learning with A*
- Integrate the two algorithms
- Test in sample environments
    - Mazes
    - Node trees

# Proof of Concept

- Create a dataset that ranks different outputs of LLMs (use LAION Open Assistant model to generate synthetic data)

- Create a model that ranks each sentence (different parameter constraints could make different personalities)

- Then combine token generation, rank x token choices with the model ranking model, use A* to choose best path that ranks the best
