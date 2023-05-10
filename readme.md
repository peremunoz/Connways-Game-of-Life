# Connway's Game of Life

## Important note

The game only supports initial states with matrix dimensions of 80x60. You can change this in the `main.py` file editing the `WIDTH` and `HEIGHT` constants.
The game is not optimized for performance, it is just a proof of concept.

## Usage

If you have the `pygame` module installed in your machine, just execute the following:
```bash
python3 main.py <execution mode> [random]
```
Where `<execution mode>` can be:

`auto`: Automatic execution mode. It will run the game automatically until the user stops it or the game ends.

`manual`: Manual execution mode. It will run the game step by step (pressing any key) until the user stops it or the game ends.

And `random` refers to the initial state of the game. If it is present, the initial state will be random. Otherwise, it will be loaded from the initialState.txt file.

You can quit the game at any time by pressing the X button of the window.

If not, you will need to run the program inside the virtual environment. For doing it, execute the following command inside the root folder:
```bash
pipenv shell
```
Then, execute the python program as specified above.

## Definition of the initial state

The initial state of the game is defined in the file `initialState.txt`. The file must contain a matrix of 0s and 1s, separated by a comma, where 0s represent dead cells and 1s represent alive cells. 

For example:

```
0,0,0,0,0,0,0,0,0,0
1,0,0,1,1,0,0,0,0,0
0,1,0,0,0,1,0,0,0,0
0,0,1,0,0,0,1,0,0,0
```
Where cells [1,0], [1,3], [1,4], [2,1], [2,5], [3,2], [3,6] are alive and the rest are dead.

## Output

The output of the program is printed in a graphical window. The window will be updated every iteration (in auto or manual mode). The window will be closed when the game ends.

## Requirements

The game needs the following library to be installed:

- Pygame

You can install it with the following command:

```bash
pip3 install pygame
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Pygame](https://www.pygame.org/)
- [Pygame documentation](https://www.pygame.org/docs/)

## Author

- **Pere Muñoz Figuerol** - [peremunoz]
