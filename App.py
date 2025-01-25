import customtkinter
from NavigationFrame import *
from SettingsManager import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Settings Manager
        self.settings_manager = SettingsManager()
        self.settings = self.settings_manager.settings

        # Apply settings
        self.title("Robot-GUI")
        self.geometry(f'{self.settings["window"]["width"]}x{self.settings["window"]["height"]}')
        self.minsize(800, 600)
        self.current_scale = self.settings["scale"]
        self.set_theme(self.settings["theme"])
        self.set_scale(self.current_scale)

        # Grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Create navigation frame
        self.navigation_frame = NavigationFrame(self, self.change_appearance_mode)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        # Create content frames
        self.create_frames()

        # Hotkey bindings for scaling
        self.bind_hotkeys()

        # Save settings when closing
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_frames(self):
        """Create the frames."""
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.controller_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.led_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ml_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Select default frame
        self.select_frame_by_name("home")

    def bind_hotkeys(self):
        # Bind hotkeys for scaling the GUI.
        self.bind("<Control-equal>", lambda _: self.update_scaling(0.1))  # Ctrl+=
        self.bind("<Control-minus>", lambda _: self.update_scaling(-0.1))  # Ctrl+-
        self.bind("<Control-0>", lambda _: self.reset_scaling())  # Ctrl+0

    def set_theme(self, theme):
        # Apply the selected theme.
        customtkinter.set_appearance_mode(theme)

    def set_scale(self, scale):
        # Apply the scaling to the application.
        customtkinter.set_widget_scaling(scale)
        customtkinter.set_window_scaling(scale)

    def update_scaling(self, scale_delta):
        # Update scaling of all GUI elements.
        new_scale = self.current_scale + scale_delta
        new_scale = max(0.5, min(new_scale, 1.5))  # Range between 0.5 and 1.5
        self.current_scale = new_scale
        self.set_scale(new_scale)

    def reset_scaling(self):
        # Reset scaling to the default value (1.0).
        self.current_scale = 1.0
        self.set_scale(self.current_scale)

    def change_appearance_mode(self, new_appearance_mode):
        # Change the theme.
        self.set_theme(new_appearance_mode)
        self.settings["theme"] = new_appearance_mode

    def select_frame_by_name(self, name):
        # Show the selected frame and hide others.
        self.navigation_frame.update_selected_button(name)
        frame_map = {
            "home": self.home_frame,
            "controller": self.controller_frame,
            "led": self.led_frame,
            "ml": self.ml_frame
        }
        for frame_name, frame in frame_map.items():
            if name == frame_name:
                frame.grid(row=0, column=1, sticky="nsew")
            else:
                frame.grid_forget()

    def on_close(self):
        """Save settings and close the app."""
        self.settings["window"]["width"] = self.winfo_width()
        self.settings["window"]["height"] = self.winfo_height()
        self.settings["scale"] = self._get_window_scaling()
        self.settings["theme"] = self._get_appearance_mode()
        self.settings_manager.save_settings()
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
