import streamlit as st

# Set the page title
st.set_page_config(page_title="World of Asia R.")

# Define the photos and titles
photo_data = {
    "2025": [
        {"image": "2025/P_20250326_195228.jpeg", "title": "World in our hands"}
    ],
    "2015": [
        {"image": "2015/P04_jpg.jpg", "title": "First..."}
    ],
    "Stories": [
        {"image": "Scan07.04.2025182414_001.jpg", "title": "Part 1"},
        {"image": "Scan07.04.2025182554_001.jpg", "title": "Part 2"},
        {"image": "Scan07.04.2025182647_001.jpg", "title": "Part 3"},
        {"image": "Scan07.04.2025182746_001.jpg", "title": "Part 4"}

    ]


}
        
# Create tabs
tabs = st.tabs([ "2025","2015", "Stories"])

# Display photos for each tab
for tab_name, tab in zip(photo_data.keys(), tabs):
    with tab:
        st.title(tab_name)
        photos = photo_data[tab_name]
        cols = st.columns(1)
        for idx, photo in enumerate(photos):
            with cols[idx % 1]:

                st.image(photo["image"], width=1200,  )
                st.write(photo["title"])
                st.markdown("---")
