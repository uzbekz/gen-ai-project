import streamlit as st
from story_gen import generate_story

st.title("👻 HauntScript: Horror Story Generator")

theme = st.text_input("Enter Horror Theme")
setting = st.text_input("Enter Setting")
characters = st.text_area("Enter Character Details")
twist = st.text_area("Enter Plot Twist (optional)")

if st.button("Generate Story"):
    if theme and setting and characters:
        # Build the prompt using the inputs
        prompt = (
            f"Write a horror story with the theme '{theme}', "
            f"set in '{setting}', involving the following characters: {characters}. "
        )
        if twist:
            prompt += f"Include this plot twist: {twist}."

        # Generate and display the story
        story = generate_story(prompt)
        st.subheader("Your Horror Story")
        st.write(story)
    else:
        st.warning("Please fill in all the required fields.")
