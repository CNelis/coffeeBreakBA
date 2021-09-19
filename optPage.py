import streamlit as st
from PIL import Image


def show_opt_page():
    # image = Image.open('banner/R.png')
    # st.image(image, use_column_width=True)

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

    # nameList = nameList.sort()
    inOut = ['Im In!', 'Im Out!']

    for name in nameList:
        st.radio('Select one ' + name, inOut)
