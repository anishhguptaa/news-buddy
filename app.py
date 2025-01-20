import streamlit as st
from main import crew

st.title("News Article Generator")
topic = st.text_input("Enter the News Article topic:")

if st.button("Generate News Article") and topic:
    inputs = {"topic": topic}
    try:
        with st.spinner("Generating your news article!"):
            crew.kickoff(inputs=inputs)

            with open(f"news/{topic}_news.md", "r") as file:
                content = file.read()

            st.success("News Article generated successfully!")
            st.download_button(
                label="Download News Article",
                data=content,
                file_name=f"{topic}_news.md",
                mime="text/md",
            )
            st.markdown(content)

    except FileNotFoundError:
        st.error(f"The expected article was not generated: {topic}_news.md")
