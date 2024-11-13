import tkinter as tk
from tkinter import PhotoImage, ttk, IntVar
import time
import RPi.GPIO as GPIO  # GPIO-Bibliothek importieren


# GPIO initialisieren

GPIO.setmode(GPIO.BCM)  # Verwende die BCM-Nummerierung
GPIO.setwarnings(False)  # Warnungen deaktivieren
GPIO.setup(4, GPIO.OUT)  # Setze Pin 4 als Ausgang
GPIO.setup(27, GPIO.OUT)  # Setze Pin 27 als Ausgang

#GPIO-Eingänge
# GPIO-Einstellungen fuer die Eingaenge (Punkte)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # GPIO 23 als Eingang mit Pull-Down-Widerstand
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # GPIO 24 als 

# Globale Variable fuer den Zeit-Count
timer_running = False
time_seconds = 0

# Globale Variablen fuer die Punktestaende

game_duration = 0
score1, score2, score3, score4 = 0, 0, 0, 0
weiter_1, weiter_2, weiter_3, weiter_4 = 0, 0, 0, 0
gewinner_1, gewinner_2, gewinner_3, gewinner_4 = 0, 0, 0, 0
verlierer_1, verlierer_2, verlierer_3, verlierer_4 = 0, 0, 0, 0
gewinner_2_1, gewinner_2_2, verlierer_2_1, verlierer_2_2 = 0, 0, 0, 0
weiter_1, weiter_2, weiter_3, weiter_4 = 0, 0, 0, 0
weiter_2_1, weiter_2_2 = 0, 0
angabe = 0
current_game = 1
winners = []

final_game = False
current_round = 1

return_button_status = False

#Button
global participant_label, button_4, button_8


#Callback-Funktion, die aufgerufen wird, wenn der Return-Button gedrueckt wird
def on_return_button_clicked():
    print("Return Button wurde gedrueckt!")
    global return_button_status 
    return_button_status = True
    show_buttons()
    hide_labels()
    reset_center_timer()
    result_label.place_forget()
    punktemodus_button.place_forget()
    zeitmodus_button.place_forget()
    punkte_auswahl.place_forget()
    #weiter_button.place_forget()
    button_4.place_forget()
    button_8.place_forget()
    participant_label.place_forget()
    participant_label.place
    button_4.place_forget()  # Links platzieren
    button_8.place_forget() 
    label5.place_forget()
    label4.place_forget() # Rechts platzieren
    root.after(3000, return_button_status = False)
    
   
def punktemodus(spieler_x, spieler_y, score_a, score_b, label_a, label_b, zielpunktzahl):
    while score_a == 10 or score_b == 10 or return_button_status == True:
        label_a.place(x=200, y=300)
        label_b.place(x=1400, y=300)
        
        score_score_a.place(x=200, y=360)
        score_score_b.place(x=1400, y=360)


# Callback-Funktion, die aufgerufen wird, wenn die anderen Buttons gedrueckt werden
def on_single_player_mode_clicked():
    print("Einzelspielmodus Button wurde gedrueckt!")
    single_player_button.place_forget()  # Einzelspielmodus-Button ausblenden
    quick_game_button.place_forget()  # Schnelles Spiel-Button ausblenden
    tournament_mode_button.place_forget()  # Turniermodus-Button ausblenden
    
    # Zeige stattdessen die neuen Modus-Buttons an
    punktemodus_button.place(x=600, y=360)
    zeitmodus_button.place(x=900, y=360)
    
    

    


def on_quick_game_clicked():
    global score1, score3
    print("Schnelles Spiel Button wurde gedrueckt!")
    
     # Punktestand zuruecksetzen

    score_label1.config(text=str(score1))
    score_label3.config(text=str(score3))
    
    
    single_player_button.place_forget()  # Den Einzelspielmodus Button ausblenden
    quick_game_button.place_forget() #Schnelles Spiel Button ausblenden
    tournament_mode_button.place_forget() 
   
    GPIO.output(4, GPIO.HIGH)  # Setze Pin 4 auf HIGH
    root.after(10000, turn_off_gpio)  # Schalte GPIO nach 10 Sekunden wieder aus
    show_labels()
    start_center_timer()  # Starte den mittleren Timer
    
    

        
    



