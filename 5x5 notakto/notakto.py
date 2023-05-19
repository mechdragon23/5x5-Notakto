import arcade
from arcade.gui import UIManager
from games import *
from project import *

# Set how many rows and columns we will have
ROW_COUNT = 15
COLUMN_COUNT = 15

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "15 x 15 Notakto"

class StartView(arcade.View):
    def __init__(self):
        super().__init__()

        # a UIManager to handle the UI.
        self.manager = UIManager()
        self.manager.enable()

        # set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # create a text label
        ui_text_label = arcade.gui.UITextArea(text="Notakto",
                                              width=500,
                                              height=40,
                                              font_size=28,
                                              font_name="Arial")
        self.v_box.add(ui_text_label.with_space_around(bottom=12))

        text = "by, Chandra Lindy, " \
               "Alexander Au, " \
               "Dilhan Franco, \n" \
               "Frank Salgado-Gonzalez,"
        ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=500,
                                              height=60,
                                              font_size=14,
                                              font_name="Arial")
        self.v_box.add(ui_text_label.with_space_around(bottom=80))

        text = "Just like Tic-Tac-Toe but not really... \n" \
               "try not to get three in a row... \n" \
               "see if you can beat our Hard AI. GLHF! \n"
        ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=350,
                                              height=80,
                                              font_size=15,
                                              bold=True,
                                              font_name="Arial")
        self.v_box.add(ui_text_label.with_space_around(bottom=12))

        # create a start button
        start_button = arcade.gui.UIFlatButton(text="Start Game", width=200)
        self.v_box.add(start_button.with_space_around(bottom=5))

        # handle start button click events
        @start_button.event("on_click")
        def on_click_start_button(event):
            game_view = GameView()
            self.window.show_view(game_view)

        # create a settings button
        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=5))

        # handle settings button click events
        @settings_button.event("on_click")
        def on_click_settings_button(event):
            print("Settings:", event)

        # create a quit button
        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=5))

        # handle quit button click events
        @quit_button.event("on_click")
        def on_click_quit_button(event):
            arcade.exit()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    # def on_click_start(self, event):
    #     game_view = GameView()
    #     self.window.show_view(game_view)

    def on_draw(self):
        self.clear()
        self.manager.draw()


class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()
        # a UIManager to handle the UI.
        # self.manager = arcade.gui.UIManager()
        # self.manager.enable()

        # set background color
        # arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)


    def on_draw(self):
        self.clear()
        self.manager.draw()



class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        """
        Set up the application.
        """
        super().__init__()
        # create empty game board
        self.board = [[0 for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]
        self.game = Notakto(self.board)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.board = [[0 for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]

        self.game = Notakto(self.board)

        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.board[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        # print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.game.state.to_move == 'Min' and self.board[row][column] == 0:
                self.board[row][column] = 1
                move = (row, column)
                state = self.game.result(self.game.state, move)
                self.game.state = state

                # check if player made a losing move
                if self.game.is_lose_condition(state):
                    # print('Game Over')
                    game_over_view = GameOverView(SCREEN_WIDTH, SCREEN_HEIGHT)
                    # game_over_view.setup()
                    self.window.show_view(game_over_view)
            # else:
            #     self.board[row][column] = 0

    def on_update(self, delta_time):
        state = self.game.state or self.game.initial
        player = state.to_move

        if player == 'Max':
            move = AI_hard(self.game, state)
            state = self.game.result(state, move)
            self.game.state = state

            row, col = move
            self.board[row][col] = 1

            if self.game.terminal_test(state):
                print('Game Over')
                arcade.exit()

        if player == 'Min':
            return

class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self, screen_width, screen_height):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("game_over.png")
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        # arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(self.screen_width / 2, self.screen_height / 2,
                                self.screen_width, self.screen_height)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        start_view = StartView()
        # start_view.setup()
        self.window.show_view(start_view)



if __name__ == "__main__":

  window = arcade.Window(530, 530, "Notakto - CPSC 481 - Spring 2023", resizable=True)
  start_view = StartView()
  # start_view.setup()
  window.show_view(start_view)
  arcade.run()
