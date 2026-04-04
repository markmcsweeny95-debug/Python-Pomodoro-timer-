
# Modules used go here 
import time 
import turtle 
from turtle import*
from datetime import datetime 
from zoneinfo import ZoneInfo


# List of variables
x = 1 
p = 1 
y = 1
z = 1 
a = 5 
b = 5
d = 1
f = 0
e = 0
m = 0 
g = 1 
elapsed = 0 
cycles = 0 
total_study_secs_clone = 0 
total_study_secs = 0
total_break_secs = 0
total_secs = 0 
paused = False
cyclessecond = 0 


def toggle_pause():
  global paused 
  paused = not paused 
def update ():
  while paused:
    screen.update()
    time.sleep(0.1)
  



# Subroutine responsible for converting Decimal time into Hours, Mins and Secs
def decimal_to_hours(study_length):
          result = ("")
          first_digit = study_length[0]
          if first_digit in ("1","2","3","4","5","6","7","8","9"):
            second_digit = study_length[1]
            third_digit = study_length[2]
            if second_digit == ".":
             hours = int(study_length[0])
             tens_mins = int(study_length[2])
             tens_mins_final = (tens_mins * 6)
             result = f" {hours} hours and {tens_mins_final}mins"
             hours_final2 = (hours * 60) + tens_mins_final
            if third_digit == ".":
             tens_hours = int(study_length[0])
             seconds_hours = int(study_length[1])
             tens_mins = int(study_length[3])
             tens_mins_final = (tens_mins * 6)
             tens_hours_final = (tens_hours * 10)
             hours_final = (tens_hours_final + seconds_hours)
             result = f"{hours_final} hours and {tens_mins_final} mins"
             hours_final2 = (tens_hours_final * 60) + tens_mins_final

          else:
             hours_final2 = ("ERROR!")
          return hours_final2


_original_print = print

def print(*args, **kwargs):
  time.sleep(0.1)
  _original_print(*args, **kwargs)



print("MAKE SURE YOU HAVE READ THE README BEFORE USING THIS CODE, IF YOU HAVE NOT YET READ IT ENTER H NOW! IF  YOU HAVE PRESS ENTER TO CONTINUE")
h_present = input ("")
if h_present == "h" or h_present == "H":
  print("\n" * 4)
  print("Pomodoro Timer")
  print("\n" * 1)
  print("Features")
  print("- Study timer and break timer")
  print("- Custom time setting as well as classic 25,5 min setting")
  print("- Real time clock display so you can keep track of time")
  print("- Pausing and resuming function using spacebar")
  print("- Visual progress indicator for time left as well as text")
  print("\n" * 1)
  print("HOW TO RUN!")
  print("Controls")
  print("- (spacebar) to pause or resume timer. ")
  print("\n" * 1)
  print("How it works")
  print("- The timer is based on the pomodoro study technique (25min study, 5 min break)")
  print("- You can also make your own study cycles and break duration lengths to your liking")
  print ("- The program tracks real session progress and displays the remaining cycles as well as live time")
  print("\n" * 1)
  print("CONTACT INFO")
  print("- For more information view my public github repo at https://github.com/markmcsweeny95-debug/Python-Pomodoro-timer- ")
  print("- Or contact me on slack @markmcsweeny95 ")
  print("\n" * 3)
print("FOR FULL INSTURCTIONS ON USE ENTER F OTHERWISE ENTER TO CONTINUE")
instructions = input ("")
if instructions == "f" or instructions == "F":
  print("- Enter your city and the continent the city is in to allow the code to sync to your time zone")
  print("- Once this is done you will be welcomed and it will ask whether you would like to use a classic pomodoro timer (25 mins study and 5 mins break), or you can choose custom and set any minutes study and break")
  print("- You must ONLY enter the letter O or the letter C and nothing else or code will not work")
  print("- If you have selected custom it will ask you to input the time you would like to study for at each time, ie the time you study between breaks")
  print("- The code will then ask you to enter the break length in minutes WITH NO DECIMAL PLACES")
  print("- You will then be asked to enter the total study length this is how long you will repeat the pomodoro cyles for (MUST BE MORE THAN 1 HOUR AND MUST CONTAIN A DECIMAL PLACE)")
  print("- Once you enter the info a few outputs will show up with all the details of your timer, check these before commiting to starting properly")
  print("- Your timer will open in a new window usually along the task bar and select it, it should auto size automatically but if not you can full screen it.")
  print("- Enjoy it!!!")
  print("\n" * 3 )

