import customtkinter
from PIL import Image
import os

class NavigationFrame(customtkinter.CTkFrame):
    def __init__(self, parent, appearance_mode_callback):
        super().__init__(parent, corner_radius=0)
        self.parent = parent
        self.appearance_mode_callback = appearance_mode_callback

        self.grid_rowconfigure(6, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images/Navigation")
        logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(50, 50))
        home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        controller_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "controller_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "controller_light.png")), size=(20, 20))
        led_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "led_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "led_light.png")), size=(20, 20))
        cyborg_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "cyborg_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "cyborg_light.png")), size=(20, 20))

        # Add logo
        self.navigation_frame_label = customtkinter.CTkLabel(self, text="  Robot-GUI", image=logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Navigation buttons
        self.home_button = self.create_nav_button("Home", "home", 1, home_image)
        self.controller_button = self.create_nav_button("Controller", "controller", 2, controller_image)
        self.led_button = self.create_nav_button("LEDs", "led", 3, led_image)
        self.ml_button = self.create_nav_button("Machine Learning", "ml", 4, cyborg_image)

        # Appearance mode menu
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self, values=["Light", "Dark", "System"], 
                                                                font=customtkinter.CTkFont(family="Inter", size=12), 
                                                                command=self.appearance_mode_callback)
        self.appearance_mode_menu.set(customtkinter.get_appearance_mode())
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    def create_nav_button(self, text, frame_name, row, image):
        button = customtkinter.CTkButton(
            self, corner_radius=0, height=40, border_spacing=10, text=text, image=image, font=customtkinter.CTkFont(family="Inter", size=12),
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.parent.select_frame_by_name(frame_name)
        )
        button.grid(row=row, column=0, sticky="ew")
        return button

    def update_selected_button(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.controller_button.configure(fg_color=("gray75", "gray25") if name == "controller" else "transparent")
        self.led_button.configure(fg_color=("gray75", "gray25") if name == "led" else "transparent")
        self.ml_button.configure(fg_color=("gray75", "gray25") if name == "ml" else "transparent")

