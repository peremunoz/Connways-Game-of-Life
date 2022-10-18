# Connway's Game of Life

By Pere Muñoz Figuerol

## Important note

The game only supports initial states with matrix dimensions of 80x60. You can change this in the `main.cpp` file editing the `WIDTH` and `HEIGHT` constants.
The game is not optimized for performance, it is just a proof of concept.

## Usage

```bash
python3 main.py <execution mode> [random]
```

Where `<execution mode>` can be:

`auto`: Automatic execution mode. It will run the game automatically until the user stops it or the game ends.

`manual`: Manual execution mode. It will run the game step by step until the user stops it or the game ends.

And `random` refers to the initial state of the game. If it is present, the initial state will be random. Otherwise, it will be loaded from the initialState.txt file.

You can quit the game at any time by pressing the X button on the window.

## Definition of the initial state

The initial state of the game is defined in the file `initial_state.txt`. The file must contain a matrix of 0s and 1s, separated by a comma, where 0s represent dead cells and 1s represent alive cells. 

For example:

```
0,0,0,0,0,0,0,0,0,0
1,0,0,1,1,0,0,0,0,0
0,1,0,0,0,1,0,0,0,0
0,0,1,0,0,0,1,0,0,0
```

## Output

The output of the program is printed in a graphical window. The window will be updated every iteration (in auto or manual mode). The window will be closed when the game ends.

## Requirements

The game needs the following library to be installed:

- Pygame