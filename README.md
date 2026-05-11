# Othello AI Project

This repository contains various Artificial Intelligence agents designed to play the game of **Othello** (also known as Reversi). The project explores classic search algorithms, heuristic optimization, and time-constrained decision-making.

## Project Structure

* **`othello.py`**: Core game logic including state representation, move generation, and scoring.
* **`game.py`**: Handles the game loop and player turns.
* **`agent.py`**: Implements the `RandomAgent`, `MinimaxAgent`, and `AlphaBeta` pruning agent.
* **`ehc35.py`**: Advanced agent using Iterative Deepening and a positional heuristic evaluation function.
* **`main.py`**: The entry point for running matches via the command line.
* **`run.sh`**: A shell script utility for easy execution.

---

## Implemented Agents

### 1. Random Agent
Selects moves randomly from the list of legal options. Used as a baseline for performance testing.

### 2. Minimax Agent
Explores all possible game states up to a specified depth. It seeks to maximize the score for the current player while assuming the opponent plays optimally.
* **Complexity:** $O(b^d)$

### 3. Alpha-Beta Agent
An optimized version of Minimax that prunes branches that cannot influence the final decision. This allows the agent to search deeper within the same time constraints.
* **Complexity:** Average $O(b^{d/2})$

### 4. Extra Agent (`ehc35`)
A high-performance agent that utilizes:
* **Iterative Deepening:** Gradually increases search depth until a time limit is reached.
* **Heuristic Evaluation:** Prioritizes **corners** and **edges** (strategic positions) rather than just raw piece count.

---

## How to Run

Run the game using the `run.sh` script by specifying two agents and a search constraint (depth for standard agents, milliseconds for the extra agent).

**Command Syntax:**
```bash
sh run.sh <agent1> <agent2> <depth_or_time>
