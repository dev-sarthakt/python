import sys, time, json, requests, pygame, math
from tkinter import *
from tkinter import ttk, messagebox

update = 60
progress = 0
max_mag = 0
max_mag_loc = ''
eq_coo = []
url = 'https://ipinfo.io/json'

def eas():
    pygame.mixer.init()
    pygame.mixer.music.load('eas.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def usgs():
    current_time = time.localtime()
    past_time = time.localtime(time.time()-(60*5))

    present = time.strftime("%Y-%m-%dT%H:%M:%S", current_time)
    past = time.strftime("%Y-%m-%dT%H:%M:%S", past_time)

    usgs = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude='+f'{lat}'+'&longitude='+f'{lon}'+'&maxradiuskm=1750&minmagnitude=0&starttime='+f'{past}'+'&endtime='+f'{present}'+'&orderby=time'
    usgs_request = requests.get(usgs)
    usgs_request_json = usgs_request.json()
    if usgs_request.status_code == 200:
        with open('usgs.json', 'w') as f:
            json.dump(usgs_request_json, f, indent=4)
        with open('usgs.json', 'r') as f:
            data = json.load(f)
        if len(data['features']) != 0:
            with open('log.txt', 'a') as f:
                for eq_data in data['features']:
                    log_str = f'{time.strftime("Date : %Y-%m-%d | Time : %H:%M:%S", current_time)} | {eq_data['properties']['title']} | Coo : {eq_data['geometry']['coordinates']}\n'
                    f.write(log_str)
                    global max_mag, max_mag_loc, eq_coo
                    if eq_data['properties']['mag'] > max_mag:
                        max_mag = eq_data['properties']['mag']
                        max_mag_loc = eq_data['properties']['title']
                        eq_coo = eq_data['geometry']['coordinates']
            dist = math.sqrt(math.pow((eq_coo[0]-lon), 2)+math.pow((eq_coo[1]-lat), 2))
            if max_mag > 5.5:
                seis_label['text'] = f'!!! {max_mag_loc} !!!'
                seis_label['fg'] = 'red'
                mag_bar['style'] = "red.Horizontal.TProgressbar"
                mag_bar['value'] = max_mag*10
                dist_bar['value'] = 100-((dist/1750)*100)
                root.update_idletasks()
                eas()
            else:
                seis_label['text'] = f'!!! {max_mag_loc} !!!'
                mag_bar['style'] = "green.Horizontal.TProgressbar"
                mag_bar['value'] = max_mag*10
                dist_bar['value'] = 100-((dist/1750)*100)
    else:
        print("Something went wrong with usgs.")
        exit(1)

def update_loop():
            global update, progress
            if update < 0:
                usgs()
                update = 60
                progress = 0
            if update < 4:
                label0["fg"]="red"
                progress_bar["style"] = "red.Horizontal.TProgressbar"
            else:
                label0["fg"]="black"
                progress_bar["style"] = "green.Horizontal.TProgressbar"
            label0['text']=f"Nxt update in {update:02}s..."
            progress_bar['value']=progress
            root.update_idletasks()
            root.after(1000, update_loop)
            update -= 1
            progress += (1/60)*100

ip_permission = messagebox.askyesno("Permission Request", "Allow SeisGuard to access this device's IP?")

if ip_permission:
    request = requests.get(url)
    json_request = request.json()
    if request.status_code == 200:
        with open('ip.json', 'w') as f:
            json.dump(json_request, f, indent=4)
        root = Tk()
        root.title("SeisGuard")
        if sys.platform.startswith("win"):
            root.iconbitmap("icon.ico")
            icon = PhotoImage(file="icon.png").subsample(5, 5)
        else:
            icon = PhotoImage(file="icon.png").subsample(5, 5)
            root.iconphoto(True, icon) 

        style = ttk.Style(root)
        style.configure("green.Horizontal.TProgressbar", background="green")
        style.configure("red.Horizontal.TProgressbar", background="red")

        frm = Frame(root, padx=25, pady=25, bg="#00FFFF")
        frm.grid()

        icon_label = Label(frm, image=icon, bg="#00FFFF")
        icon_label.grid(row=0, column=0, padx=10, pady=10)

        main_label = Label(frm, text="SeisGuard", bg="#00FFFF", font=("Courier New", 25, "bold"))
        main_label.grid(row=1, column=0, padx=10, pady=10)

        with open('ip.json', 'r') as f:
            data = json.load(f)
        city, state, country, coo, post = data['city'], data['region'], data['country'], data['loc'], data['postal']
        lat, lon = map(float, coo.split(','))

        loc_label = Label(frm, text=f"Location : {city}, {state}, {country} - {post}", bg="#00FFFF", font=("Courier New", 15))
        loc_label.grid(row=2, column=0, padx=10, pady=10)

        progress_bar_frame = Frame(frm, padx=10, pady=10, bg="#00FFFF")
        progress_bar_frame.grid(row=3, column=0)

        label0 = Label(progress_bar_frame, bg="#00FFFF", font=("Courier New", 15))
        label0.grid(row=0, column=0, padx=10, pady=10)

        progress_bar = ttk.Progressbar(progress_bar_frame, style="green.Horizontal.TProgressbar", length=600, mode='determinate')
        progress_bar.grid(row=1, column=0, padx=10, pady=10)

        seis_label = Label(frm, anchor='center', text="No seismic activity detected.", bg="#00FFFF", font=("Courier New", 15, "bold"))
        seis_label.grid(row=4, column=0, padx=10, pady=10)

        mag_bar_frame = Frame(frm, bg="#00FFFF")
        mag_bar_frame.grid(row=5, column=0, padx=10, pady= 10)

        

        mag_label = Label(mag_bar_frame, text="Magnitude : ", bg="#00FFFF", font=("Courier New", 15, "bold"))
        mag_label.grid(row=0, column=0, padx=10, pady=10)

        mag_bar = ttk.Progressbar(mag_bar_frame, style="green.Horizontal.TProgressbar", length=400, mode='determinate')
        mag_bar.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        dist_label = Label(mag_bar_frame, text="Distance : ", bg="#00FFFF", font=("Courier New", 15, "bold"))
        dist_label.grid(row=1, column=0, padx=10, pady=10)

        dist_bar = ttk.Progressbar(mag_bar_frame, style="green.Horizontal.TProgressbar", length=400, mode='determinate')
        dist_bar.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        update_loop()
        button0 = ttk.Button(frm, text="Quit", command=root.destroy).grid(row=6, column=0, pady=25)
        root.mainloop()
    else:
        print("Something went wrong with ipinfo.")
        exit(1)
else:
    exit(1)
