import streamlit as st
from image_generator import generate_image
from vision import analyze_sketch
from prompt_builder import build_prompt
import os

# Page Config 
st.set_page_config(
    page_title="VisionCraft AI",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Styling 
st.markdown("""
    <style>
        html, body, .stApp {
            min-height: 100vh;
            background:
                radial-gradient(at 0% 0%, rgba(167, 139, 250, 0.28) 0px, transparent 50%),
                radial-gradient(at 100% 0%, rgba(244, 114, 182, 0.22) 0px, transparent 50%),
                radial-gradient(at 100% 100%, rgba(56, 189, 248, 0.22) 0px, transparent 50%),
                radial-gradient(at 0% 100%, rgba(129, 140, 248, 0.25) 0px, transparent 50%),
                #f3f0fb;
            background-attachment: fixed;
        }

        section[data-testid="stSidebar"] {
            display: none;
        }

        .block-container {
            max-width: 1150px;
            padding: 1.2rem 2rem 3rem 2rem;
        }

        .block-container > div > .stMarkdown p,
        .block-container > div > .stMarkdown h1,
        .block-container > div > .stMarkdown h2,
        .block-container > div > .stMarkdown h3 {
            color: #2b2350;
        }

        .navbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.65);
            backdrop-filter: blur(18px);
            -webkit-backdrop-filter: blur(18px);
            border: 1px solid rgba(123, 92, 255, 0.15);
            border-radius: 20px;
            padding: 1rem 1.8rem;
            margin-bottom: 1.8rem;
            box-shadow: 0 8px 28px rgba(80, 60, 140, 0.12);
        }
        .navbar-title {
            font-size: 1.35rem;
            font-weight: 800;
            color: #2b2350;
            margin: 0;
        }

        .stButton > button,
        div[data-testid="stHorizontalBlock"] button {
            border-radius: 999px !important;
            font-weight: 600 !important;
            border: none !important;
            transition: transform 0.15s ease, box-shadow 0.15s ease, filter 0.15s ease !important;
        }

        button[kind="secondary"] {
            background-color: rgba(123, 92, 255, 0.10) !important;
            color: #4b3f99 !important;
        }
        button[kind="secondary"]:hover {
            background-color: rgba(123, 92, 255, 0.20) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(123, 92, 255, 0.25);
        }

        button[kind="primary"] {
            background: linear-gradient(90deg, #7b5cff, #ff6ec7) !important;
            color: white !important;
            box-shadow: 0 4px 16px rgba(123, 92, 255, 0.35);
        }
        button[kind="primary"]:hover {
            filter: brightness(1.08);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(123, 92, 255, 0.5);
        }
        button[kind="primary"]:active,
        button[kind="secondary"]:active {
            transform: translateY(0px);
        }

        .stButton > button {
            padding: 0.65rem 0;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] .stButton > button {
            border-radius: 12px !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(255, 255, 255, 0.88) !important;
            border-radius: 18px !important;
            border: none !important;
            padding: 0.6rem 1rem !important;
            box-shadow: 0 12px 30px rgba(80, 60, 140, 0.15);
            margin-bottom: 1.2rem;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] h1,
        div[data-testid="stVerticalBlockBorderWrapper"] h2,
        div[data-testid="stVerticalBlockBorderWrapper"] h3,
        div[data-testid="stVerticalBlockBorderWrapper"] p,
        div[data-testid="stVerticalBlockBorderWrapper"] label,
        div[data-testid="stVerticalBlockBorderWrapper"] span {
            color: #2b2350 !important;
        }

        .example-box {
            background-color: rgba(123, 92, 255, 0.08);
            border-left: 3px solid #7b5cff;
            padding: 0.6rem 0.9rem;
            border-radius: 6px;
            font-size: 0.85rem;
            color: #2b2350 !important;
        }

        .app-footer {
            text-align: center;
            color: #6a6190;
            font-size: 0.8rem;
            margin-top: 2.5rem;
        }
    </style>
""", unsafe_allow_html=True)

if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []
if "page" not in st.session_state:
    st.session_state.page = "text"

# FLOATING TOP NAVBAR

st.markdown('<div class="navbar">', unsafe_allow_html=True)
logo_col, nav_col1, nav_col2, spacer_col = st.columns([2.5, 1.3, 1.5, 2.2])

with logo_col:
    st.markdown('<p class="navbar-title">VisionCraft AI</p>', unsafe_allow_html=True)

with nav_col1:
    if st.button(
        "Text to Image",
        use_container_width=True,
        type="primary" if st.session_state.page == "text" else "secondary"
    ):
        st.session_state.page = "text"

with nav_col2:
    if st.button(
        "Sketch to Image",
        use_container_width=True,
        type="primary" if st.session_state.page == "sketch" else "secondary"
    ):
        st.session_state.page = "sketch"



st.markdown('</div>', unsafe_allow_html=True)


# TEXT TO IMAGE

if st.session_state.page == "text":

    card = st.container(border=True)
    with card:
        st.header("Generate an Image from Text")
        st.write("Describe what you want to see — the more specific, the better the result.")

        col1, col2 = st.columns([3, 1])

        with col1:
            prompt = st.text_area(
                "Your prompt",
                height=160,
                placeholder="e.g. A futuristic AI robot standing in a cyberpunk city at sunset, "
                            "blue neon lights, ultra realistic, cinematic lighting"
            )

        with col2:
            style = st.selectbox("Style", ["Realistic", "Cartoon", "Cyberpunk", "Watercolor", "3D Render"])
            size = st.select_slider("Size", options=["512x512", "768x768", "1024x1024"], value="1024x1024")

        with st.expander("Click for an example"):
            st.markdown(
                '<div class="example-box">"A cozy cabin in the mountains during snowfall, '
                'warm lights glowing through the windows, soft evening tones, painterly style."</div>',
                unsafe_allow_html=True
            )

        generate = st.button("✨ Generate Image", use_container_width=True, type="primary")

        if generate:
            if not prompt.strip():
                st.warning("Hey, you forgot to write a prompt!")
            elif len(prompt.strip()) < 8:
                st.warning("That prompt's a bit too short — try adding more detail.")
            else:
                st.session_state.prompt_history.append(prompt.strip())
                with st.spinner("Generating image..."):

                    final_prompt = f"""
                    {prompt}

                    Style: {style}

                    Image Size: {size}

                    High quality, detailed, professional artwork.
                    """

                    result = generate_image(final_prompt)

                if result.endswith(".png"):

                    st.success("Image generated successfully!")

                    st.image(result, use_container_width=True)

                    with open(result, "rb") as file:
                        st.download_button(
                            label="Download Image",
                            data=file,
                            file_name="generated_image.png",
                            mime="image/png",
                            use_container_width=True
                        )

                else:

                    st.error(result)

        if st.session_state.prompt_history:
            with st.expander(f"Recent prompts ({len(st.session_state.prompt_history)})"):
                for p in reversed(st.session_state.prompt_history[-5:]):
                    st.write(f"• {p[:70]}{'...' if len(p) > 70 else ''}")


# SKETCH TO IMAGE

else:

    card = st.container(border=True)
    with card:
        st.header("Turn a Rough Sketch into Real Art")
        st.write("Upload a sketch and let the model figure out what to make of it.")

        left, right = st.columns([1, 1])

        with left:
            uploaded_file = st.file_uploader(
                "Upload your sketch",
                type=["png", "jpg", "jpeg"],
                help="Works best with a clear photo of a hand-drawn sketch on plain paper."
            )

            extra_notes = st.text_input(
                "Anything to add? (optional)",
                placeholder="e.g. make it more colorful, add a night sky"
            )

        with right:
            if uploaded_file:
                st.image(uploaded_file, caption="Your sketch", width=320)
            else:
                st.info("No sketch uploaded yet.")

        analyze = st.button("🚀 Analyze Sketch", use_container_width=True, type="primary")

        if analyze:

            if uploaded_file is None:

                st.warning("Please upload an image first.")

            else:

                os.makedirs("input", exist_ok=True)

                image_path = os.path.join("input", uploaded_file.name)

                with open(image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                with st.spinner("Analyzing sketch..."):

                    vision_description = analyze_sketch(image_path)

                    final_prompt = build_prompt(
                        vision_description,
                        extra_notes
                    )

                    result = generate_image(final_prompt)

                if result.endswith(".png"):

                    st.success("Image generated successfully!")

                    st.image(result, use_container_width=True)

                    with open(result, "rb") as file:
                        st.download_button(
                            label="Download Image",
                            data=file,
                            file_name="generated_sketch.png",
                            mime="image/png",
                            use_container_width=True
                        )

                else:

                    st.error(result)

# Footer
st.markdown(
    '<div class="app-footer">Built with Streamlit • VisionCraft AI</div>',
    unsafe_allow_html=True
)