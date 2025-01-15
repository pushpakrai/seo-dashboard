import streamlit as st
from streamlit_elements import elements, mui, html
import pandas as pd
import numpy as np
from streamlit_extras.chart_container import chart_container
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.grid import grid
from streamlit_sortables import sort_items


my_grid = grid(2, 1, 2, vertical_align="bottom")

original_items = [
    {'header': 'first container',  'items': ['A', 'B', 'C']},
    {'header': 'second container', 'items': ['D', 'E', 'F']}
]

sorted_items = sort_items(original_items, multi_containers=True)

st.write(f'original_items: {original_items}')
st.write(f'sorted_items: {sorted_items}')

@st.cache_data
def generate_data():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    return chart_data

chart_data = generate_data()

chart_pd = pd.DataFrame(chart_data)

with my_grid.expander("Data Panel", expanded=True):
    filtered_df = dataframe_explorer(chart_pd, case=False)
    data = st.file_uploader("Upload a file")

my_grid.dataframe(filtered_df, use_container_width=True)

with my_grid.container():
    with chart_container(filtered_df):
        st.write("Data Spread")
        st.area_chart(filtered_df)


with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    from streamlit_elements import dashboard

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2),
        dashboard.Item("second_item", 2, 0, 2, 2),
        dashboard.Item("third_item", 0, 2, 1, 1),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

    with dashboard.Grid(layout):
        mui.Box("First item",key="first_item")
        mui.Paper("second item", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")

    # If you want to retrieve updated layout values as the user move or resize dashboard items,
    # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
        # You can save the layout in a file, or do anything you want with it.
        # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")