def update_timer():
    global timer_running, time_seconds
    if timer_running:
        time_seconds += 1  # Zeit erhuehen
        minutes = time_seconds // 60
        seconds = time_seconds % 60
        time_label.config(text=f"{minutes}:{seconds:02}")  # Label aktualisieren
        root.after(1000, update_timer)  # Alle 1000ms (1 Sekunde) erneut aufrufen    
    
    
    
    
    


def show_labels_Punkte():
    label1.place(x=200, y=300)
    score_label1.place(x=200, y=360)  # Punktestand anzeigen
    
    label3.place(x=1400, y=300)
    score_label3.place(x=1400, y=360)  # Punktestand anzeigen







def show_labels():
    # Spielerlabel und Punktestand anzeigen
    label1.place(x=200, y=300)
    score_label1.place(x=200, y=360)  # Punktestand anzeigen
    label2.place(x=800, y=300)
    center_timer_label.place(x=800, y=360)
    label3.place(x=1400, y=300)
    score_label3.place(x=1400, y=360)  # Punktestand anzeigen

def hide_labels():
    # Spielerlabel und Punktestand ausblenden
    label1.place_forget()
    score_label1.place_forget()  # Punktestand ausblenden
    label2.place_forget()
    center_timer_label.place_forget()
 
    score_label3.place_forget()
    label3.place_forget()

def show_buttons():
    # Buttons wieder einblenden
    single_player_button.place(x=150, y=150)  # Die vorherige Position wiederherstellen
    tournament_mode_button.place(x=840, y=150)
    quick_game_button.place(x=495, y=150)  # Die vorherige Position wiederherstellen

def on_tournament_mode_clicked():
    print("Turniermodus Button wurde gedrueckt!")
    single_player_button.place_forget()
    quick_game_button.place_forget()
    tournament_mode_button.place_forget()
    
    # Zeigt das Label zur Auswahl der Teilnehmerzahl und die Buttons an
    participant_label.place(x=800, y=200, anchor="center")  # Oben mittig platzieren
    button_4.place(x=500, y=360)  # Links platzieren
    button_8.place(x=1100, y=360)  # Rechts platzieren
    
def on_button_4_clicked():
    print("4 Teilnehmer gewaehlt!")
    button_4.place_forget()
    button_8.place_forget()
    participant_label.place_forget()
    show_labels_Punkte()  # Z
     # Zeige die Labels an, nachdem 4 Teilnehmer ausgewaehlt wurden
    angabe = 4 # Das erste Spiel mit Spieler 1 und 2 starten
    show_Label_1_2(angabe = 4)
    
def on_button_8_clicked():
    print("8 Teilnehmer gewaehlt!")
    button_4.place_forget()
    button_8.place_forget()
    participant_label.place_forget()
    show_labels()
    label2.place_forget()
    center_timer_label.place_forget()  # Zeige die Labels an, nachdem 8 Teilnehmer ausgewaehlt wurden
    start_game(1, 2)  # Das erste Spiel mit Spieler 1 und 2 starten

def show_Label_1_2(angabe):
    
    label1.place(x=200, y=300)
    score_label1.place(x=200, y=360)  # Punktestand anzeigen
    
    label3.place(x=1400, y=300)
    score_label3.place(x=1400, y=360)
    score1 = 10
    score_label1.config(text=str(score1))
    score_label3.config(text=str(score3))
    if score1 == 10:
        gewinner_1 = "Spieler_1"
        verlierer_1 = "Spieler_2"
        result_text = "Spieler 1 hat gewonnen!"
        result_label.config(text=result_text)
        result_label.place(x=600, y=360)
        if angabe == 4:
            root.after(15000, show_Label_3_4(angabe, gewinner_1 , verlierer_1))
            root.after(15000, result_label.place_forget)
            
    elif score2 == 10:
        gewinner_1 = "Spieler_2"
        verlierer_1 = "Spieler_1"
        result_text = "Spieler 2 hat gewonnen!"
        result_label.config(text=result_text)
        result_label.place(x=600, y=360)
        weiter_1 = 1
        if angabe == 4:
            root.after(15000, show_Label_3_4(angabe, gewinner_1 , verlierer_1))
            root.after(15000, result_label.place_forget)
       
        
