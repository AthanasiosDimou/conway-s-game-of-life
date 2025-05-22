# Conway's Game of Life
#!/usr/bin/env python

import pygame
import numpy as np
import ctypes

# Initialize Pygame
pygame.init()

# Get system metrics
user32 = ctypes.windll.user32
SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

# Set window size to 80% of screen size
WINDOW_WIDTH = int(SCREEN_WIDTH * 0.8)
WINDOW_HEIGHT = int(SCREEN_HEIGHT * 0.8)

# Constants
COLUMNS: int = 140
LINES: int = 60

# Colors
BLACK = (0, 0, 0)
DARK_GRAY = (30, 30, 30)  # Dark background
LIGHT_GRAY = (180, 180, 180)  # Light squares
GRID_COLOR = (50, 50, 50)  # Darker grid lines
GREEN = (0, 255, 0)

# Initialize the grid
grid = np.zeros((LINES, COLUMNS))

# Create a font object for the button text
font = pygame.font.Font(None, 36)

# Create the play button
button_rect = pygame.Rect(375, 550, 100, 30)
play_text = font.render("Play", True, BLACK)
play_text_rect = play_text.get_rect(center=button_rect.center)

def count_neighbors(x, y):
    """Count the number of live neighbors for a cell."""
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            row = (x + i) % LINES
            col = (y + j) % COLUMNS
            total += grid[row][col]
    return total

def update_grid():
    """Update the grid according to Conway's Game of Life rules."""
    global grid
    new_grid = grid.copy()
    for i in range(LINES):
        for j in range(COLUMNS):
            neighbors = count_neighbors(i, j)
            if grid[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    grid = new_grid

def main(window_height:int = WINDOW_HEIGHT, window_width: int = WINDOW_WIDTH):
    global grid
    running = True
    playing = False
    clock = pygame.time.Clock()
    cell_size = 20  # Fixed cell size
    
    
    # Initialize screen at the start of main
    screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    pygame.display.set_caption("Conway's Game of Life")

    # Update button rectangle position based on initial window size
    button_rect.x = window_width // 2 - 50
    button_rect.y = window_height - 40
    play_text_rect.center = button_rect.center

    start_drag_pos = None  # Initialize start_drag_pos
    
    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.VIDEORESIZE:
                window_width = event.w
                window_height = event.h
                screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                # Update button rectangle position based on new window size
                button_rect.x = window_width // 2 - 50
                button_rect.y = window_height - 40
                play_text_rect.center = button_rect.center

            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[2]:  # Right button is held down
                    if start_drag_pos is not None:  # Ensure start_drag_pos is initialized
                        # Get the current mouse position
                        mouse_pos = pygame.mouse.get_pos()
                        # Calculate the start and end positions for drag selection
                        start_x, start_y = start_drag_pos
                        end_x, end_y = mouse_pos
                        # Determine the range of cells to select
                        x_start = min(start_x // cell_size, end_x // cell_size)
                        x_end = max(start_x // cell_size, end_x // cell_size)
                        y_start = min(start_y // cell_size, end_y // cell_size)
                        y_end = max(start_y // cell_size, end_y // cell_size)
                        # Select the cells in the range
                        for i in range(y_start, y_end + 1):
                            for j in range(x_start, x_end + 1):
                                if 0 <= i < LINES and 0 <= j < COLUMNS:
                                    grid[i][j] = 1  # Set cell to alive

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if event.button == 1:  # Left click
                    # Check if play button was clicked
                    if button_rect.collidepoint(mouse_pos):
                        playing = not playing
                    # Check if grid was clicked
                    elif mouse_pos[1] < screen.get_height() - 50:  # Above the button
                        x = mouse_pos[1] // cell_size
                        y = mouse_pos[0] // cell_size
                        if 0 <= x < LINES and 0 <= y < COLUMNS:
                            grid[x][y] = 1 - grid[x][y]  # Toggle cell state
                elif event.button == 3:  # Right click
                    start_drag_pos = mouse_pos  # Store the starting position for drag selection

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:  # Right button released
                    start_drag_pos = None  # Reset the starting position for drag selection
                    
        # Clear the screen
        screen.fill(DARK_GRAY)

        # Draw the grid
        for i in range(LINES):
            for j in range(COLUMNS):
                cell_rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, LIGHT_GRAY if grid[i][j] else DARK_GRAY, cell_rect)
                pygame.draw.rect(screen, GRID_COLOR, cell_rect, 1)

        # Draw the play button
        pygame.draw.rect(screen, GREEN if playing else DARK_GRAY, button_rect)
        pygame.draw.rect(screen, LIGHT_GRAY, button_rect, 2)
        screen.blit(play_text, play_text_rect)

        # Update the display
        pygame.display.flip()

        # Update the grid if playing
        if playing:
            update_grid()
            clock.tick(5)  # Control the speed of updates

    pygame.quit()

if __name__ == "__main__":
    main()
