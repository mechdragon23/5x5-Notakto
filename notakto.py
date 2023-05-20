import arcade
from arcade.gui import UIManager
from games import *
from project import *
import time

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
SCREEN_TITLE = "Notakto - CPSC 481 - Spring 2023"

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
            if self.window.current_view == self:
                game_view = GameView()
                game_view.setup()
                self.window.show_view(game_view)

        # create a settings button
        settings_button = arcade.gui.UIFlatButton(text="Settings", width=200)
        self.v_box.add(settings_button.with_space_around(bottom=5))

        # handle settings button click events
        @settings_button.event("on_click")
        def on_click_settings_button(event):
            pass
            # if self.window.current_view == self:
            #     settings_view = SettingsView()
            #     self.window.show_view(settings_view)

        # create a quit button
        quit_button = arcade.gui.UIFlatButton(text="Quit", width=200)
        self.v_box.add(quit_button.with_space_around(bottom=5))

        # handle quit button click events
        @quit_button.event("on_click")
        def on_click_quit_button(event):
            if self.window.current_view == self:
                arcade.exit()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_draw(self):
        self.clear()
        self.manager.draw()

class SettingsView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.clear()
        self.manager.draw()

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # create empty game board
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.board = [[0 for i in range(COLUMN_COUNT)] for j in range(ROW_COUNT)]
        self.game = Notakto(self.board)
        self.board_sprite_list = arcade.SpriteList()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = column * (WIDTH + MARGIN) + (WIDTH / 2 + MARGIN)
                y = row * (HEIGHT + MARGIN) + (HEIGHT / 2 + MARGIN)
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.board_sprite_list.append(sprite)
        self.state = self.game.initial

    def resync_board_with_sprites(self):
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                pos = row * COLUMN_COUNT + column
                if self.board[row][column] == 0:
                    self.board_sprite_list[pos].color = arcade.color.WHITE
                else:
                    self.board_sprite_list[pos].color = arcade.color.GREEN

    def on_draw(self):
        # This command has to happen before we start drawing
        self.clear()
        self.board_sprite_list.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        # Change the x/y screen coordinates to grid coordinates
        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        # check boundry
        if row >= ROW_COUNT or column >= COLUMN_COUNT:
            return

        if self.state.to_move == 'Min' and self.board[row][column] == 0:
            self.board[row][column] = 1
            self.resync_board_with_sprites()

            move = (row, column)
            state = self.game.result(self.state, move)
            self.state = state

            # check if player made a losing move
            if self.game.is_lose_condition(state):
                game_over_view = GameOverView(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.window.show_view(game_over_view)

    def on_update(self, delta_time):
        state = self.state
        player = state.to_move

        if player == 'Max':
            move = AI_hard(self.game, state)
            state = self.game.result(state, move)
            self.state = state

            row, col = move
            self.board[row][col] = 1

            self.resync_board_with_sprites()

            if self.game.is_lose_condition(state):
                game_over_view = GameOverView(SCREEN_WIDTH, SCREEN_HEIGHT)
                self.window.show_view(game_over_view)

        else: return

class GameOverView(arcade.View):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.texture = arcade.load_texture("game_over.png")
        self.screen_width = screen_width
        self.screen_height = screen_height


    def on_draw(self):
        self.clear()
        self.texture.draw_sized(self.screen_width / 2, self.screen_height / 2,
                                self.screen_width, self.screen_height)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        start_view = StartView()
        self.window.show_view(start_view)

if __name__ == "__main__":

  window = arcade.Window(SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, resizable=True)
  start_view = StartView()
  window.show_view(start_view)
  arcade.run()
