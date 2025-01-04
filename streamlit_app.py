import streamlit as st
from PIL import Image

# Function for each individual page
def page1():
    st.title("Feature 1: Page 1")
    st.write("This is Page 1.")
    st.text_input("Enter some data for Page 1")

def page2():
    st.title("Feature 2: Page 2")
    st.write("This is Page 2.")
    st.text_input("Enter some data for Page 2")

def page3():
    st.title("Feature 3: Page 3")
    st.write("This is Page 3.")
    st.text_input("Enter some data for Page 3")

def page4():
    st.title("Feature 4: Page 4")
    st.write("This is Page 4.")
    st.text_input("Enter some data for Page 4")

def page5():
    st.title("Feature 5: Page 5")
    st.write("This is Page 5.")
    st.text_input("Enter some data for Page 5")

def page6():
    st.title("Feature 6: Page 6")
    st.write("This is Page 6.")
    st.text_input("Enter some data for Page 6")

def page7():
    st.title("Feature 7: Page 7")
    st.write("This is Page 7.")
    st.text_input("Enter some data for Page 7")

# Footer with customizable text
def footer():
    custom_footer = st.text_area("Enter footer information", "Your custom footer info goes here.")
    st.write(custom_footer)

# Main function to display the home page and navigation
def main():
    # Sidebar Navigation
    page_options = ["Home", "Page 1", "Page 2", "Page 3", "Page 4", "Page 5", "Page 6", "Page 7"]
    selected_page = st.sidebar.radio("Navigate", page_options)

    # Home Page Content
    if selected_page == "Home":
        st.title("Welcome to the Home Page")
        
        # Editable Columns and Image Boxes on Home Page
        col1, col2 = st.columns(2)
        
        with col1:
            st.header("Column 1: Editable")
            st.text_input("Input something here")
        
        with col2:
            st.header("Column 2: Image Box")
            uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
            if uploaded_image:
                img = Image.open(uploaded_image)
                st.image(img, caption="Uploaded Image", use_column_width=True)
        
        # Display Icons for Navigation to 7 Pages
        st.write("### Click an Icon to Go to the Respective Page")
        icon_col1, icon_col2, icon_col3 = st.columns(3)
        
        with icon_col1:
            if st.button("🔧 Page 1"):
                selected_page = "Page 1"
        
        with icon_col2:
            if st.button("⚙️ Page 2"):
                selected_page = "Page 2"
        
        with icon_col3:
            if st.button("🔩 Page 3"):
                selected_page = "Page 3"
        
        st.write("### Footer Section")
        footer()

    # Navigate to individual pages
    elif selected_page == "Page 1":
        page1()
        footer()

    elif selected_page == "Page 2":
        page2()
        footer()

    elif selected_page == "Page 3":
        page3()
        footer()

    elif selected_page == "Page 4":
        page4()
        footer()

    elif selected_page == "Page 5":
        page5()
        footer()

    elif selected_page == "Page 6":
        page6()
        footer()

    elif selected_page == "Page 7":
        page7()
        footer()

# Running the app
if __name__ == "__main__":
    main()
