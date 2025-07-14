import streamlit as st

# Set the page title
st.set_page_config(page_title="World of Asia R.")

# Define the photos and titles
photo_data = {
    "2025": [
        {"image": "Scan07.04.2025182414_001.jpg", "title": "Design 1"},
        {"image": "Scan07.04.2025182554_001.jpg", "title": "Design 1"},
        {"image": "Scan07.04.2025182647_001.jpg", "title": "Design 1"},
        {"image": "Scan07.04.2025182746_001.jpg", "title": "Design 1"}

       ]
}
        
# Create tabs
tabs = st.tabs([ "2024", "2025","2026","2027"])

# Display photos for each tab
for tab_name, tab in zip(photo_data.keys(), tabs):
    with tab:
        st.title(tab_name)
        photos = photo_data[tab_name]
        cols = st.columns(1)
        for idx, photo in enumerate(photos):
            with cols[idx % 1]:
                st.image(photo["image"], width=1200)
                st.write(photo["title"])
                st.markdown("---")
