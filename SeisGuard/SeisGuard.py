import sys, time, json, requests
from tkinter import *
from tkinter import ttk, messagebox

update = 60
progress = 0
url = 'https://ipinfo.io/json'

def usgs():
    current_time = time.localtime()
    past_time = time.localtime(time.time()-60)

    present = time.strftime("%Y-%m-%dT%H:%M:%S", current_time)
    past = time.strftime("%Y-%m-%dT%H:%M:%S", past_time)

    usgs = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&latitude='+f'{lat}'+'&longitude='+f'{lon}'+'&maxradiuskm=1750&minmagnitude=0&starttime='+f'{past}'+'&endtime='+f'{present}'+'&orderby=time'
    usgs_request = requests.get(usgs)
    usgs_request_json = usgs_request.json()
    if usgs_request.status_code == 200:
        with open('usgs.json', 'w') as f:
            json.dump(usgs_request_json, f, indent=4)
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

        update_loop()
        button0 = ttk.Button(frm, text="Quit", command=root.destroy).grid(row=4, column=0, pady=25)
        root.mainloop()
    else:
        print("Something went wrong with ipinfo.")
        exit(1)
else:
    exit(1)