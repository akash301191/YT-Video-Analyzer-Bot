# YT Video Analyzer Bot

YT Video Analyzer Bot is an intelligent Streamlit application that dissects YouTube videos into structured outlines, timestamped summaries, key takeaways, and visual highlights—making video content easier to navigate, study, and review. Powered by [Agno](https://github.com/agno-agi/agno) and OpenAI's GPT-4o, the bot transforms long-form videos into clean, digestible markdown reports in just one click.

## Folder Structure

```
YT-Video-Analyzer-Bot/
├── yt-video-analyzer-bot.py
├── README.md
└── requirements.txt
```

* **yt-video-analyzer-bot.py**: The main Streamlit application.
* **requirements.txt**: Required Python packages.
* **README.md**: This documentation file.

## Features

* **YouTube URL Input**
  Paste the URL of any YouTube video you want to analyze—ideal for tutorials, lectures, reviews, and interviews.

* **AI-Powered Video Analysis**
  The YouTube Agent processes the video structure, detects major topic transitions, and produces well-organized markdown output with timestamps.

* **Structured Breakdown**
  Each video is analyzed across four key dimensions:
  - 📺 Video Overview  
  - 🕑 Timestamped Outline  
  - ⭐ Key Insights & Takeaways  
  - 🖼️ Visual & Practical Notes

* **Markdown Output**
  Clean, reader-friendly markdown with headers, bullet points, and emojis to represent content types like 📚 Educational or 💻 Technical.

* **Download Option**
  Save the full video analysis as a `.md` file with one click.

* **Clean Streamlit UI**
  Minimal, responsive interface built with Streamlit for a seamless user experience.

## Prerequisites

* Python 3.11 or higher  
* An OpenAI API key ([Get one here](https://platform.openai.com/account/api-keys))

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/akash301191/YT-Video-Analyzer-Bot.git
   cd YT-Video-Analyzer-Bot
    ```

2. **(Optional) Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   # or
   venv\Scripts\activate           # On Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the app**:

   ```bash
   streamlit run yt-video-analyzer-bot.py
   ```

2. **In your browser**:

   * Add your OpenAI API key in the sidebar.
   * Paste the URL of a YouTube video you want to analyze.
   * Click **🎬 Analyze This Video**.
   * View and download the AI-generated video report.

3. **Download Option**
   Use the **📥 Download Report** button to save your analysis as a `.md` file for future reference or sharing.

## Code Overview

* **`render_sidebar()`**: Accepts and stores the OpenAI API key via the sidebar.
* **`render_video_input()`**: Captures the YouTube video URL input.
* **`generate_video_analysis()`**:
  * Instantiates a YouTube Agent using Agno and OpenAI's GPT-4o
  * Analyzes the video in multiple stages with consistent formatting
  * Returns the full markdown report
* **`main()`**: Orchestrates layout, event handling, and report rendering.

## Contributions

Contributions are welcome! If you'd like to suggest features, fix bugs, or improve the UI, feel free to fork the repo and submit a pull request. Please ensure your code is clean and aligns with the project's purpose.
