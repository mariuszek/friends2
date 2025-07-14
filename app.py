import streamlit as st

# Set the page title
st.set_page_config(page_title="World of Asia R.")

# Define the photos and titles
photo_data = {
    "2025": [
        {"image": "img 101.jpg", "title": "Design 1"},
        {"image": "img 102.jpg", "title": "Design 2"},
        {"image": "img 103.jpg", "title": "Design 3"},
        {"image": "img 104.jpg", "title": "Design 4"},
        {"image": "img 105.jpg", "title": "Design 5"},
    ]
    /*,
    "Kobbari Bondam": [
        {"image": "img 1.jpg", "title": "Design 1"},
        {"image": "img 2.jpg", "title": "Design 2"},
        {"image": "img 3.jpg", "title": "Design 3"},
        {"image": "img 4.jpg", "title": "Design 4"},
        {"image": "img 5.jpg", "title": "Design 5"},
        {"image": "img 6.jpg", "title": "Design 6"},
        {"image": "img 7.jpg", "title": "Design 7"},
        {"image": "img 8.jpg", "title": "Design 8"},
        {"image": "img 9.jpg", "title": "Design 9"},
        {"image": "img 10.jpg", "title": "Design 10"},
        {"image": "img 11.jpg", "title": "Design 11"},
        {"image": "img12.jpg", "title": "Design 12"},
        {"image": "img 13.jpg", "title": "Design 13"},
        {"image": "img 14.jpg", "title": "Design 14"},
        {"image": "img 15.jpg", "title": "Design 15"},
        {"image": "img 16.jpg", "title": "Design 16"},
        {"image": "img 17.jpg", "title": "Design 17"},
        {"image": "img 18.jpg", "title": "Design 18"},
        {"image": "img 19.jpg", "title": "Design 19"},
        {"image": "img 20.jpg", "title": "Design 20"},
    ],
    "Kobbari kudikalu": [
        {"image": "img 301.jpg", "title": "Design 1"},
        {"image": "img 302.jpg", "title": "Design 2"},
        {"image": "img 303.jpg", "title": "Design 3"},
        {"image": "img 304.jpg", "title": "Design 4"},
        {"image": "img 305.jpg", "title": "Design 5"},
        {"image": "img 306.jpg", "title": "Design 6"},
        {"image": "img 307.jpg", "title": "Design 7"}
    ],
    "ungarala bindhelu": [
        {"image": "img 201.jpg", "title": "Design 1"},
        {"image": "img 202.jpg", "title": "Design 2"},
        {"image": "img 203.jpg", "title": "Design 3"},
        {"image": "img 204.jpg", "title": "Design 4"},
        {"image": "img 205.jpg", "title": "Design 5"},
        {"image": "img 206.jpg", "title": "Design 6"},
        {"image": "img 207.jpg", "title": "Design 7"},
        {"image": "img 208.jpg", "title": "Design 8"},
        {"image": "img 209.jpg", "title": "Design 9"},
        {"image": "img 210.jpg", "title": "Design 10"}
    ],
    "Garika muntha": [
        {"image": "img 501.jpg", "title": "Design 1"},
        {"image": "img 502.jpg", "title": "Design 2"},
        {"image": "img 503.jpg", "title": "Design 3"},
        {"image": "img 504.jpg", "title": "Design 4"},
        {"image": "img 505.jpg", "title": "Design 5"},
        {"image": "img 506.jpg", "title": "Design 6"},
        {"image": "img 507.jpg", "title": "Design 7"},
        {"image": "img 508.jpg", "title": "Design 8"},
        {"image": "img 509.jpg", "title": "Design 9"}
    ],
    "Kanyadanam set": [
        {"image": "img 601.jpg", "title": "Design 1"},
        {"image": "img 602.jpg", "title": "Design 2"},
        {"image": "img 603.jpg", "title": "Design 3"},
        {"image": "img 604.jpg", "title": "Design 4"},
        {"image": "img 605.jpg", "title": "Design 5"},
        {"image": "img 606.jpg", "title": "Design 6"},
        {"image": "img 607.jpg", "title": "Design 7"},
        {"image": "img 608.jpg", "title": "Design 8"},
        {"image": "img 609.jpg", "title": "Design 9"}
    ]*/
}

# Create tabs
tabs = st.tabs([ "2025","2026","2027"])

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
