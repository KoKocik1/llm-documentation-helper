import streamlit as st
from Backend.core import run_llm
from Backend.utils import get_formatted_response


def initialize_session_state():
    """Initialize session state variables if they don't exist."""
    if "chat_answers_history" not in st.session_state:
        st.session_state.chat_answers_history = []
    if "user_prompt_history" not in st.session_state:
        st.session_state.user_prompt_history = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "sources_history" not in st.session_state:
        st.session_state.sources_history = []


def main():
    st.header("LangChain Documentation Helper")
    initialize_session_state()

    prompt = st.text_input(
        "Prompt", placeholder="Enter your prompt", key="prompt_input"
    )

    if prompt:
        if not prompt.strip():
            st.write("Please enter a prompt")
            return

        with st.spinner("Generating response..."):
            generated_response = run_llm(
                query=prompt, chat_history=st.session_state.chat_history
            )
            formatted_response, sources = get_formatted_response(generated_response)

            # Update session state
            st.session_state.user_prompt_history.append(prompt)
            st.session_state.chat_answers_history.append(formatted_response)
            st.session_state.sources_history.append(sources)
            st.session_state.chat_history.extend(
                [("human", prompt), ("ai", generated_response["result"])]
            )

    # Display chat history
    if st.session_state.chat_answers_history:
        for response, user_query, sources in zip(
            st.session_state.chat_answers_history,
            st.session_state.user_prompt_history,
            st.session_state.sources_history,
        ):
            st.chat_message("user").write(user_query)
            with st.chat_message("assistant"):
                st.markdown(response)
                cols = st.columns(len(sources))
                for i, (col, source) in enumerate(zip(cols, sources)):
                    with col:
                        st.link_button(
                            f"Source {i + 1}", source, use_container_width=True
                        )


if __name__ == "__main__":
    main()
