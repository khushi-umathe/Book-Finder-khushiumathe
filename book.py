import streamlit as st
import requests 
from urllib.parse import quote

st.set_page_config(page_title='Book Finder App',page_icon='📖')
st.title('Book Finder App 📖 ')
st.write('Discover The World Of Books')
book = st.text_input("Enter book name")


st.markdown(
    """
    <style>
    /* Main page background */
    .stApp {
        background: linear-gradient(135deg, #F5F7FA, #E8EEF5);
        color: #1E293B;
    }

    /* Main content width and spacing */
    .block-container {
        max-width: 1000px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }

    /* Main title */
    h1 {
        color: #172554;
        font-size: 2.6rem;
        font-weight: 800;
        letter-spacing: -1px;
    }

    /* Book titles */
    h2, h3 {
        color: #0F766E;
        font-weight: 700;
    }

    /* Description and general text */
    p, label {
        color: #475569;
        font-size: 1rem;
    }

    /* Search input */
    .stTextInput input {
        border: 1px solid #CBD5E1;
        border-radius: 10px;
        padding: 12px;
        background-color: #FFFFFF;
        color: #1E293B;
    }

    .stTextInput input:focus {
        border-color: #0F766E;
        box-shadow: 0 0 0 2px rgba(15, 118, 110, 0.15);
    }

    /* Search button */
    .stButton > button {
        background-color: #0F766E;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.8rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #115E59;
        color: white;
        border: none;
        transform: translateY(-2px);
    }

    /* Links */
    a {
        color: #0F766E !important;
        font-weight: 600;
    }

    /* Divider between books */
    hr {
        border: none;
        height: 1px;
        background-color: #D8E1EA;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
    }

    /* Images */
    img {
        border-radius: 8px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


if(st.button('Search')):
    response = requests.get(f'https://openlibrary.org/search.json?title={quote(book)}&limit=5')
    if(book):                
        if response.status_code == 200:
            st.success('Book data fetched successfully')
            data = response.json()
                    
            if(data['docs']):

                            
                for item in data['docs']:

                    title = item.get('title', 'Unknown Title')
                    authors = item.get('author_name', ['Unknown Author'])
                    year = item.get('first_publish_year', 'Unknown')

                    st.subheader(title)
                    st.write('Author:', ', '.join(authors[:2]))
                    st.write('First published:', year)

                                
                    cover_id = item.get('cover_i')

                    if(cover_id):
                        st.image(f'https://covers.openlibrary.org/b/id/{cover_id}-M.jpg',width=150)
                        
                    key = item.get('key')           

                        

                    if(key):
                        st.markdown(f'[View Book Details](https://openlibrary.org{key})')
                                    

                    st.divider()

            else:
              st.warning('No books found. Try another title.')

        else:
          st.error('Unable to fetch book data')

    else:
      st.warning('Please enter a book name')

       