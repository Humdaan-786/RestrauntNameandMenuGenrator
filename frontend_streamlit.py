import streamlit as st
import langchainhelper

st.title("Restuarant name and menu generator")
cusine=st.sidebar.selectbox(
    "Pick a Cusine",
    ("Select a Cuisine","Indian","American","British","Italian","French","Korean","Japanese","Hungarian","Taiwanese"
     ,"Coulambian","Mexiacan","Russian","Israilian","Irish" ))



if cusine != "Select a Cuisine":
    responce=langchainhelper.gen_op(cusine)
    # print(responce[0])
    responce= responce[0]

# Extract and clean the restaurant name
    restaurant_name = responce["restaurant_name"].split("\n")[0].strip()  # Get the first line, strip extra spaces

# Extract and clean the menu
    menu = responce["menu"].strip()  # Remove extra spaces

# Display the cleaned results
    print("Restaurant Name:", restaurant_name)
    print("\nMenu:")
    print(menu)

    st.header(f"{restaurant_name}")
    st.write("**Menu Items**")
    st.markdown(menu, unsafe_allow_html=True)
    # for item in menu:
    #     st.write("-", item)
    # menu_items=responce['menu'].strip().split(",")
    # st.write("**Menu Items**")
    # for item in menu_items:
    #     st.write("-",item)