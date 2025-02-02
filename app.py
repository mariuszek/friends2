import streamlit as st

# Set the page title
st.set_page_config(page_title="Photo Gallery App")

# Define the photos and titles
photo_data = {
    "Adduthera": [
        {"image": "img/Adduthera/img 101.jpg", "title": "Design 1"},
        {"image": "img/Adduthera/img 102.jpg", "title": "Design 2"},
        {"image": "img/Adduthera/img 103.jpg", "title": "Design 3"},
        {"image": "img/Adduthera/img 104.jpg", "title": "Design 4"},
        {"image": "img/Adduthera/img 105.jpg", "title": "Design 5"},
    ],
    "Kobbari Bondam": [
        {"image": "img/Kobbari Bondam/img 1.jpg", "title": "Design 1"},
        {"image": "img/Kobbari Bondam/img 2.jpg", "title": "Design 2"},
        {"image": "img/Kobbari Bondam/img 3.jpg", "title": "Design 3"},
        {"image": "img/Kobbari Bondam/img 4.jpg", "title": "Design 4"},
        {"image": "img/Kobbari Bondam/img 5.jpg", "title": "Design 5"},
        {"image": "img/Kobbari Bondam/img 6.jpg", "title": "Design 6"},
        {"image": "img/Kobbari Bondam/img 7.jpg", "title": "Design 7"},
        {"image": "img/Kobbari Bondam/img 8.jpg", "title": "Design 8"},
        {"image": "img/Kobbari Bondam/img 9.jpg", "title": "Design 9"},
        {"image": "img/Kobbari Bondam/img 10.jpg", "title": "Design 10"},
        {"image": "img/Kobbari Bondam/img 11.jpg", "title": "Design 11"},
        {"image": "img/Kobbari Bondam/img12.jpg", "title": "Design 12"},
        {"image": "img/Kobbari Bondam/img 13.jpg", "title": "Design 13"},
        {"image": "img/Kobbari Bondam/img 14.jpg", "title": "Design 14"},
        {"image": "img/Kobbari Bondam/img 15.jpg", "title": "Design 15"},
        {"image": "img/Kobbari Bondam/img 16.jpg", "title": "Design 16"},
        {"image": "img/Kobbari Bondam/img 17.jpg", "title": "Design 17"},
        {"image": "img/Kobbari Bondam/img 18.jpg", "title": "Design 18"},
        {"image": "img/Kobbari Bondam/img 19.jpg", "title": "Design 19"},
        {"image": "img/Kobbari Bondam/img 20.jpg", "title": "Design 20"},
    ],
    "Kobbari kudikalu": [
        {"image": "img/Kobbari kudikalu/img 301.jpg", "title": "Design 1"},
        {"image": "img/Kobbari kudikalu/img 302.jpg", "title": "Design 2"},
        {"image": "img/Kobbari kudikalu/img 303.jpg", "title": "Design 3"},
        {"image": "img/Kobbari kudikalu/img 304.jpg", "title": "Design 4"},
        {"image": "img/Kobbari kudikalu/img 305.jpg", "title": "Design 5"},
        {"image": "img/Kobbari kudikalu/img 306.jpg", "title": "Design 6"},
        {"image": "img/Kobbari kudikalu/img 307.jpg", "title": "Design 7"}
    ],
    "ungarala bindhelu": [
        {"image": "img/ungarala bindhelu/img 201.jpg", "title": "Design 1"},
        {"image": "img/ungarala bindhelu/img 202.jpg", "title": "Design 2"},
        {"image": "img/ungarala bindhelu/img 203.jpg", "title": "Design 3"},
        {"image": "img/ungarala bindhelu/img 204.jpg", "title": "Design 4"},
        {"image": "img/ungarala bindhelu/img 205.jpg", "title": "Design 5"},
        {"image": "img/ungarala bindhelu/img 206.jpg", "title": "Design 6"},
        {"image": "img/ungarala bindhelu/img 207.jpg", "title": "Design 7"},
        {"image": "img/ungarala bindhelu/img 208.jpg", "title": "Design 8"},
        {"image": "img/ungarala bindhelu/img 209.jpg", "title": "Design 9"},
        {"image": "img/ungarala bindhelu/img 210.jpg", "title": "Design 10"}
    ],
    "Garika muntha": [
        {"image": "img/Garika muntha/img 501.jpg", "title": "Design 1"},
        {"image": "img/Garika muntha/img 502.jpg", "title": "Design 2"},
        {"image": "img/Garika muntha/img 503.jpg", "title": "Design 3"},
        {"image": "img/Garika muntha/img 504.jpg", "title": "Design 4"},
        {"image": "img/Garika muntha/img 505.jpg", "title": "Design 5"},
        {"image": "img/Garika muntha/img 506.jpg", "title": "Design 6"},
        {"image": "img/Garika muntha/img 507.jpg", "title": "Design 7"},
        {"image": "img/Garika muntha/img 508.jpg", "title": "Design 8"},
        {"image": "img/Garika muntha/img 509.jpg", "title": "Design 9"}
    ],
    "Kanyadanam set": [
        {"image": "img/Kanyadanam set/img 601.jpg", "title": "Design 1"},
        {"image": "img/Kanyadanam set/img 602.jpg", "title": "Design 2"},
        {"image": "img/Kanyadanam set/img 603.jpg", "title": "Design 3"},
        {"image": "img/Kanyadanam set/img 604.jpg", "title": "Design 4"},
        {"image": "img/Kanyadanam set/img 605.jpg", "title": "Design 5"},
        {"image": "img/Kanyadanam set/img 606.jpg", "title": "Design 6"},
        {"image": "img/Kanyadanam set/img 607.jpg", "title": "Design 7"},
        {"image": "img/Kanyadanam set/img 608.jpg", "title": "Design 8"},
        {"image": "img/Kanyadanam set/img 609.jpg", "title": "Design 9"}
    ]
}

# Create tabs
tabs = st.tabs([ "Adduthera","Kobbari Bondam","Kobbari kudikalu","ungarala bindhelu","Garika muntha","Kanyadanam set"])

# Display photos for each tab
for tab_name, tab in zip(photo_data.keys(), tabs):
    with tab:
        st.title(tab_name)
        photos = photo_data[tab_name]
        cols = st.columns(2)
        for idx, photo in enumerate(photos):
            with cols[idx % 2]:
                st.image(photo["image"], width=300)
                st.write(photo["title"])
                st.markdown("---")
