import random
import tkinter
from tkinter.ttk import *
from tkinter import scrolledtext


window = tkinter.Tk()

window.title("Bespoke Document Generator")

# pack is used to show the object in the window

lab_name = tkinter.Label(window, text = "Name of student:", font=("Arial Bold", 20))
lab_name.grid(column=0, row=2)
name = tkinter.Entry(window, width=30)
name.grid(column=0, row=3)

rad1 = tkinter.Radiobutton(window, text='M', value=1)
rad2 = tkinter.Radiobutton(window, text='F', value=2)
rad1.grid(column=1, row=3)
rad2.grid(column=2, row=3)

l1 = tkinter.Label(window, text = "Bespoke Report Generator!", font=("Arial Bold", 20))
l1.grid(column=3, row=0)

lab_academic = tkinter.Label(window, text = "Academic:", font=("Arial Bold", 14))
lab_academic.grid(column=0, row=4)
combo1 = Combobox(window, width=15, justify="center", state="readonly")
combo1['values']= (1, 2, 3, 4, 5)
combo1.current(2)
combo1.grid(column=0, row=5)

lab_behaviour = tkinter.Label(window, text = "Behaviour:", font=("Arial Bold", 14))
lab_behaviour.grid(column=0, row=6)
combo2 = Combobox(window, width=15, justify="center", state="readonly")
combo2['values']= (1, 2, 3, 4, 5)
combo2.current(2)
combo2.TextAlign = 2
combo2.grid(column=0, row=7)

lab_participation = tkinter.Label(window, text = "Participation:", font=("Arial Bold", 14))
lab_participation.grid(column=0, row=8)
combo3 = Combobox(window, width=15, justify="center", state="readonly")
combo3['values']= (1, 2, 3, 4, 5)
combo3.current(2)
combo3.TextAlign = 2
combo3.grid(column=0, row=9)

lab_homework = tkinter.Label(window, text = "Homework:", font=("Arial Bold", 14))
lab_homework.grid(column=0, row=10)
combo4 = Combobox(window, width=15, justify="center", state="readonly")
combo4['values']= (1, 2, 3, 4, 5)
combo4.current(2)
combo4.TextAlign = 2
combo4.grid(column=0, row=11)

txt = scrolledtext.ScrolledText(window, width=60,height=10)
txt.grid(column=3, row=1)
txt.insert("1.0", "Select the appropriate choices and generate your bespoke student report here!")






def gen():


    # Input metrics on a scale of 1-5
    behaviour = combo2.current() + 1
    participation = combo3.current() + 1
    homework = combo4.current() + 1
    academic = combo1.current() + 1

    attribute_vals = [behaviour, participation, homework, academic]

    # input gender
    if rad1.select():
        male = True
    else:
        male = False

    # input first name
    first_name = name.get()
    #surname = "Raina"

    # Create correct belonging phrase
    if first_name[-1] == 's':
        belonging = first_name+'\''
    else:
        belonging = first_name+'\'s'


    # Create correct pronouns
    if male:
        his = " his "
        him = " him "
        he = " he "
        His = " His "
        Him = " Him "
        He = " He "
    else:
        his = " her "
        him = " her "
        he = " she "
        His = " Her "
        Him = " Her "
        He = " She "



    NUM_ATTRIBUTES = 4
    NUM_GRADES = 5
    TOTAL_FILES = 21

    # Get random number index for each attribute
    rand_nums = []
    for i in range(NUM_ATTRIBUTES):
        rand_nums.append(random.randint(0,TOTAL_FILES - 1))


    # Extract the phrases
    # List to store the phrases
    phrases = []
    for attribute_num in range(NUM_ATTRIBUTES):
        file = 'versions/' + str(rand_nums[attribute_num]) + '.txt'
        with open(file) as f:
            lines = f.readlines()

        phrase_index = (attribute_num * NUM_GRADES) + attribute_vals[attribute_num] - 1
        phrase = lines[phrase_index]

        # Correct for name
        phrase = phrase.replace("James\'", belonging)
        phrase = phrase.replace("James", first_name)

        # Correct for pronouns
        phrase = phrase.replace(" his ", his)
        phrase = phrase.replace(" him ", him)
        phrase = phrase.replace(" he ", he)
        phrase = phrase.replace(" His ", His)
        phrase = phrase.replace(" Him ", Him)
        phrase = phrase.replace(" He ", He)

        # Remove trailing new line
        phrase = phrase.rstrip("\n")

        phrases.append(phrase)


    # Randomise order of phrases
    random.shuffle(phrases)

    # Put together
    overall = ''
    for phrase in phrases:
        overall += (phrase + ' ')

    # Display on interface
    txt = scrolledtext.ScrolledText(window, width=60,height=10)
    txt.grid(column=3, row=1)
    txt.insert("1.0", overall)



bt = tkinter.Button(window, text="Generate", font=("Arial Bold", 18), bg="green", command=gen)
bt.grid(column=0, row=12)

window.geometry('900x700')
window.mainloop()