def show_Label_3_4(angabe, gewinner_1, verlierer_1):
    score1 = 0
    score2 = 0
    
    label4.place(x=200, y=300)
    score_label1.place(x=200, y=360)  # Punktestand anzeigen
    
    label5.place(x=1400, y=300)
    score_label3.place(x=1400, y=360)
    score1 = 10
    score_label1.config(text=str(score1))
    score_label3.config(text=str(score3))
    if score1 == 10:
        spieler_3 = "winner_2"
        spieler_4 = "verlierer_2"
        result_text = "Spieler 3 hat gewonnen!"
        result_label.config(text=result_text)
        result_label.place(x=600, y=360)
        weiter2 = 1
        
    elif score2 == 10:
        spieler_3 = "verlierer_2"
        spieler_4 = "winner_2"
        result_text = "Spieler 4 hat gewonnen!"
        result_label.config(text=result_text)
        result_label.place(x=600, y=360)
        weiter_2 = 1
        
        
    
def Vierer_Modus_Turnier():
    
    if weiter_1 == 1:
        root.after(15000, show_Label_3_4)
        result_label.place_forget()
        
        if weiter_2 == 2:
            result_text = "Spieler 4 hat gewonnen!"
        result_label.config(text=result_text)
        result_label.place(x=600, y=360)
        
        
    
    


# Funktion, um GPIO nach 10 Sekunden wieder auszuschalten
def turn_off_gpio():
    GPIO.output(4, GPIO.LOW)  # Setze Pin 4 auf LOW
    print("GPIO Pin 4 wurde wieder auf LOW geschaltet.")
    
def start_game(player_a, player_b):
    global score1, score2, score3, score4
    
    # Labels fr die Spieler setzen
    if player_a == 1 and player_b == 2:
        label1.config(text="Spieler 1")
        label3.config(text="Spieler 2")
        score_label1.config(text=str(score1))
        score_label3.config(text=str(score2))
    elif player_a == 3 and player_b == 4:
        label1.config(text="Spieler 3")
        label3.config(text="Spieler 4")
        score_label1.config(text=str(score3))
        score_label3.config(text=str(score4))
    elif current_mode == "turniermodus" and final_game:
        label1.config(text="Gewinner Halbfinale 1")
        label3.config(text="Gewinner Halbfinale 2")
    
    # Jetzt die spezifische Sieges-erprfung basierend auf dem Spielmodus
    if current_mode == "turniermodus":
        check_winner_turniermodus(player_a, player_b)
    elif current_mode == "schnellmodus":
        check_quick_mode()
    elif current_mode == "einzelspielermodus":
        check_single_player()
    
    # Punktestand Labels und Labels anzeigen
       


    
#Timer
    
def start_center_timer():
    global timer_running, time_seconds
    timer_running = True
    time_seconds = 0
    update_center_timer()  # Beginne das Update sofort



def update_center_timer():
    global timer_running, time_seconds
    if timer_running:
        minutes = time_seconds // 60
        seconds = time_seconds % 60
        center_timer_label.config(text=f"{minutes}:{seconds:02}")
        if time_seconds >= 61:
            timer_running = False
            center_timer_label.place_forget()  # Timer-Label ausblenden
            check_winner()  # Gewinner pruefen und anzeigen
        else:
            time_seconds += 1
            root.after(1000, update_center_timer)

def reset_center_timer():
    global timer_running, time_seconds
    timer_running = False
    time_seconds = 0
    center_timer_label.config(text="0:00")

