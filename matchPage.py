import itertools
import random

import streamlit as st
from PIL import Image


def show_match_page():
    # image = Image.open('banner/R.png')
    # st.image(image, use_column_width=True)

    st.header('View this weeks coffee chat match below')

    nameList = ['Isobel Stewart', 'Alex Stone', 'Anitha Ramalingam', 'Chloe Gallacher', 'Chris Bellingham',
                'Chris Magowan', 'Chris Nelis', 'Dave Edwards', 'Dave Miller', 'Elaine Porteous', 'Elisha Cooper',
                'Emma Gillespie', 'Euan Cameron', 'Gillian McPhillips', 'Guy Chisholm', 'Jack Penman', 'Kirsty Purden',
                'Linda Horsburgh', 'Ross McArthur', 'Ryan Sharkey', 'Senthamil Vijayakumar Pandiyan', 'Shaun Cooper',
                'Suresh Natesan', 'David Ballantyne', 'Campbell Roberts', 'Kirsty ramsay', 'Jean Hezghia',
                'Dylan Wright', 'David Anderson', 'Tara McGonigle', 'Grant Stalker', 'Athos Georgiou'
                ]

    def split_list(a_list):
        half = len(a_list) // 2
        return a_list[:half], a_list[half:]

    a, b = split_list(nameList)

    listLength = len(nameList)

    matches = random.sample(set(itertools.product(a, b)), listLength)

    st.write(matches)



