# Conway's Game of Life (Pygame Implementation)

This is a Python implementation of John Conway's Game of Life, a cellular automaton devised by the British mathematician John Horton Conway in 1970. It's a zero-player game, meaning its evolution is determined by its initial state, requiring no further input.

This implementation uses Pygame for the graphical interface and NumPy for efficient grid manipulation.

## Features

*   **Visual Simulation:** Watch the patterns evolve on a grid.
*   **Interactive Cell Placement:**
    *   **Left-click** on a cell to toggle its state (alive/dead).
    *   **Right-click and drag** to set multiple cells to alive.
*   **Play/Pause Control:** A "Play" button to start and stop the simulation.
*   **Resizable Window:** The game window can be resized, and the layout (including the play button) adapts.
*   **Dynamic Sizing:** The initial window size is set to 80% of your screen's dimensions.
*   **Configurable Grid:** The number of `LINES` and `COLUMNS` can be adjusted in the script.
*   **Clear Visuals:** Uses distinct colors for live cells, dead cells, and the grid.

## Requirements

*   Python 3.x
*   Pygame: `pip install pygame`
*   NumPy: `pip install numpy`
*   `ctypes` (standard Python library, used for getting screen dimensions)

## How to Run

1.  **Save the Code:** Save the provided Python script as a `.py` file (e.g., `game_of_life.py`).
2.  **Install Dependencies:** If you haven't already, install Pygame and NumPy:
    ```bash
    pip install pygame numpy pywin32
    ```
3.  **Run the Script:** Execute the script from your terminal:
    ```bash
    python game_of_life.py
    ```
    Or, if you're on a Unix-like system and have made the script executable (`chmod +x game_of_life.py`):
    ```bash
    ./game_of_life.py
    ```

## Controls

*   **Left Mouse Click (on Grid):** Toggles the state of the clicked cell (alive to dead, or dead to alive).
*   **Right Mouse Click + Drag (on Grid):** Sets all cells within the dragged area to "alive".
*   **Left Mouse Click (on "Play" Button):** Starts or pauses the simulation. The button color changes to green when playing.
*   **Resize Window:** Drag the window borders to resize. The game elements will adjust.
*   **Close Window:** Click the window's close button to quit the application.

## Code Overview

*   **Initialization:**
    *   Pygame is initialized.
    *   Screen dimensions are fetched using `ctypes` to set an initial window size (80% of screen).
    *   Constants for grid `COLUMNS`, `LINES`, and colors are defined.
    *   The game `grid` is initialized as a NumPy array of zeros.
*   **`count_neighbors(x, y)`:**
    *   Calculates the number of live neighbors for a given cell `(x, y)`.
    *   Handles wraparound for cells at the edges of the grid (toroidal array).
*   **`update_grid()`:**
    *   Applies the rules of Conway's Game of Life to each cell:
        1.  Any live cell with fewer than two live neighbours dies (underpopulation).
        2.  Any live cell with two or three live neighbours lives on to the next generation.
        3.  Any live cell with more than three live neighbours dies (overpopulation).
        4.  Any dead cell with exactly three live neighbours becomes a live cell (reproduction).
    *   Updates the global `grid` with the new state.
*   **`main()` Function:**
    *   Sets up the Pygame screen and caption.
    *   Manages the main game loop.
    *   **Event Handling:**
        *   `QUIT`: Exits the game.
        *   `VIDEORESIZE`: Handles window resizing and updates UI element positions.
        *   `MOUSEMOTION` (with right-button pressed): Handles drag-selection to activate cells.
        *   `MOUSEBUTTONDOWN`:
            *   Left-click: Toggles cell state or interacts with the "Play" button.
            *   Right-click: Initiates drag-selection.
        *   `MOUSEBUTTONUP`: Resets drag-selection state.
    *   **Rendering:**
        *   Clears the screen.
        *   Draws the grid cells based on their state.
        *   Draws the "Play" button.
        *   Updates the display.
    *   **Simulation Logic:** If `playing` is true, calls `update_grid()` and controls the simulation speed using `clock.tick(5)` (approximately 5 frames/generations per second).

## Customization

*   **Grid Size:** Modify `COLUMNS` and `LINES` constants at the top of the script to change the grid dimensions.
*   **Colors:** Change the `BLACK`, `DARK_GRAY`, `LIGHT_GRAY`, `GRID_COLOR`, `GREEN` tuples to alter the appearance.
*   **Simulation Speed:** Change the value in `clock.tick(5)` within the `main` loop's `if playing:` block to speed up or slow down the simulation.

## Potential Enhancements

*   Add a "Clear Grid" button.
*   Implement a speed control slider or keyboard shortcuts.
*   Allow users to save and load patterns.
*   Add more predefined patterns (e.g., glider, spaceship).
*   Option to change cell size dynamically.
*   More sophisticated visual themes.

---

Feel free to contribute or modify this Game of Life implementation!