# Gewinner pruefen und Ergebnis anzeigen
def check_winner():
    global score1, score2, score3, score4, winners, current_round, final_game
    
    if current_round == 1:  # Spiel 1: Spieler 1 vs Spieler 2
        if score1 > 10:
            winners.append(1)
            result_text = "Spieler 1 hat gewonnen!"
        elif score2 > 10:
            winners.append(2)
            result_text = "Spieler 2 hat gewonnen!"
        current_round += 1
        root.after(15000, lambda: start_game(3, 4))
        
    elif current_round == 2:  # Spiel 2: Spieler 3 vs Spieler 4
        if score3 > 10:
            winners.append(3)
            result_text = "Spieler 3 hat gewonnen!"
        elif score4 > 10:
            winners.append(4)
            result_text = "Spieler 4 hat gewonnen!"
        current_round += 1
        root.after(15000, start_final_game)
    
    else:  # Finale
        if score1 > 10:
            result_text = "Final: Spieler 1 hat das Turnier gewonnen!"
        elif score3 > 10:
            result_text = "Final: Spieler 3 hat das Turnier gewonnen!"
        final_game = True
        # Return-Button einblenden, um zurueckzukehren
        return_button.place(x=800, y=500)
    
    # Gewinner-Label anzeigen und 15 Sekunden warten
    result_label.config(text=result_text)
    result_label.place(x=800, y=360)
    root.after(15000, reset_for_next_round)

# Funktion zum Aktualisieren von Datum und Uhrzeit
def update_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)
    
    
    
    
    
    
    
    
# Funktion zum Aktualisieren der Button-Position bei Groessenanderung
def update_button_position(event):
    return_button.place(y=root.winfo_height() - 100)  # Button 100 Pixel vom unteren Rand entfernt platzieren
     #Auch die anderen Buttons anpassen
    single_player_button.place(y=root.winfo_height() - 150)  # Fuer den Einzelspielmodus
    quick_game_button.place(y=root.winfo_height() - 150)  # Fuer das schnelle Spiel
    tournament_mode_button.place(y=root.winfo_height() - 150)  # Fuer den Turniermodus   
    
# Callback-Funktionen fuw "Punktemodus" und "Zeitmodus"
def on_punktemodus_clicked():
    print("Punktemodus wurde gewuwhlt!")
    # Hier kann die Logik fgt werden
    punktemodus_button.place_forget()
    zeitmodus_button.place_forget()
    
   
   
    punkte_auswahl.place(x=600, y=360)
    

    # Weiter-Button erstellen
    
    weiter_button.place(x=900, y=360)


def on_zeitmodus_clicked():
    print("Zeitmodus wurde gewaehlt!")
    # Die "Punktemodus" und "Zeitmodus"-Buttons ausblenden
    punktemodus_button.place_forget()
    zeitmodus_button.place_forget()
    
    # Erstellen der vier Buttons fuer 5, 10, 15 und 20 Punkte und vertikale Platzierung
    button_5.place(x=300, y=360)
    button_10.place(x=700, y=360)
    button_15.place(x=1100, y=360)
    button_20.place(x=1500, y=360)
    
def on_point_button_clicked(points):
    print(f"Punkte fuer Zeitmodus ausgewaehlt: {points}")
    # Hier kann weitere Logik fuer den Zeitmodus hinzugefuegt werden
    game_duration = points * 60  # Minuten in Sekunden umwandeln
    # Alle Punkt-Buttons ausblenden, nachdem eine Auswahl getroffen wurde
    button_5.place_forget()
    button_10.place_forget()
    button_15.place_forget()
    button_20.place_forget()
    
    start_game_timer(game_duration)  # Timer mit der ausgewlten Dauer starten

    # Labels anzeigen (wie im schnellen Spiel)
    show_labels()

def start_game_timer(duration):
    global timer_running, time_seconds
    timer_running = True
    time_seconds = 0
    update_game_timer(duration)  # Beginne das Update sofort

