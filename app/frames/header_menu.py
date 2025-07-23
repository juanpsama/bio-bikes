from tkinter import Menu, Tk


class HeaderMenu(Menu):
    def __init__(self, parent: Tk, controller, menu_frames):
        super().__init__(parent)
        self.controller = controller
        # parent.config(menu=self)

        # Create the File menu
        file_menu = Menu(self, tearoff=0)
        self.add_cascade(label="App", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.exit_app)

        # Create the Navigation menu
        navigation_menu = Menu(self, tearoff=0)
        self.add_cascade(label="Menú", menu=navigation_menu)
        for key, value in menu_frames.items():
            navigation_menu.add_command(
                label=value.display_name or key,
                command=lambda opt=key: self.navigate(opt),
            )

        # # Create the Configuration menu
        # config_menu = Menu(self, tearoff=0)
        # self.add_cascade(label="Configuration", menu=config_menu)
        # config_options_list = [
        #     "Config Option 1",
        #     "Config Option 2",
        #     "Config Option 3"
        # ]
        # for option in config_options_list:
        #     config_menu.add_command(label=option, command=lambda opt=option: self.open_config(opt))

        # # Create the Logout menu
        # self.add_command(label="Logout", command=self.logout)

    def new_command(self):
        # Placeholder for new command logic
        print("New command executed")

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
