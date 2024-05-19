import customtkinter
import os
from PIL import Image
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkintermapview import TkinterMapView
from tkinter import messagebox
from geopy.geocoders import Nominatim




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("eDNA Tracker")
        self.geometry("900x700+400+50")
        self.resizable(True, True)  # Disable resizing

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "main images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "success-colored-dna-images-4.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Picture1.png")), size=(500, 130))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Pondy_Univ_logo1.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image_1 = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark_1.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light_1.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  eDNA Tracker", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="eDNA DB",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="eDNA Search",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image_1, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="eDNA Upload",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame.rowconfigure(1, weight=1)  # configure row to expand vertically

        self.textbox = customtkinter.CTkTextbox(self.home_frame, width=400, height=200, font=("Roboto", 20))
        self.textbox.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Add some text to the textbox
        self.textbox.insert(customtkinter.END, "eDNA Tracker: Development of a Bioinformatic Tool for Creating an eDNA                                  Database and Monitoring Invasive Species\n\n")
        self.textbox.insert(customtkinter.END, "                                           A Dissertation Submitted to\n"
                                               "                              Pondicherry University, in partial fulfilment of\n"
                                               "                               Master of Science Degree in Bioinformatics\n\n")
        self.textbox.insert(customtkinter.END, "                                                                     By\n")
        self.textbox.insert(customtkinter.END, "                                                     Ashish Vachan Tiru\n")
        self.textbox.insert(customtkinter.END, "                                                     MSc. Bioinformatics\n\n")
        self.textbox.insert(customtkinter.END, "                                                  Under the Supervision of\n")
        self.textbox.insert(customtkinter.END, "                                                            Dr. A. Murali\n "
                                               "                                                     Assistant Professor\n\n")
        self.textbox.insert(customtkinter.END, "                                                      \n")
        self.textbox.insert(customtkinter.END, "DEPARTMENT OF ECOLOGY AND ENVIRONMENTAL SCIENCES, SCHOOL OF LIFE SCIENCES, PONDICHERRY UNIVERSITY, PUDUCHERRY - 605014."
                                               "                                                                    MAY- 2024\n")
        self.textbox.insert(customtkinter.END, "\n")
        self.textbox.configure(state="disabled")  # Disable editing


        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create third frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()

        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
            self.setup_search_tab()
        else:
            self.third_frame.grid_forget()

        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def fetch_data_from_db(self):
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Ashish01",
                database="eDNA_db_1"
            )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                cursor = connection.cursor()

                # Fetch table schema
                cursor.execute("DESCRIBE eDNA_Data")
                schema = cursor.fetchall()

                # Fetch table data
                cursor.execute("SELECT * FROM eDNA_Data")
                records = cursor.fetchall()

                # Create a new frame to display the data
                data_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
                data_frame.grid(row=0, column=1, sticky="nsew")

                # Clear previous data in the frame (if any)
                for widget in data_frame.winfo_children():
                    widget.destroy()

                # Create the Treeview widget
                tree = ttk.Treeview(data_frame)
                tree.pack(fill=tk.BOTH, expand=True)

                # Define the columns
                tree["columns"] = tuple(range(len(records[0])))

                # Configure the columns
                for col in tree["columns"]:
                    tree.column(col, anchor="w")

                # Insert headers into the Treeview
                headers = [column[0] for column in schema]
                tree.heading("#0", text="", anchor="w")
                for i, header in enumerate(headers):
                    tree.heading(i, text=header, anchor="w")

                # Insert data into the Treeview
                for record in records:
                    tree.insert("", tk.END, values=record)

                # Style the Treeview
                style = ttk.Style()
                style.theme_use("default")

                style.configure("Treeview",
                                background="#2a2d2e",
                                foreground="white",
                                rowheight=25,
                                fieldbackground="#343638",
                                bordercolor="#343638",
                                borderwidth=0)
                style.map('Treeview', background=[('selected', '#22559b')])

                style.configure("Treeview.Heading",
                                background="#565b5e",
                                foreground="white",
                                relief="flat")
                style.map("Treeview.Heading",
                          background=[('active', '#3484F0')])

        except mysql.connector.Error as e:
            print("Error connecting to MySQL: ", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")
        self.fetch_data_from_db()

    def select_frame_by_name(self, name):
        # Set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")

        # Show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            self.second_frame.grid_forget()
            self.third_frame.grid_forget()
            self.fourth_frame.grid_forget()
        elif name == "frame_2":
            self.home_frame.grid_forget()
            self.second_frame.grid(row=0, column=1, sticky="nsew")
            self.third_frame.grid_forget()
            self.fourth_frame.grid_forget()
        elif name == "frame_3":
            self.home_frame.grid_forget()
            self.second_frame.grid_forget()
            self.third_frame.grid(row=0, column=1, sticky="nsew")
            self.fourth_frame.grid_forget()
        elif name == "frame_4":
            self.home_frame.grid_forget()
            self.second_frame.grid_forget()
            self.third_frame.grid_forget()
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

        if not hasattr(self, 'search_frame'):
            self.search_frame = customtkinter.CTkFrame(self.third_frame, corner_radius=0, fg_color="transparent")
            self.search_frame.pack(fill=tk.BOTH, expand=True)

            # Add a label for the CO1 marker input
            co1_label = customtkinter.CTkLabel(self.search_frame, text="Enter CO1 marker:")
            co1_label.pack(pady=10)

            # Increase the size of the text box
            self.co1_textbox = customtkinter.CTkTextbox(self.search_frame, width=500,
                                                        height=400)  # Adjust width and height as needed
            self.co1_textbox.pack(pady=10)

            # Add a label for the location selection
            location_label = customtkinter.CTkLabel(self.search_frame, text="Select Location:")
            location_label.pack(pady=10)

            # Add the location combobox
            self.location_combobox = customtkinter.CTkComboBox(self.search_frame,
                                                               values=["Andhra Pradesh", "Arunachal Pradesh", "Assam",
                                                                       "Bihar", "Chhattisgarh", "Goa", "Gujarat",
                                                                       "Haryana", "Himachal Pradesh", "Jharkhand",
                                                                       "Karnataka", "Kerala", "Madhya Pradesh",
                                                                       "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
                                                                       "Nagaland", "Odisha", "Punjab",
                                                                       "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
                                                                       "Tripura", "Uttarakhand", "Uttar Pradesh",
                                                                       "West Bengal"])
            self.location_combobox.pack(pady=10)

            # Create a search button
            search_button = customtkinter.CTkButton(self.search_frame, text="Search", command=self.search_co1_marker)
            search_button.pack(pady=10)
        else:
            self.search_frame.pack(fill=tk.BOTH, expand=True)

    def search_co1_marker(self):
        # Get the CO1 marker from the text box and remove leading and trailing whitespace
        co1_marker = self.co1_textbox.get("1.0", tk.END).strip()

        # Get the selected location from the combobox
        location = self.location_combobox.get()

        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Ashish01",
                database="eDNA_db_1"
            )
            if connection.is_connected():
                cursor = connection.cursor()

                # Search for the CO1 marker and location in the database
                cursor.execute(
                    "SELECT scientific_name, common_name, Location FROM eDNA_Data WHERE CO1_marker = %s AND Location = %s",
                    (co1_marker, location))
                results = cursor.fetchall()

                if results:
                    # Create a new window to display the search results
                    self.result_window = customtkinter.CTkToplevel(self)
                    self.result_window.title("Native/ Local Species")

                    # Set the geometry of the result_window to match the main window
                    self.result_window.geometry("900x600+400+100")

                    # Create a frame to hold the results
                    result_frame = customtkinter.CTkFrame(self.result_window, corner_radius=0, fg_color="transparent")
                    result_frame.pack(fill=tk.BOTH, expand=True)

                    # Display the search results
                    for result in results:
                        scientific_name, common_name, location = result
                        result_label = customtkinter.CTkLabel(result_frame,
                                                              text=f"Scientific Name: {scientific_name}\nCommon Name: {common_name}\nLocation: {location}")
                        result_label.pack(pady=10)

                    # Create a frame for the map
                    self.map_frame = customtkinter.CTkFrame(self.result_window, corner_radius=0, fg_color="transparent")
                    self.map_frame.pack(fill=tk.BOTH, expand=True)

                    # Add a marker to the map
                    lat, lon = self.get_coordinates_from_location(location)
                    self.map_view = TkinterMapView(self.map_frame, width=600, height=400, corner_radius=0)
                    self.map_view.pack(fill=tk.BOTH, expand=True)
                    self.map_view.set_position(lat, lon)
                    self.map_view.set_marker(lat, lon, text=location)
                else:
                    # Check if CO1 marker matches but location doesn't
                    cursor.execute("SELECT scientific_name, common_name, Location FROM eDNA_Data WHERE CO1_marker = %s",
                                   (co1_marker,))
                    co1_results = cursor.fetchall()

                    if co1_results:
                        messagebox.showinfo("Species Type", "This species is an Invasive Species.")
                    else:
                        messagebox.showinfo("Species Type", "Species unspecified.")

        except mysql.connector.Error as e:
            print("Error connecting to MySQL: ", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

        if not hasattr(self, 'upload_frame'):
            self.upload_frame = customtkinter.CTkFrame(self.fourth_frame, corner_radius=0, fg_color="transparent")
            self.upload_frame.pack(fill=tk.BOTH, expand=True)

            # Create CTkTabview
            tabview = customtkinter.CTkTabview(self.upload_frame)
            tabview.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

            # Tab 1: Input data (common_name, scientific_name, CO1_marker)
            tab1 = tabview.add("Input Data")

            common_name_label = customtkinter.CTkLabel(tab1, text="Common Name:")
            common_name_label.pack(pady=10, anchor="w")
            self.common_name_textbox = customtkinter.CTkTextbox(tab1, width=300, height=1)
            self.common_name_textbox.pack(pady=5, anchor="w")

            scientific_name_label = customtkinter.CTkLabel(tab1, text="Scientific Name:")
            scientific_name_label.pack(pady=10, anchor="w")
            self.scientific_name_textbox = customtkinter.CTkTextbox(tab1, width=300, height=1)
            self.scientific_name_textbox.pack(pady=5, anchor="w")

            co1_marker_label = customtkinter.CTkLabel(tab1, text="CO1 Marker:")
            co1_marker_label.pack(pady=10, anchor="w")
            self.co1_marker_textbox = customtkinter.CTkTextbox(tab1, width=300, height=200)
            self.co1_marker_textbox.pack(pady=5, anchor="w")

            # Tab 2: Location input using Tkintermapview
            tab2 = tabview.add("Location")

            # Create a frame for the search input
            search_frame = customtkinter.CTkFrame(tab2, corner_radius=0, fg_color="transparent")
            search_frame.pack(fill=tk.X, padx=30, pady=10)

            # Text box for user input
            search_textbox = customtkinter.CTkTextbox(search_frame, width=300, height=1)
            search_textbox.pack(side=tk.LEFT)

            # Search button
            search_button = customtkinter.CTkButton(search_frame, text="Search",
                                                    command=lambda: self.search_place_on_map(
                                                        search_textbox.get("1.0", tk.END).strip()))
            search_button.pack(side=tk.LEFT, padx=10)

            map_frame = customtkinter.CTkFrame(tab2, corner_radius=0, fg_color="transparent")
            map_frame.pack(fill=tk.BOTH, expand=True)

            self.map_view = TkinterMapView(map_frame, width=600, height=400, corner_radius=0)
            self.map_view.pack(fill=tk.BOTH, expand=True)

            # Add marker functionality
            self.map_view.bind("<Button-1>", self.add_marker)

            # Add Location label and Indian states combo box
            location_frame = customtkinter.CTkFrame(tab2, corner_radius=0, fg_color="transparent")
            location_frame.pack(fill=tk.X, padx=30, pady=10)

            location_label = customtkinter.CTkLabel(location_frame, text="Location")
            location_label.pack(side=tk.LEFT)

            indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat",
                             "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
                             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
                             "Rajasthan",
                             "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttarakhand", "Uttar Pradesh",
                             "West Bengal"]

            self.location_combobox = customtkinter.CTkComboBox(location_frame, values=indian_states)
            self.location_combobox.pack(side=tk.LEFT)

            # Save button
            save_button = customtkinter.CTkButton(self.upload_frame, text="Save", command=self.save_data)
            save_button.pack(pady=10)
        else:
            self.upload_frame.pack(fill=tk.BOTH, expand=True)

    def get_coordinates_from_location(self, location):
        geocoder = Nominatim(user_agent="eDNA_Tracker")
        location = geocoder.geocode(location)
        return location.latitude, location.longitude

    def add_marker(self, event):
        # Get the coordinates of the left-click event
        x, y = event.x, event.y

        # Convert pixel coordinates to latitude and longitude
        lat, lon = self.map_view.convert_pixel_to_coords(x, y)

        # Add a marker at the clicked location
        marker = self.map_view.set_marker(lat, lon)

        # Update the state name in the combo box
        self.update_state_name(lat, lon)

    def update_state_name(self, lat, lon):
        # Use geocoding to get the state name from the coordinates
        geocoder = Nominatim(user_agent="eDNA_Tracker")
        location = geocoder.reverse(f"{lat}, {lon}")

        # Get the state name from the location
        state_name = location.raw['address']['state']

        # Update the combo box with the state name
        self.location_combobox.set(state_name)

    def delete_marker_on_map(self):
        # Get the list of markers on the map
        markers = self.map_view.get_markers()

        if markers:
            # Remove the last added marker
            self.map_view.delete_marker(markers[-1])

            # Update the coordinates and state text boxes
            self.coordinates_textbox.delete("1.0", tk.END)
            self.state_textbox.delete("1.0", tk.END)

            if markers:
                last_marker = markers[-1]
                self.coordinates_textbox.insert(tk.END, f"Coordinates: {last_marker.position}")
                self.state_textbox.insert(tk.END, f"State: {last_marker.state}")

    def search_place_on_map(self, search_query):
        # Implement the functionality to search for the place on the map
        if search_query:
            try:
                # Geocode the search query to get the coordinates
                geocoder = Nominatim(user_agent="eDNA_Tracker")
                location = geocoder.geocode(search_query)

                if location:
                    # Center the map on the searched location
                    self.map_view.set_position(location.latitude, location.longitude)

                    # Add a marker at the searched location
                    marker = self.map_view.set_marker(location.latitude, location.longitude, text=location.address)

                    # Update the coordinates and state text boxes
                    self.coordinates_textbox.delete("1.0", tk.END)
                    self.coordinates_textbox.insert(tk.END, f"Coordinates: {location.point}")

                    self.state_textbox.delete("1.0", tk.END)
                    self.state_textbox.insert(tk.END, f"State: {location.raw['address'].get('state', '')}")
                else:
                    messagebox.showerror("Error", "No results found for the search query.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while searching: {str(e)}")

    def save_data(self):
        common_name = self.common_name_textbox.get("1.0", customtkinter.END).strip()
        scientific_name = self.scientific_name_textbox.get("1.0", customtkinter.END).strip()
        co1_marker = self.co1_marker_textbox.get("1.0", customtkinter.END).strip()
        location = self.location_combobox.get()

        # Save data to the database
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Ashish01",
                database="eDNA_db_1"
            )
            if connection.is_connected():
                cursor = connection.cursor()

                # Insert data into the database
                sql_query = "INSERT INTO eDNA_Data (common_name, scientific_name, co1_marker, location) VALUES (%s, %s, %s, %s)"
                values = (common_name, scientific_name, co1_marker, location)
                cursor.execute(sql_query, values)
                connection.commit()

                # Show success message
                save_succeeded_window = customtkinter.CTkToplevel(self)
                save_succeeded_window.title("Save Successful")
                save_succeeded_label = customtkinter.CTkLabel(save_succeeded_window, text="Data saved to the database.")
                save_succeeded_label.pack(pady=20)

                print("Data saved to the database.")
        except mysql.connector.Error as e:
            print("Error connecting to MySQL: ", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")

if __name__ == "__main__":
    app = App()
    app.mainloop()

