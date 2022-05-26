import streamlit as st
# Helper fucntions

def is_authenticated(user, password):
    user = user.lower()
    if (user == 'admin' and password == "pr3lzn070319zmvszxcg"):
        return True
    else:
        return False
def linespace_generator(n_spaces=1):
    for i in range(n_spaces):
        st.write("")
class PasswordNotFound(Exception):
    """
    Please check the file located at https://github.com/kenfus/streamlit-password/blob/master/streamlit_password.py
    """
    pass
     
# Implementation, should be used in the end of if __name__ == "__main__":

if __name__ == "__main__":
    st.sidebar.warning("**Please enter the Password.**")
    if st.sidebar.checkbox('Show hint 🔭', False):
        st.sidebar.write(
        r"""
            The hidden word is made up of 36 letters and numbers. 

            Thus, it has

            $(26 + 10) ^{20} \approx 1.34 × 10^{31}$ 
            
            possible combinations.

            If you make one guess every second, it will take you 

            $\frac{1.34 × 10^{31}}{60*60*24*365} \approx 4.2*10^{23}\text{ years}$

            to guess the word.

            Maybe there is another way to figure this out?
        """,
        unsafe_allow_html=True,
    )
        if st.sidebar.checkbox('That does not help me 😞 ', False):
            st.sidebar.write(
            r"""
            That is a shame... I wish there is something someone could do.

            Maybe at least the button below will cheer you up?
            """,
            unsafe_allow_html=True,
        )   
            show_ballons = st.sidebar.button("Show ballons 🎈")
            if show_ballons:
                st.balloons()
                show_ballons = False
            show_answer = st.sidebar.button("DEBUG: LOGIN")
            if show_answer:
                raise PasswordNotFound('Exception: Debug Password not found.\nCheck file located at https://github.com/kenfus/streamlit-password/blob/master/streamlit_password.py')

    user = st.text_input("Enter a user name", "admin")
    password = st.text_input("Enter a password", type="password")
    if is_authenticated(user, password):
        st.write("Access granted.")
        st.write('https://share.streamlit.io/kenfus/hangman-one/streamlit_hangman.py')

    else:
        st.write("Please enter your password.")
    linespace_generator(n_spaces=2)