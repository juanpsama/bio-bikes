
from tkinter.ttk import Frame, Button, OptionMenu
from tkinter import Tk, StringVar


class HeaderMenuFrame(Frame):
    def __init__(self, parent: Tk, controller):
        super().__init__(parent)
        self.controller = controller
        # Create the list of options for navigation
        options_list = [
            "SelectPacientFrame",
            "PacientDataFrame",
            "SelectImageInputFrame",
            "VideoAnalisisFrame",
            "WebcamImageInputFrame",
            "PacientInfoFrame"
        ]

        # Variable to keep track of the selected option
        self.value_inside = StringVar(self)
        self.value_inside.set("Select an Option")

        # Create the OptionMenu widget for navigation
        self.navigation_menu = OptionMenu(self, self.value_inside, *options_list, command=self.navigate)
        self.navigation_menu.grid(row=0, column=0, padx=5, pady=5)

        # Create the list of options for configuration
        config_options_list = [
            "Config Option 1",
            "Config Option 2",
            "Config Option 3"
        ]

        # Variable to keep track of the selected config option
        self.config_value_inside = StringVar(self)
        self.config_value_inside.set("Config Options")

        # Create the OptionMenu widget for configuration
        self.config_menu = OptionMenu(self, self.config_value_inside, *config_options_list, command=self.open_config)
        self.config_menu.grid(row=0, column=1, padx=5, pady=5)

        # Create logout button
        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=0, column=2, padx=5, pady=5)

        # Create exit button
        self.exit_button = Button(self, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=0, column=3, padx=5, pady=5)

    def navigate(self, selection):
        self.controller.show_frame(selection)

    def open_config(self, selection):
        # Placeholder for configuration logic
        print(f"Open configuration option: {selection}")

    def logout(self):
        # Placeholder for logout logic
        print("Logout")

    def exit_app(self):
        # Placeholder for exit logic
        print("Exit application")
        self.controller.root.quit()