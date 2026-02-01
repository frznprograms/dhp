import streamlit as st

st.set_page_config(
    page_title="Valentine?",
    page_icon="💘",
    layout="centered",
)

st.markdown(
    """
    <style>
      .block-container {
        padding-top: 3rem;
        max-width: 720px;
      }
      /* bigger buttons */
      div.stButton > button {
        width: 100%;
        padding: 0.9rem 1rem;
        font-size: 1.05rem;
        border-radius: 12px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

if "yes_clicked" not in st.session_state:
    st.session_state["yes_clicked"] = False

if "no_clicked" not in st.session_state:
    st.session_state["no_clicked"] = 0

# Optional: store the latest "No" message so it persists nicely
if "no_message" not in st.session_state:
    st.session_state["no_message"] = ""


def click_yes():
    st.session_state["yes_clicked"] = True


def click_no():
    st.session_state["no_clicked"] += 1
    count = st.session_state["no_clicked"]

    messages = {
        1: "What is your problem? 😤",
        2: "You want to test me is it? 🤨",
        3: "Keep this up and I'm going to crash the page.",
        4: "Fine, waste my effort then.",
    }
    st.session_state["no_message"] = messages.get(count, "Okay enough. Refreshing...")

    if count > 4:
        st.session_state["no_clicked"] = 0
        st.session_state["no_message"] = ""


def page_question():
    st.subheader("Will you be my valentine? 💖", divider="red")

    # Buttons side-by-side
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.button("Yes!", on_click=click_yes, use_container_width=True)
    with col2:
        st.button("No", on_click=click_no, use_container_width=True)

    # Show the "No" message under the buttons
    if st.session_state["no_message"]:
        st.info(st.session_state["no_message"])

    with st.expander("Need a hint?"):
        st.write("What's so difficult? Jollywell click yes now.")

        st.image(
            "assets/fail.gif",
            caption="Last warning 😤",
            use_container_width=True,
        )


def page_yes():
    st.balloons()
    st.header("Hooray!! 🥰💘")
    st.write("Correct answer. I knew you loved me 😌")

    st.image(
        "assets/success.gif",
        use_container_width=True,
    )

    st.success("Thank you for being my Valentine 💐")

    # Reset button (optional)
    if st.button("Replay 🔁", use_container_width=True):
        st.session_state["yes_clicked"] = False
        st.session_state["no_clicked"] = 0
        st.session_state["no_message"] = ""
        st.rerun()


# Router
if st.session_state["yes_clicked"]:
    page_yes()
else:
    page_question()
