import arcade
import arcade.gui
import notakto


class WelcomeWindow(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Notakto - CPSC 481 - Spring 2023", resizable=True)

        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # set background color
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

        # create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # create a text label
        ui_text_label = arcade.gui.UITextArea(text="Notakto",
                                              width=650,
                                              height=40,
                                              font_size=28,
                                              font_name="Arial")
        self.v_box.add(ui_text_label.with_space_around(bottom=12))

        text = "by, Chandra Lindy, " \
               "Alexander Au, " \
               "Dilhan Franco, " \
               "Frank Salgado-Gonzalez,"
        ui_text_label = arcade.gui.UITextArea(text=text,
                                              width=650,
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
            print("Start:", event)

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

    def on_click_start(self, event):
        print("Start:", event)

    def on_draw(self):
        self.clear()
        self.manager.draw()



if __name__ == "__main__":

  window = WelcomeWindow()
  arcade.run()
