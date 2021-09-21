import itertools
import random
from datetime import datetime, timedelta
import plotly.graph_objects as go
import numpy
import streamlit as st
from PIL import Image
from random import randint


def show_match_page():
    image = Image.open('banner/CGI_LinkedIn_banner_modern_office.jpg')
    st.image(image, use_column_width=True)

    primaryColor = "#e31937"
    secondaryBackgroundColor = "#e1e1e1"
    textColor = "#000000"

    def startAndEnd(day):
        dt = datetime.strptime(day, '%Y-%m-%d')
        start = dt - timedelta(days=dt.weekday())
        end = start + timedelta(days=6)
        return start, end

    st.header('View this weeks coffee chat match below')

    nameList = ['Isobel Stewart', 'Alex Stone', 'Anitha Ramalingam', 'Chloe Gallacher', 'Chris Bellingham',
                'Chris Magowan', 'Chris Nelis', 'Dave Edwards', 'Dave Miller', 'Elaine Porteous', 'Elisha Cooper',
                'Emma Gillespie', 'Euan Cameron', 'Gillian McPhillips', 'Guy Chisholm', 'Jack Penman', 'Kirsty Purden',
                'Linda Horsburgh', 'Ross McArthur', 'Ryan Sharkey', 'Senthamil Vijayakumar Pandiyan', 'Shaun Cooper',
                'Suresh Natesan', 'David Ballantyne', 'Campbell Roberts', 'Kirsty ramsay', 'Jean Hezghia',
                'Dylan Wright', 'David Anderson', 'Tara McGonigle', 'Grant Stalker', 'Athos Georgiou'
                ]

    optArray = numpy.load('numArr/OptArray.npy')
    optedIn = []

    for choice in range(0, len(optArray) - 2):
        if optArray[choice] == 1.0:
            optedIn.append(nameList[choice])

    def split_list(a_list):
        half = len(a_list) // 2
        return a_list[:half], a_list[half:]

    def oddEven(listA, listB):
        if len(listA) > len(listB):
            double = listA[-1] + ' + ' + (listA[0])
            listA[-1] = double
            del listA[0]
        if len(listB) > len(listA):
            double = listB[-1] + ' + ' + (listB[0])
            listB[-1] = double
            del listB[0]

        return listA, listB

    listLength = int(len(optedIn) / 2)
    organiserAttendeeGroups = []
    a, b = split_list(optedIn)

    for x in range(0, listLength):
        b.append(b.pop(b.index(b[0])))
        if (x % 2) == 0:
            organiserAttendeeGroups.append([a, b.copy()])
        else:
            organiserAttendeeGroups.append([b.copy(), a])

    week = int(datetime.date(datetime.today()).strftime("%V"))
    modTablePicker = week % listLength
    a, b = oddEven(organiserAttendeeGroups[modTablePicker][0], organiserAttendeeGroups[modTablePicker][1])
    fig = go.Figure(data=[go.Table(header=dict(values=['Meeting Organiser', 'Attendee'], fill_color=primaryColor),
                                   cells=dict(values=[a, b], fill_color=secondaryBackgroundColor))
                          ])
    fig.update_layout()
    st.plotly_chart(fig)
