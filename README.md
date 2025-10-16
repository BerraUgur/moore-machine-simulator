# Moore Machine Simulator
Moore Machine Simulator is a Python application for modeling, simulating, and visualizing Moore finite state machines. The project allows users to define states, input and output alphabets, transition and output tables, and to simulate the machine's behavior interactively or via text files.

## Features
- Interactive definition of states, input symbols, and output symbols
- Transition and output table creation via user input
- Step-by-step simulation of input strings, showing state transitions and outputs
- Clear tabular visualization of transitions and outputs
- No external dependencies, pure Python 3

## Getting Started

### Installation
Clone the repository or download the source code:

```bash
git clone https://github.com/BerraUgur/moore-machine-simulator.git
cd moore-machine-simulator
```

### Usage
Run the simulator:

```bash
python moore.py
```

Follow the on-screen prompts to define your Moore machine and simulate input strings.

## Input Format
You can define the machine interactively with the following format:

```
Q: {q0, q1, q2, ..., qN}
Σ = {a, b}
Γ = {0, 1}
```

Transition and output tables should be tab-separated, with headers in the first row and columns representing states and transitions.

## Example
Transition Table:

| Old State | After input a | After input b | Character printed |
|-----------|--------------|--------------|------------------|
| q0        | q1           | q0           | 0                |
| q1        | q2           | q0           | 0                |
| q2        | q3           | q0           | 0                |
| q3        | q1           | q0           | 1                |

Simulation:

```
Input String:  a a a b a b b a a b b
State:         q0 q1 q2 q3 q1 q0 q1 q2 q3 q1 q0
Output:        0  0  0  0  1  0  0  0  1  0  0
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