def update_game_timer(duration):
    global timer_running, time_seconds
    if timer_running:
        if time_seconds < duration:
            minutes = time_seconds // 60
            seconds = time_seconds % 60
            center_timer_label.config(text=f"{minutes}:{seconds:02}")
            time_seconds += 1
            root.after(1000, update_game_timer, duration)  # Alle 1000ms (1 Sekunde) erneut aufrufen
        else:
            # Wenn der Timer abgelaufen ist, das Spiel beenden und Ergebnis prfen
            timer_running = False
            check_winner()  # Gewinner pren und anzeigen

def check_winner():
    # Sicherstellen, dass score1 und score3 korrekt definiert sind
    if score1 > score3:
        result_text = "Spieler 1 hat gewonnen!"
    elif score3 > score1:
        result_text = "Spieler 2 hat gewonnen!"
    else:
        result_text = "Unentschieden!"
    
    # Ergebnis-Label anzeigen
    result_label.config(text=result_text)
    result_label.place(x=600, y=360)
    zeitmodus_button.place_forget()
    center_timer_label.place_forget()





# Funktion, die aufgerufen wird, wenn einer der Punkte-Buttons gedrueckt wird
def on_points_button_clicked(point):
    print(f"Punkte {point} gewaehlt!")
    # Hier kannst du die Logik fgen, z.B. die Variable `punkte_var` setzen.
    punkte_var.set(point)
    
    
    
def on_weiter_punktemodus_clicked(punkte_auswahl):
    selected_points = int(punkte_var.get())
    print(f"Punkte fuer Punktemodus ausgewuehlt: {selected_points}")
    # Weitere Logik fuer den Punktemodus hinzufuegen
    
    
    #punkte_auswahl.place_forget()
    weiter_button.place_forget()
    punkte_auswahl.place_forget()
    # Labels und Punktestuende fuer Spieler anzeigen (wie im "Schnellen Spiel")
    show_labels()  # Funktion zum Anzeigen der Labels aufrufen
    
  
    
    

# Hauptfenster erstellen
root = tk.Tk()
root.title("Bild und Button")
root.configure(bg='black')  # Hintergrundfarbe auf schwarz aendern

# Bild laden
imageLabel_1 = PhotoImage(file='/home/dasgelbevomei88/Bilder/FlashDuell_voll.png')  # Bildpfad anpassen

# Label mit dem Bild erstellen
image_label = tk.Label(root, image=imageLabel_1, bg='black')
image_label.pack(pady=10)  # Padding hinzufuegen, um Platz um das Bild zu schaffen















# Button fuer "Return"
return_button = tk.Button(root, text="Return", command=on_return_button_clicked, width=12, height=1, font=("Comic Sans MS", 36), bg="black", fg="white")
return_button.place(x=1500, y=250)  # Button an der gewuenschten Position platzieren

# Button fuer "Einzelspielmodus"
single_player_button = tk.Button(root, text="Einzelspielmodus", command=on_single_player_mode_clicked, width=12, height=2, font=("Comic Sans MS", 36), bg="black", fg="white")
single_player_button.place(x=150, y=150)  # Position anpassen

# Button fuer "Schnelles Spiel"
quick_game_button = tk.Button(root, text="Schnelles Spiel", command=on_quick_game_clicked, width=12, height=2, font=("Comic Sans MS", 36), bg="black", fg="white")
quick_game_button.place(x=495, y=100)  # Position anpassen

# Button fuer "Turniermodus"
tournament_mode_button = tk.Button(root, text="Turniermodus", command=on_tournament_mode_clicked, width=12, height=2, font=("Comic Sans MS", 36), bg="black", fg="white")
tournament_mode_button.place(x=840, y=50)  # Position anpassen




# Erstelle die drei Labels fuer "Schnelles Spiel"
#Spieler 1
# Spieler 1 Label
label1 = tk.Label(root, text="Spieler 1", font=("Comic Sans MS", 24), bg="black", fg="white")




# Punktestand Label (dreifach groesser)
score_label1 = tk.Label(root, text="0", font=("Comic Sans MS", 144), bg="black", fg="white")

#score_label1.config(text="10")  # Setzt den Punktestand auf 10






