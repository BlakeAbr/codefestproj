
import tkinter as tk
from tkinter import ttk
import webbrowser
from cProfile import label
from tkinter import *


class ClassroomFinderApp:
    def __init__(self, master):
        self.master = master
        master.title("Classroom Finder")

        bg_image = PhotoImage(file='C:/Users/blake/Downloads/hannieimage.png')
        
        # Create a Label with the image
        background_label = Label(master, image=bg_image)
        background_label.image = bg_image  # Keep a reference
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        master.geometry("1920x1080")


        my_img = PhotoImage(file='C:/Users/blake/Downloads/logo.png')
        img_label = Label(root, image=my_img)
        img_label.image = my_img  # Keep a reference
        img_label.place(relx=0.5, rely=0.5, anchor=CENTER)



        #Science 1 - 5
        #Anderson Center
        #Fine Arrts
        #Lecture Hall
        #Classroom Wing
        # Academic A
        # Academic B
        # Library North
        #Engineering Building
        #Union
        #Whitney Hall
        # "": {"description": "", "coordinates": ""},

        self.buildings = {

            "Library North": {"description": "Main campus library", "coordinates": "42.087833, -75.969333"},
            "Science 1": {"description": "Department of Geological Sciences and Environmental Studies and Department of Anthropology and the Public Archaeology Facility", "coordinates": "42.089118733324845, -75.97068760320238"},
            "Science 2": {"description": "Houses general purpose classrooms and instructional lab for the departments of Biological Sciences, Chemistry and Physics, Applied Physics and Astronomy", "coordinates": "42.09009419803853, -75.9711625608733"},
            "Science 3": {"description": "Department of Biological Sciences and is attached to the Research Greenhouse", "coordinates": "42.090566252815954, -75.97036448786035"},
            "Science 4": {"description": "Department of Psychology", "coordinates": "42.091212527542815, -75.97038443203778"},
            "Science 5": {"description": "Department of Psychology's behavioral neuroscience research laboratories, as well as labs for the departments of Biological Sciences and Biomedical Engineering", "coordinates": "42.09080680523944, -75.97102046087325"},
            "Anderson Center": {"description": "Designed to meet the needs of every performing group from soloists to chamber ensembles, symphonies to dance or large theatrical productions complemented by a full-scale orchestra.", "coordinates": "42.089638498022396, -75.96833601484744"},
            "Fine Arts": {"description": "Houses the University Art Museum and its permanent collection, the Don A. Watters Theater which seats 574, including 122 in its balcony, the John Arthur Cafe and classrooms.", "coordinates": "42.08940762589575, -75.96844330087274"},
            "Lecture Hall": {"description": "Includes 14 lecture halls of varying sizes, all with multimedia capabilities", "coordinates": "42.087839264362955, -75.97116834553144"},
            "Classroom Wing": {"description": "Wing that connects the Lecture Hall with Academic A", "coordinates": "42.08843399489332, -75.97212438411991"},
            "Academic A": {"description": "One of newest academic buildings on campus. Academic A houses the School of Management, the Kaschak Institute for Social Justice for Women and Girls general purpose lecture halls and PODS computing classrooms.", "coordinates": "42.089046468068005, -75.97198765743454"},
            "Academic B": {"description": "One of newest academic buildings on campus. Academic B houses CCPA's departments of Student Affairs Administration and Teachling, Learning and Educational Leadership; the Environmental Studies Program; Health Promotion and Prevention Services; the Harriet Tubman Center for Freedom and Equity; and the Physica Therapy deaprtment's Anatomy and Physiology Lab.", "coordinates": "42.08966356996432, -75.97184210320243"},
            "Engineering Building": {"description": "Home to the departments of computer science, and systems science and industrial engineering in the Thomas J. Watson College of Engineering and Applied Science.", "coordinates": "42.087557275516275, -75.96809397436695"},
            "University Union": {"description": "There are student and administrative offices in the building, as well as large rooms, the Nelson A. Mandela Room, Old Union Hall and Tillman Lobb", "coordinates": "42.088014660502424, -75.96702349155736"},
            "Whitney Hall": {"description": "Consits of mostly offices and small classrooms", "coordinates": "42.08850325122465, -75.9638228915573"},
            "East Gym": {"description": "The first building constructed on campus, opened in 1958 and homes the Campus Recreational Services Office, which coordinates Intramurals, Club Sports, Outdoor Pursuits and Wellness activities, is based here", "coordinates": "42.09177071805388, -75.96440606087323"},
            "West Gym": {"description": "Located adjacent to the Events Center, opened in 1969 and includes the Patricia A. Saunders Aquatics Center, racquetball courts and, of course, the gymnasium. In addition to the University's Division I swimming and diving teams, the DI wrestling and volleyball teams call the West Gym home, and you'll often find various Club Sports and intramural activities going on here as well.", "coordinates": "42.092627968616135, -75.97092369155715"},
            "Events Center": {"description": "This three-level facility opened in 2004, includes a six-lane, 200-meter track and multipurpose area that can be used for a number of activities including pole vault, long jump, tennis, basketball and practice for many sports. It has a bowstring steel-truss roof to provide an unobstructed view of events.", "coordinates": "42.09317138439334, -75.97191428786026"},
            "Science Library": {"description": "Houses science books in the fields of astronomy, biology, chemistry, engineering/technology, environmental sciences, geology, nursing, psychology and physics. There are also classrooms in the building,", "coordinates": "42.089936245605, -75.97019223203785"},
            "Admissions Center": {"description": "boasts a presentation room, a large lobby, formal and informal meeting spaces and offices for undergraduate admissions, student accounts, and financial aid and student records.", "coordinates": "42.08765761314504, -75.96596094922833"},
            "Old Johnson": {"description": "Newly renovated Old Johnson Hall reopened in fall 2015 and houses the Department of Geography, Educational Communications Center, Office of Course Building and Academic Space Management, Office of Emergency Management, the University Testing Center and the VARCC.", "coordinates": "42.08828434873638, -75.96426801854437"},
            "C4": {"description": "Chenango Champlain Collegiate Center serves the Newing and Dickinson residential communities. The building includes shared dining facilities and an academic center that can be accessed from each community, as well as separate programming spaces and multipurpose rooms", "coordinates": "42.08804824658952, -75.96294063018945"},
            "CIW Dining Hall": {"description": "Located in the the Iroquois Commons ", "coordinates": "42.086253401684104, -75.96679218567868"},
            "Hinman Dining Hall": {"description": "Has two levels and serves residents of Hinman College as their dining hall and a place to hold meetings and other activities.", "coordinates": "42.08661966470452, -75.972703774367"},
            "Appalachian Collegiate Center": {"description": "Serves the Mountainview College residential community and includes the dining hall, Mountainview Night Owl and programming spaces. Located on the hills overlooking the center of campus, the dining hall boasts one of the most spectacular views of campus.", "coordinates": "42.08564188056483, -75.96950241669607"},
            "Technology Hub": {"description": "home to Binghamton University's Information Technology Services staff and resources. You'll find the Help Desk located in the first floor lobby", "coordinates": "42.0881969840403, -75.96859480320246"},


# "": "",
        }

        self.shortcuts = {
            "LN": "Library North",
            "S1": "Science 1",
            "S2": "Science 2",
            "S3": "Science 3",
            "S4": "Science 4",
            "S5": "Science 5",
            "SL": "Science Library",
            "AC": "Anderson Center",
            "UU": "University Union",
            "FA": "Fine Arts",
            "LH": "Lecture Hall",
            "CW": "Classroom Wing",
            "AA": "Academic A",
            "AB": "Academic B",
            "EB": "Engineering Building",
            "WH": "Whitney Hall",
            "GE": "East Gym",
            "GW": "West Gym",
            "EC": "Events Center",
            "OJ": "Old Johnson",
            "": "",


        }
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#1a3a1a', foreground='#ffffff')
        style.configure('TButton', background='#2e5a2e', foreground='#ffffff')
        style.configure('TEntry', fieldbackground='#2e5a2e', foreground='#ffffff')

        self.label = ttk.Label(master, text="Enter building name or abbreviation to quickly get directions:", style='TLabel', font=('Helvetica', 20))

        self.label.pack(pady=10)
        
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(master, textvariable=self.search_var, style='TEntry', width=40, font=('Helvetica', 16))
        self.search_entry.pack(pady=10)
        
        self.search_button = ttk.Button(master, text="Search", command=self.search_building, style='TButton', width=20)
        self.search_button.pack(pady=10)
        
        self.result_label = ttk.Label(master, text="", style='TLabel')
        self.result_label.pack(pady=10)
        
        self.map_button = ttk.Button(master, text="Open in Google Maps", command=self.open_map, style='TButton')
        self.map_button.pack(pady=5)
        self.map_button.pack_forget()  # Hide initially
        
    def search_building(self):
        query = self.search_var.get().strip().upper()
        if query in self.shortcuts:
            query = self.shortcuts[query]
        
        if query in self.buildings:
            building = self.buildings[query]
            self.result_label.config(text=f"{query}: {building['description']}")
            self.map_button.pack()
            self.current_coordinates = building['coordinates']
        else:
            self.result_label.config(text="Building not found.")
            self.map_button.pack_forget()
    
    def open_map(self):
        url = f"https://www.google.com/maps/search/?api=1&query={self.current_coordinates}"
        webbrowser.open_new(url)

root = tk.Tk()
app = ClassroomFinderApp(root)
root.mainloop()





