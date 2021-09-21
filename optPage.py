import numpy
import streamlit as st
from PIL import Image


def show_opt_page():
    image = Image.open('banner/CGI_LinkedIn_banner_modern_office.jpg')
    st.image(image, use_column_width=True)

    st.header('Opt in / out of coffee chats')

    optOptions()


def optOptions():
    nameList = ['Isobel Stewart', 'Alex Stone', 'Anitha Ramalingam', 'Chloe Gallacher', 'Chris Bellingham',
                'Chris Magowan', 'Chris Nelis', 'Dave Edwards', 'Dave Miller', 'Elaine Porteous', 'Elisha Cooper',
                'Emma Gillespie', 'Euan Cameron', 'Gillian McPhillips', 'Guy Chisholm', 'Jack Penman', 'Kirsty Purden',
                'Linda Horsburgh', 'Ross McArthur', 'Ryan Sharkey', 'Senthamil Vijayakumar Pandiyan', 'Shaun Cooper',
                'Suresh Natesan', 'David Ballantyne', 'Campbell Roberts', 'Kirsty ramsay', 'Jean Hezghia',
                'Dylan Wright',
                'David Anderson', 'Tara McGonigle', 'Grant Stalker', 'Athos Georgiou'
                ]

    optArray = numpy.load('numArr/OptArray.npy')

    inOut = ['Im In!', 'Im Out!']

    option = st.selectbox('Select your name', nameList)

    namePosition = nameList.index(option)

    if optArray[namePosition] == 1.0:
        select = st.radio('Select one ' + option, inOut, 0)
        if select == 'Im In!':
            optArray[namePosition] = 1.0
        else:
            optArray[namePosition] = 0.0
        numpy.save('numArr/OptArray.npy', optArray)
    else:
        select = st.radio('Select one ' + option, inOut, 1)
        if select == 'Im In!':
            optArray[namePosition] = 1.0
        else:
            optArray[namePosition] = 0.0
        numpy.save('numArr/OptArray.npy', optArray)
