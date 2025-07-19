import streamlit as st
from gallery import photo_data
from gallery import photo_tabs

# Set the page title
title = "Portfolio of Asia R."
st.set_page_config(page_title=title)
st.title(body=title)
# Define the photos and titles

# Create tabs

tabs = st.tabs(photo_tabs)

# Display photos for each tab
for tab_name, tab in zip(photo_data.keys(), tabs):
        with tab:
            st.title(tab_name)
            photos = photo_data[tab_name]
            cols = st.columns(1)
            for idx, photo in enumerate(photos):
                with cols[idx % 1]:
                    st.image(photo["image"], width=1200  )
                    st.write(photo["title"])
                    st.markdown("---")
