import tkinter as tk
import requests 
from PIL import Image, ImageTk
import io

API_KEY = "96c3b15c58e34abde94f9fdbe5de9960" # my key on TMDB 
BASE_URL = "https://api.themoviedb.org/3" #
IMG_BASE_URL = "https://image.tmdb.org/t/p/w500" #tmdb poster link

   # TKINTER WINDOW
root = tk.Tk()
root.title("K-DRAMAHUB")
root.geometry ("500x650")
root.configure(bg="dark blue")

bg_img = Image.open("8a378d2023a93bc0ded145445291e6db.jpg")
bg_img = bg_img.resize((500, 650)) #fix the window/geometry
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_photo) #labels the img
bg_label.place(x=0, y=0, relwidth=1, relheight=1) #puts everything behind


title_label = tk.Label(root, text="K-DRAMAHUB", font=("Arial", 20, "bold" ))
title_label.pack(pady=10)

# for the search frame 
frame = tk.Frame(root, bg="white") 
frame.pack(pady=5)

search_label = tk.Label(frame, text="search k-drama", bg="white")
search_label.pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(frame, width=30)
search_entry.pack(side=tk.LEFT, padx=5)

# Results Box
result_text = tk.Text(root, width=60, height=15, wrap=tk.WORD, bg="white", fg="blue")
result_text.pack(pady=10, padx=10)

poster_label = tk.Label(root, bg="white")
poster_label.pack(pady=10)

def search_kdrama():
    query = search_entry.get() #gets text from search bar
    if query =="": #so empty space does'nt break 
     result_text.insert(tk.END, "please type a drama name first")
     return
      
    url = f"{BASE_URL}/search/tv" #API door for code to questions about the drama typed in     
    params = { #params keeps info in a box so it can be reuse so i dont have to rewrite stuff
        "api_key": API_KEY,
        "query": query,
        "language": "en-US",
        "with_origin_country": "KR"        
    }

    response = requests.get(url, params=params)
    data = response.json() 

    result_text.delete(1.0, tk.END)  #clears old results
    poster_label.config(image="")  #clears old posters 

    if data["results"]:
       drama = data["results"][0]
       result_text.insert(tk.END, f"Title: {drama['name']}\n\n")
       result_text.insert(tk.END, f"Overview: {drama['overview']}\n\n")
       result_text.insert(tk.END, f"Rating: {drama['vote_average']}/10")

       if drama.get('poster_path'): #if poster exists
          img_url = IMG_BASE_URL + drama['poster_path'] 
          img_data = requests.get(img_url).content
          img = Image.open(io.BytesIO(img_data))
          img = img.resize((200, 300)) #rize to fit
          photo = ImageTk.PhotoImage(img)
          poster_label.config(image=photo)
          poster_label.image = photo #keeps it from disappearing
       else:
          result_text.insert(tk.END, "\n\nNo poster available")
    else:
      result_text.insert(tk.END, "No drama found❌")
    
search_button = tk.Button(frame, text="Search", command=search_kdrama, bg="#ff0b0b", fg="white")
search_button.pack(side=tk.LEFT, padx=5)

root.mainloop()