from Button import Button
from Settings import Settings


class Interface:
    def __init__(self):
        self.settings = Settings()

        self.buttons = [
            Button(25, 25, 200, 50, 'Options.png', action=lambda: self.settings.open())
        ]

    def click_buttons(self, pos):
        for button in self.buttons:
            button.process_click(pos)
