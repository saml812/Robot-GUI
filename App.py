import customtkinter
from NavigationFrame import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Robot-GUI")
        self.geometry("1280x720")

        # Grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create navigation frame
        self.navigation_frame = NavigationFrame(self, self.change_appearance_mode_event)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        # Create frames
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # self.home_frame.grid_columnconfigure(0, weight=1)

        self.controller_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.led_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ml_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        self.navigation_frame.update_selected_button(name)

        # Show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "controller":
            self.controller_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.controller_frame.grid_forget()

        if name == "led":
            self.led_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.led_frame.grid_forget()

        if name == "ml":
            self.ml_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ml_frame.grid_forget()


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()