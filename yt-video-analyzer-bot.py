from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.youtube import YouTubeTools
from textwrap import dedent

import streamlit as st

def render_sidebar():
    st.sidebar.title("🔐 API Configuration")
    st.sidebar.markdown("---")

    # OpenAI API Key input
    openai_api_key = st.sidebar.text_input(
        "OpenAI API Key",
        type="password",
        help="Don't have an API key? Get one [here](https://platform.openai.com/account/api-keys)."
    )
    if openai_api_key:
        st.session_state.openai_api_key = openai_api_key
        st.sidebar.success("✅ OpenAI API key updated!")

    st.sidebar.markdown("---")

def render_video_input():
    st.markdown("---")
    col1, col2 = st.columns(2)

    # Column 1: Video URL input
    with col1:
        st.subheader("📺 Enter YouTube Video URL")
        youtube_url = st.text_input(
            "Paste the URL of the YouTube video you'd like to analyze:",
            placeholder="https://www.youtube.com/watch?v=example"
        )

    return youtube_url

def generate_video_analysis(youtube_url: str) -> str:
    youtube_agent = Agent(
        name="YouTube Agent",
        model=OpenAIChat(id="gpt-4o", api_key=st.session_state.openai_api_key),
        tools=[YouTubeTools()],
        instructions=dedent("""\
            You are an expert YouTube content analyst. On each link you receive, follow this structured workflow:

            ## 🔍 Video Overview
            ### Metadata
            - Title  
            - Channel  
            - Publish date  
            - View count  
            - Duration  

            ### Classification
            - Video type (tutorial, review, lecture, demo, interview, etc.)  
            - Creator’s stated goal or thesis (1–2 sentences)

            ## 🕑 Timestamped Outline
            - Divide the full runtime into logical segments.
            - For each segment, provide:
              1. **[hh:mm:ss, hh:mm:ss] Segment Title**  
                 A concise summary of what happens in 3–4 bullet points.

            - Highlight transitions marked by topic shifts, demonstrations, or call-outs.

            ## ⭐ Key Insights & Takeaways
            - Bullet the top 3–5 “aha” points or actionable tips.  
            - Note any recommended follow-up resources (e.g., links shown on screen).

            ## 🖼️ Visual & Practical Notes
            - Describe on-screen diagrams, code snippets, or demos.  
            - Call out timestamps where visuals appear.  
            - Mention any “pro tips” the creator shares.

            ---
            ### Formatting Guidelines
            - Use emojis to tag content types:  
              📚 Educational  💻 Technical  🎮 Gaming  📱 Review  🎨 Creative  
            - Present everything in **Markdown**  
            - Use bullet lists and sub-lists for clarity  
            - Keep summaries tight: ≤ 2 sentences per segment  
                            
            ## Quality & Consistency Checks
            - Confirm timestamp accuracy matches video progress.  
            - Avoid speculation: only document what you can see or hear.  
            - Maintain uniform detail across all segments.

            **Always begin with `## 🔍 Video Overview` and end with `## ⭐ Key Insights & Takeaways`.**
        """),
        add_datetime_to_instructions=True,
        markdown=True,
    )

    youtube_response = youtube_agent.run(f"Analyze this video: {youtube_url}")
    youtube_analysis = youtube_response.content 

    return youtube_analysis

def main() -> None:
    # Page config
    st.set_page_config(page_title="YT Video Analyzer Bot", page_icon="🎬", layout="wide")

    # Custom styling
    st.markdown(
        """
        <style>
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        div[data-testid="stTextInput"] {
            max-width: 1200px;
            margin-left: auto;
            margin-right: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header and intro
    st.markdown("<h1 style='font-size: 2.5rem;'>🎬 YT Video Analyzer Bot</h1>", unsafe_allow_html=True)
    st.markdown(
        "Welcome to YT Video Analyzer Bot — an intelligent Streamlit application that dissects YouTube videos into structured outlines, topic summaries, and key takeaways—making content navigation and learning more efficient than ever.",
        unsafe_allow_html=True
    )

    render_sidebar()
    youtube_url = render_video_input()

    st.markdown("---")

    if st.button("🎬 Analyze This Video"):
        if not hasattr(st.session_state, "openai_api_key"):
            st.error("Please provide your OpenAI API key in the sidebar.")
        else:
            if youtube_url.strip() == "":
                st.error("Please enter a valid YouTube video URL.")
            else:
                with st.spinner("Analyzing the YouTube video..."):
                    youtube_analysis = generate_video_analysis(youtube_url)
                    st.session_state.youtube_analysis = youtube_analysis

    # Display analysis if available
    if "youtube_analysis" in st.session_state:
        st.markdown(st.session_state.youtube_analysis, unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Report",
            data=st.session_state.youtube_analysis,
            file_name="youtube_video_analysis.md",
            mime="text/markdown"
        )

if __name__ == "__main__":
    main()