print("Begin by entering the continent you are in to sync timezones")
timezonecont = input("")
print("Now, enter the capital city of the country you are in or a large city in the same country")
timezonecity = input("")
finaltimezone = f"{timezonecont}/{timezonecity}"

print("Welcome to my pomodoro timer!") # Welcome message


while x == 1: # Loops whole code (Only used when user enters incorrect value and has to restart)
    
    while paused:
     screen.update()
     time.sleep(0.1)
    
    
    print("Would you like to use the original pomodoro timer (25min study, 5 min break) or customise your own?")
    print("(Enter 'O' for original or enter 'C' for a custom timer)")
    print("\n" * 1 )
    classic = input ("") # User inputs "o" or "c" to select a custom timer or the original pomodoro one

    #ENTERING ORIGINAL POMDODORO TIMER SETTINGS
    #>>>

    if classic == "O" or classic == "o": # Introduction
     print("Ok, we will use the classic pomodoro timer!")
     print("Enter how long your entire study period will last... (Answer in a decimal of an hour) for example (1.2)")
     print("\n" * 1)

     study_length = str(input("")) # User inputs hours of total study period to 1 dp
     if (decimal_to_hours(study_length)) == "ERROR!": #If user enters a value which is not an hour to 1 dp
       print("You entered an incorrect value, please try again!")
       print("Code will restart in")
       while a > 0: #Prints a countdown from 5 to 0 
        while paused:
         screen.update()
         time.sleep(0.1)
        print(a)
        time.sleep(1)
        a = a - 1
       print("CODE RESTARTING...") 
       print("")
       while y <5:
        while paused:
         screen.update()
         time.sleep(0.1)
        print(">>>")
        y = y + 1 # code restarts
     else: 
       study_time = int(25)# Defines how long the study period is in each cycle
       break_time = int(5)# Defines how long the break period is in each cycle
       study_length2 = int(decimal_to_hours(study_length)) # Number of mins in the hours user input earlier #Defines it as an integer

       print ((decimal_to_hours(study_length)),"mins") # Displays to user how many minutes are in the hours they inputted
       cycles = ((decimal_to_hours(study_length))/30) # Calculates the number of cycles of the pomdoro timer that is needed 
       if total_secs > 0:
        cycles_fraction = cycles - (((elapsed / total_session_secs)))
       else:
        cycles_fraction = cycles
       cyclesmain = int(cycles_fraction)
      
       print(cycles,"cycles")
     

       if cycles_fraction < 0:
        cyclesmain = 0
        cyclessecond = 0

       
       cyclesmod = (study_length2 % 30) # Calculates the amount of minutes in the last decimal of a cycle
       print(cyclesmod,"Mins remainder")
       cyclesdiv = (study_length2// 30 )# Calculates the number of cycles of the pomodor timer can be completed in the time the user input
       print(cyclesdiv,"total cycles")
       print(cyclesdiv,"cycles and a",cyclesmod,"min remainder") # Tells user how many complete cycles of the pomodor timer are completed  
       total_secs = (study_time*60) + (break_time*60) #Calculates how many seconds total in the pomdodoro cycle 
       total_session_secs = study_length2 * 60
       total_study_secs = study_time*60
       total_break_secs = break_time * 60
       print("Enter yes to confirm these details are correct")
       confirm = input("")
       if confirm == "yes" or confirm == "YES" or confirm == "Yes":
         print("STARTING TIMER")
         print("Don't forget to unpause it once it starts")
         g = 2 
       else:
         print("You entered an incorrect value, please try again!")
         print("Code will restart in")
         while a > 0: #Prints a countdown from 5 to 0 
          while paused:
           screen.update()
           time.sleep(0.1)
          print(a)
          time.sleep(1)
          a = a - 1
         
         
 
       #TURTLE SET-UP
       #>>>

       draw = turtle.Turtle() # Defining the turtles used in project 
       text = turtle.Turtle()
       state = turtle.Turtle()
       text_clone1 = turtle.Turtle()
       text_clone2 = turtle.Turtle()
       state_clone = turtle.Turtle()
       cycleturtle = turtle.Turtle()
      
       cyclesn = float(cycles)
       m = 0 
       n = 0 
       n = float(m)
       
       if total_secs > 0:
        cycles_fraction = cycles - (((elapsed / total_session_secs)))
       else:
        cycles_fraction = cycles
       cyclesmain = int(cycles_fraction)
    
       while n < cyclesn:
        n += 1
        while paused:
         screen.update()
         time.sleep(0.1)
       

        
        if cycles_fraction < 0:
         cyclesmain = 0
         cyclessecond = 0
        
        if cyclesmain < 1:
          print("Cycles left is less than 1")
          total_study_secs_clone =  int(total_secs * (cyclessecond/10) )
          if total_study_secs > total_study_secs_clone:
           total_study_secs = total_study_secs_clone
           total_break_secs = 0 
          elif total_study_secs < total_study_secs_clone:
           total_study_secs = total_study_secs
           total_break_secs = int(total_secs * (cyclessecond/10) ) - total_study_secs 

          
        
        d = 0 
        e = 0 
      

        text_clone1.clear()
        text_clone2.clear()
        draw.clear()
        text.clear()
        state.clear()
        state_clone.clear()
        cycleturtle.clear()

        turtle.setup(width = 800, height = 800) # Turtle screen settings 
        screen = turtle.Screen()
        screen.bgcolor("Black")
        screen.tracer(0)
        screen.listen()
        screen.onkey(toggle_pause, "space")
 
        state.pencolor("Purple") # Turtle settings 
        text.color("Purple")
        draw.pencolor("Purple")
        text_clone1.pencolor("Purple")
        text_clone2.pencolor("Purple")
        state_clone.pencolor("Purple")
        cycleturtle.pencolor("White")
        state_clone.pensize(10)
        draw.pensize(20)
  
        draw.hideturtle() # Making turtle sprites invisible
        text.hideturtle()
        state.hideturtle()
        text_clone2.hideturtle()
        text_clone1.hideturtle()
        state_clone.hideturtle()
        cycleturtle.hideturtle()

         
  
        draw.penup() # Lifting turtles pens 
        text.penup()
        state.penup()
        text_clone1.penup()
        text_clone2.penup()
        state_clone.penup()
        cycleturtle.penup()
  
        draw.goto(0,300) # Setting turtles starting positions
        draw.left(180) 
        state.goto(-300,280)
        text.goto(0,0)
        text_clone1.goto(0,100)
        text_clone2.goto(0,-70)
        cycleturtle.goto(-300,190)
  
        text_clone1.goto(0,100)
        text_clone2.goto(0,-70)
        state_clone.goto (-300,375)
        state_clone.left(180)
  
  
        draw.pendown() # Dropping turtles pens
        text.pendown()
        state.pendown()
        state_clone.pendown()
        cycleturtle.pendown()
  
        while e < total_study_secs:
         while paused:
          screen.update()
          time.sleep(0.1)
         state_clone.forward(0.25)
         state_clone.left(360/total_secs)
         e = e + 1
        e = 0 
        state_clone.color("Green")
        while e < total_break_secs:
          while paused:
           screen.update()
           time.sleep(0.1)
          state_clone.forward(0.25)
          state_clone.left(360/total_secs)
          e = e + 1 
 
          
  
        cycle_turtle_write = f"{cyclesmain}.{cyclessecond} CYCLES"
  
        #STARTING STUDY MODE
        #>>>
  
        v = total_study_secs - 1 #Setting starting seconds to 1 less than what they should be to ensure correct timing 
  
        state.write("Study", align  = "center", font = ("Arial",30,"bold")) # Writing the state in top left corner 
        cycleturtle.write(cycle_turtle_write, align = "center", font = ("Arial",15,"bold"))
  
        d = 0

        if g == 2:
          paused = True
        else:
          paused = False
        
        text.write("Press the spacebar to start!", align  = "center", font = ("Arial",30,"bold"))

        while d < total_study_secs:

          

         

          cycle_turtle_write = f"{cyclesmain}.{cyclessecond} CYCLES"
          cycleturtle.clear()
          cycleturtle.write(cycle_turtle_write, align="center", font=("Arial",15,"bold"))

          if total_secs > 0:
           cycles_fraction = cycles - (((elapsed / total_session_secs)))
          else:
           cycles_fraction = cycles
          cyclesmain = int(cycles_fraction)
          cyclessecond = int(round((cycles_fraction - cyclesmain) * 10))

          if cycles_fraction < 0:
           cyclesmain = 0
           cyclessecond = 0

          while paused:
           screen.update()
           time.sleep(0.1)
       
          draw.forward ((360/total_study_secs) * 5) # Moves the drawing turtle the appropriate distance and angle
          draw.left (360 / total_study_secs) 
  
          vvar = int(v)               # Re-defining Variables 
          vvar_hours = int(v//3600)
          vvar_mins = int(v//60)
          vvar_mins_div6   = int((vvar_mins/6)+1) 
          if vvar_mins < 10:
            vvar_mins = f"0{vvar_mins}"
          vvar_secs = int(v%60)
          if vvar_secs < 10:
            vvar_secs = f"0{vvar_secs}"
  
          now = datetime.now(ZoneInfo(finaltimezone))
          time_str = now.strftime ("%H:%M:%S")
  
          vvar2 = f"{vvar_hours}:{vvar_mins}:{vvar_secs}" # Current time remaining is defined 
          vvar_clone1 = f"{vvar_hours}.{vvar_mins_div6  }Hrs"
  
          text.clear() # resets text display
          text_clone1.clear()
          text_clone2.clear()
          text.write(vvar2, align  = "center", font = ("Arial",50,"bold"))
          text_clone1.write(vvar_clone1, align = "center", font = ("Arial",15, "bold"))
          text_clone2.write(time_str, align = "center", font = ("Arial", 15, "bold") )
  
          v -= 1
          elapsed = elapsed + 1
          d += 1
  
          screen.update() # update screen 
  
          time.sleep(1) # Internal timing 
  
         # STARTING BREAK MODE
        #>>>
  
   
        v = total_break_secs - 1 #Setting starting seconds to 1 less than what they should be to ensure correct timing 
  
        draw.pencolor("Green") # Turtle colours updated 
        state.pencolor("Green")
        text.pencolor("Green")
        text_clone1.pencolor("Green")
        text_clone2.pencolor("Green")
  
        draw.clear() # All text on screen cleared 
        state.clear()
        text.clear()
        text_clone1.clear()
        text_clone2.clear()
  
        state.write("Break", align  = "center", font = ("Arial",30,"bold")) # Writing the state in top left corner 
  
        d = total_study_secs

        while d < total_study_secs + total_break_secs:

          cycle_turtle_write = f"{cyclesmain}.{cyclessecond} CYCLES"
          cycleturtle.clear()
          cycleturtle.write(cycle_turtle_write, align="center", font=("Arial",15,"bold"))

          if total_secs > 0:
           cycles_fraction = cycles - (((elapsed / total_session_secs)))
          else:
           cycles_fraction = cycles
          cyclesmain = int(cycles_fraction)
          cyclessecond = int(round((cycles_fraction - cyclesmain) * 10)) 

          if cycles_fraction < 0:
             cyclesmain = 0
             cyclessecond = 0

          while paused:
           screen.update()
           time.sleep(0.1)
       
          draw.forward ((360/total_break_secs) * 5) # Moves the drawing turtle the appropriate distance and angle
          draw.left (360 / total_break_secs)
  
          vvar = int(v) # Re-defining variables 
          vvar_hours = int(v//3600)
          vvar_mins = int(v//60)
          vvar_mins_div6   = int((vvar_mins/6)+1) 
          if vvar_mins < 10:
            vvar_mins = f"0{vvar_mins}"
          vvar_secs = int(v%60)
          if vvar_secs < 10:
            vvar_secs = f"0{vvar_secs}"
  
          now = datetime.now(ZoneInfo(finaltimezone))
          time_str = now.strftime ("%H:%M:%S")
  
          vvar2 = f"{vvar_hours}:{vvar_mins}:{vvar_secs}" # Current time remaining is defined
          vvar_clone1 = f"{vvar_hours}.{vvar_mins_div6  }Hrs"
  
          text.clear()
          text_clone1.clear()
          text_clone2.clear()
          text.write(vvar2, align  = "center", font = ("Arial",50,"bold")) # Resets text display 
          text_clone1.write(vvar_clone1, align = "center", font = ("Arial",15, "bold"))
          text_clone2.write(time_str, align = "center", font = ("Arial", 15, "bold") )
  
          v -= 1
          elapsed = elapsed + 1
          d += 1
  
          screen.update() # update screen 
  
          time.sleep(1) # internal timing 
        
        draw.left(180)
        state_clone.left(180)
        
       
    
       
       
       
  
          
       x = x + 1 # Ends loop of original setting 

    #CUSTOM POMODORO TIMER SETTING
    #>>>
       
     
    elif classic == "c" or classic == "C":
     print("You have selected a custom pomodoro timer!")

     print("Enter how long you will study for at each time... (in mins) ")
     study_time = int(input("")) # Prompts uer to input how long they will study for inside each cycle 
     
     print("Enter how long you will have a break for before studying again... (in mins)")
     break_time = int(input("")) # Prompts user to input how long they will study for insiide each cycle 

     print("Enter how long your total study period will last... (Answer in a decimal of an hour) for example (1.2)")
     study_length = str(input("")) # Prompts user to enter how long their total session will last (hours)

     print ((decimal_to_hours(study_length)),"mins") # Uses decimal time to hrs,mins,secs algorthithm to convert total session time and output it 

     study_length2 = int(decimal_to_hours(study_length)) # study length determined using decimal to hrs,mins,secs algorithm

     study_length3 = study_time + break_time # Defines total cycle time as the time spent studying plus the break time 

     cycles = study_length2/study_length3 # calculates the number of cycles using total study time and total cycle time 
     if total_secs > 0:
      cycles_fraction = cycles - (((elapsed / total_session_secs)))
     else:
      cycles_fraction = cycles
     cyclesmain = int(cycles_fraction)
     cyclessecond = int(round((cycles_fraction - cyclesmain) * 10))

     print(cycles,"cycles") # Outputs to user all valuable information 
  
     if cycles_fraction < 0:
      cyclesmain = 0
      cyclessecond = 0

     
     cyclesmod = (study_length2 % study_length3)
     print(cyclesmod,"Mins remainder")
     cyclesdiv = (study_length2// study_length3 )
     print(cyclesdiv,"total cycles")
     print(cyclesdiv,"cycles and a",cyclesmod,"min remainder")

     total_secs = (study_time*60) + (break_time*60) # Calculates the total time of study time, break time and total time in secs to use for maths
     total_session_secs = study_length2 * 60
     total_study_secs = study_time*60
     total_break_secs = break_time * 60

     #TURTLE SET-UP
      #>>>

     draw = turtle.Turtle() # Defining the turtles used in project 
     text = turtle.Turtle()
     state = turtle.Turtle()
     text_clone1 = turtle.Turtle()
     text_clone2 = turtle.Turtle()
     state_clone = turtle.Turtle()
     cycleturtle = turtle.Turtle()

     turtle.setup(width = 800, height = 800) # Turtle screen settings 
     screen = turtle.Screen()
     screen.bgcolor("Black")
     screen.tracer(0)

     state.pencolor("Purple") # Turtle settings 
     text.color("Purple")
     draw.pencolor("Purple")
     text_clone1.color("Purple")
     text_clone2.color("Purple")
     state_clone.color("Purple")
     cycleturtle.color("White")
     draw.pensize(20)
     state_clone.pensize(10)

     draw.hideturtle() # Making turtle sprites invisible
     text.hideturtle()
     state.hideturtle()
     text_clone1.hideturtle()
     text_clone2.hideturtle()
     state_clone.hideturtle()
     cycleturtle.hideturtle()

     draw.penup() # Lifting turtles pens 
     text.penup()
     state.penup()
     text_clone1.penup()
     text_clone2.penup()
     state_clone.penup()
     cycleturtle.penup()

     draw.goto(0,300) # Setting turtles starting positions
     draw.left(180) 
     state.goto(-300,280)
     text.goto(0,0)
     text_clone1.goto(0,100)
     text_clone2.goto(0,-100)
     state_clone.goto (-300,375)
     state_clone.left(180)
     cycleturtle.goto(-300,190)

     draw.pendown() # Dropping turtles pens
     text.pendown()
     state.pendown()
     text_clone1.pendown()
     text_clone2.pendown()
     state_clone.pendown()
     cycleturtle.pendown()

     while e < total_study_secs:
       while paused:
        screen.update()
        time.sleep(0.1)
       state_clone.forward(0.25)
       state_clone.left(360/total_secs)
       e = e + 1
     e = 0 
     state_clone.color("Green")
     while e < total_break_secs:
       while paused:
        screen.update()
        time.sleep(0.1)
       state_clone.forward(0.25)
       state_clone.left(360/total_secs)
       e = e + 1 
  
     cycle_turtle_write = f"{cycles} CYCLES"

      #STARTING STUDY MODE
      #>>>

     v = total_study_secs - 1 #Setting starting seconds to 1 less than what they should be to ensure correct timing 

     state.write("Study", align  = "center", font = ("Wilko",30,"bold")) # Writing the state in top left corner 
     cycleturtle.write(cycle_turtle_write, align = "center", font = ("Arial",15,"bold"))

     while d < total_study_secs:
        
        cycle_turtle_write = f"{cyclesmain}.{cyclessecond} CYCLES"
        cycleturtle.clear()
        cycleturtle.write(cycle_turtle_write, align="center", font=("Arial",15,"bold"))

        cycles_fraction = cycles - (((elapsed / total_session_secs)))
        cyclesmain = int(cycles_fraction)
        cyclessecond = int(round((cycles_fraction - cyclesmain) * 10))

        if cycles_fraction < 0:
         cyclesmain = 0
         cyclessecond = 0

        while paused:
         screen.update()
         time.sleep(0.1)
        draw.forward ((360/total_study_secs) * 5) # Moves the drawing turtle the appropriate distance and angle
        draw.left (360 / total_study_secs)

        vvar = int(v)               # Re-defining Variables 
        vvar_hours = int(v//3600)
        vvar_mins = int(v//60)
        vvar_mins_div6   = int((vvar_mins/6)+1) 
        if vvar_mins < 10:
          vvar_mins = f"0{vvar_mins}"
        if int(vvar_mins) > 59:
          vvar_mins = vvar_mins - 59
        vvar_secs = int(v%60)
        if vvar_secs < 10:
          vvar_secs = f"0{vvar_secs}"

        now = datetime.now(ZoneInfo(finaltimezone))
        time_str = now.strftime ("%H:%M:%S")

        vvar2 = f"{vvar_hours}:{vvar_mins}:{vvar_secs}" # Current time remaining is defined
        vvar_clone1 = f"{vvar_hours}.{vvar_mins_div6  }Hrs" 

        text.clear() # resets text display
        text_clone1.clear()
        text_clone2.clear()
        text.write(vvar2, align  = "center", font = ("Arial",50,"bold"))
        text_clone1.write(vvar_clone1, align = "center", font = ("Arial",15, "bold"))
        text_clone2.write(time_str, align = "center", font = ("Arial", 15, "bold") )

        v -= 1
        elapsed = elapsed + 1
        d += 1

        screen.update() # update screen 

        time.sleep(1) # Internal timing 

      # STARTING BREAK MODE
      #>>>


     v = total_break_secs - 1 #Setting starting seconds to 1 less than what they should be to ensure correct timing 

     state.write("Break", align  = "center", font = ("Arial",30,"bold")) # Writing the state in top left corner 

     draw.clear() # All text on screen cleared 
     state.clear()
     text.clear()
     text_clone1.clear()
     text_clone2.clear()

     draw.pencolor("Green") # Turtle colours updated 
     state.pencolor("Green")
     text.pencolor("Green")
     text_clone1.pencolor ("Green")
     text_clone2.pencolor("Green")   

     d = total_study_secs

     while d < total_study_secs + total_break_secs:
        
        cycle_turtle_write = f"{cyclesmain}.{cyclessecond} CYCLES"
        cycleturtle.clear()
        cycleturtle.write(cycle_turtle_write, align="center", font=("Arial",15,"bold"))

        if total_secs > 0:
         cycles_fraction = cycles - (((elapsed / total_session_secs)))
        else:
         cycles_fraction = cycles
        cyclesmain = int(cycles_fraction)
        cyclessecond = int(round((cycles_fraction - cyclesmain) * 10))

        if cycles_fraction < 0:
         cyclesmain = 0
         cyclessecond = 0

        while paused:
         screen.update()
         time.sleep(0.1)
        draw.forward ((360/total_break_secs) * 5) # Moves the drawing turtle the appropriate distance and angle
        draw.left (360 / total_break_secs)

        vvar = int(v) # Re-defining variables 
        vvar_hours = int(v//3600)
        vvar_mins = int(v//60)
        vvar_mins_div6   = int((vvar_mins/6)+1) 
        if vvar_mins < 10:
          vvar_mins = f"0{vvar_mins}"
        if int(vvar_mins) > 59:
          vvar_mins = vvar_mins - 59
        vvar_secs = int(v%60)
        if vvar_secs < 10:
          vvar_secs = f"0{vvar_secs}"

        now = datetime.now(ZoneInfo(finaltimezone))
        time_str = now.strftime ("%H:%M:%S")

        vvar2 = f"{vvar_hours}:{vvar_mins}:{vvar_secs}" # Current time remaining is defined 
        vvar_clone1 = f"{vvar_hours}.{vvar_mins_div6  }Hrs"

        text.clear()
        text_clone1.clear()
        text_clone2.clear()
        text.write(vvar2, align  = "center", font = ("Arial",50,"bold")) # Resets text display 
        text_clone1.write(vvar_clone1, align = "center", font = ("Arial",15, "bold"))
        text_clone2.write(time_str, align = "center", font = ("Arial", 15, "bold") )

        v -= 1
        elapsed = elapsed + 1
        d += 1

        screen.update() # update screen 

        time.sleep(1) # internal timing 
     x = x + 1 
    else:
     print("You entered an incorrect value, please try again!") # Code if user enters an incorrect value

     print("Code will restart in") # Output shows a countdown from 5 
     while a > 0:
      while paused:
       screen.update()
       time.sleep(0.1)
      print(a)
      time.sleep(1)
      a = a - 1             

     print("CODE RESTARTING...") # Code clears some space in shell to start over so user doesn't get confused 
     while y <5:
       while paused:
        screen.update()
        time.sleep(0.1)
       print(">>>")
       y = y + 1
     x = 1