#Zeit
label2 = tk.Label(root, text="Spielstand", font=("Comic Sans MS", 24), bg="black", fg="white")

#Spieler 2
label3 = tk.Label(root, text="Spieler 2", font=("Comic Sans MS", 24), bg="black", fg="white")

label4 = tk.Label(root, text="Spieler 3", font=("Comic Sans MS", 24), bg="black", fg="white")

#Spieler 2
label5 = tk.Label(root, text="Spieler 4", font=("Comic Sans MS", 24), bg="black", fg="white")

# Punktestand Label (dreifach groesser)
score_label3 = tk.Label(root, text="0", font=("Comic Sans MS", 144), bg="black", fg="white")

#score_label3.config(text="10")  # Setzt den Punktestand auf 10

# Label fuer den Timer (als globales Label erstellt)
time_label = tk.Label(root, text="0:00", font=("Comic Sans MS", 144), bg="black", fg="white")



# Ereignis binden, um die Position des Buttons bei Groessenanderung zu aktualisieren
root.bind("<Configure>", update_button_position)








# Label fuer Datum und Uhrzeit oben rechts
time_label = tk.Label(root, font=('Comic Sans MS', 36), fg='white', bg='black')  # Textfarbe weiss, Hintergrund schwarz
time_label.place(relx=0.925, y=30, anchor='ne')  # Label oben rechts platzieren

# Zentrales Timer-Label fuer das Hochzaehlen
center_timer_label = tk.Label(root, text="0:00", font=("Comic Sans MS", 144), bg="black", fg="white")
#center_timer_label.place(x=800, y=360)

# Ergebnis-Label (anfangs versteckt)
result_label = tk.Label(root, text="", font=("Comic Sans MS", 72), bg="black", fg="white")

# Neue Buttons fr "Punktemodus" und "Zeitmodus" (anfangs unsichtbar)
punktemodus_button = tk.Button(root, text="Punktemodus", command=on_punktemodus_clicked, width=12, height=2, font=("Comic Sans MS", 36), bg="black", fg="white")
zeitmodus_button = tk.Button(root, text="Zeitmodus", command=on_zeitmodus_clicked, width=12, height=2, font=("Comic Sans MS", 36), bg="black", fg="white")
punkte_var = IntVar(root)
punkte_var.set(5)# Ve

punkteoptionen =  [5, 10, 15, 20]
punkte_auswahl = tk.OptionMenu(root, punkte_var, *punkteoptionen)
punkte_auswahl.config(font=("Comic Sans MS", 30), bg="black", fg="white", width=15)
  



button_5 = tk.Button(root, text="5", command=lambda: on_point_button_clicked(5), 
                     width=5, height=2, font=("Comic Sans MS", 60), bg="black", fg="white")
button_10 = tk.Button(root, text="10", command=lambda: on_point_button_clicked(10), 
                      width=5, height=2, font=("Comic Sans MS", 60), bg="black", fg="white")
button_15 = tk.Button(root, text="15", command=lambda: on_point_button_clicked(15), 
                      width=5, height=2, font=("Comic Sans MS", 60), bg="black", fg="white")
button_20 = tk.Button(root, text="20", command=lambda: on_point_button_clicked(20), 
                      width=5, height=2, font=("Comic Sans MS", 60), bg="black", fg="white")
                      
participant_label = tk.Label(root, text="Bitte waehlen Sie die Anzahl der Teilnehmer aus!", font=("Comic Sans MS", 60), bg="black", fg="white")



button_4 = tk.Button(root, text="4", command=on_button_4_clicked, 
                      width=5, height=2, font=("Comic Sans MS", 60), bg="black", fg="white")
button_8 = tk.Button(root, text="8", command=on_button_8_clicked, 
                      width=5, height=2, font=("Comic Sans MS", 60), bg="black", fg="white")

# Zeit und Datum aktualisieren
update_time()

# Hauptschleife starten
root.mainloop()

# GPIO aufraeumen, wenn das Programm beendet wird
GPIO.cleanup()

