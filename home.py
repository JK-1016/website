import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

ga_html = """
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-PXWDQVC');</script>
<!-- End Google Tag Manager -->
</head>

<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-PXWDQVC"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
</body>

"""

st.markdown(ga_html,unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

#loading assets
st.image(Image.open("images/banner.png"),caption = "How the coworkers described me.")
lottie_gif = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_zboivc9e.json")
img_proj1 = Image.open("images/1.png")
img_proj2 = Image.open("images/2.png")
img_proj3 = Image.open("images/3.png")

left_column,right_column = st.columns(2)

with left_column:
    st.subheader("Hi, I am Vicky :wave:")
    st.header(":red[Passionate for understanding users' needs and data analytics!]")
    st.write("I enjoy finding ways to automate stuff and interpret data efficiently.")
    st.write("**[My links >](https://linktr.ee/vickytc)**")

with right_column:
    st_lottie(lottie_gif, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Who am I?")
    st.write('##')
    st.write(
        """
**Being an expert with a broad knowledge base and deep expertise in the IT field has always been my ultimate goal.** I got a degree in software engineering while working full-time. It was certainly a challenge but it has allowed me to develop better time management skills. Having once lost my way, I never thought about giving up this time. My commitment to succeed has pushed me to go further. By consistently challenging the status quo and applying my updated knowledge, I became the first and only business developer in AsiaYo who was assigned to work alongside a team of engineers to handle anomaly detection of API integration. After being promoted to a key account manager in the midst of company downsizing due to the pandemic, I’ve broadened my skills in team training, user journey optimization, and business analytics. I also deliberately fought for the opportunities to build product requirements documents with the developers. This process made me realize that I felt the most rewarding when I could increase higher product usage and consequently reduce the churn rate by creating values for the software users. Therefore, I honed in and secured a position as a business relationship manager at a Singaporean HR information system company, helping clients find their latent needs and make the most of our solutions. My professional trajectory has shown that I am always moving towards my goal. 

The struggle in my nontraditional self-exploration path is indescribable, but the lessons learned make it all worth it. Whenever I pulled through something, I would ask myself: “What can I learn from this experience?” and “How can I do better next time?” During the whole process, I acquired a better analytical mindset and skills, a daring heart to do something new, an attribute of seeking inputs from others, and unstoppable perseverance born from overcoming internal struggles under extreme pressure. My authentic happiness lies in surpassing yesterday's self. This driving force can be proved by the activities I attended, the GitHub projects I built, and Medium articles written in my leisure time. My intrinsic drive allows me to evolve and learn constantly without external force. With the hard skills and soft skills accumulated from the past, now, I can confidently say that I am a problem solver having an insatiable appetite for pushing myself to manage time better for new challenges and think out of the box. 

        """
    )

# change the font size
st.markdown("""
    <style>
    .big-font {
        font-size:26px !important;
    }
    </style>
    """, unsafe_allow_html=True)


with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    st.subheader("1. Website")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_proj2)
    with text_column:
        st.markdown('<p class="big-font">Tour Booking Platform</p>', unsafe_allow_html=True)
        st.write(
            """
            Built by myself from the frontend to the backend (Python).
            """
        )
        st.markdown("[Checkout the website here...](http://3.15.192.155:3000/)")


with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_proj1)
    with text_column:
        st.markdown('<p class="big-font">Resume Builder Website</p>', unsafe_allow_html=True)
        st.write(
            """
            Using Java to develop the resume builder website with others.
            """
        )
        st.markdown("[Checkout the project source code here...](https://github.com/vicky-playground/resume)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_proj3)
    with text_column:
        st.markdown('<p class="big-font">My personal portfolio website</p>', unsafe_allow_html=True)
        st.write(
            """
            Built by myself from the frontend to the backend (Python).
            """
        )
        st.markdown("[Checkout the project source code here...](https://github.com/vicky-playground/origin)")



st.subheader("2. Data Analysis & Machine Learning:")
st.markdown('<p class="big-font"><a href="https://github.com/vicky-playground/EHR-GDP/blob/main/city_comparison_code/EHR%20City.ipynb" style="font-size: 26px"><li>Electronic Healthcare Record Subsidy Program and Socioeconomics</li></a></p>', unsafe_allow_html=True)
st.markdown('<p class="big-font"><a href="https://github.com/vicky-playground/ML-wine-quality" style="font-size: 26px"><li>Wine classification</li></a></p>', unsafe_allow_html=True)
st.markdown('<p class="big-font"><a href="https://dune.com/vickytc/custom-nft-dashboard" style="font-size: 26px"><li>NFT Transactions</li></a></p>', unsafe_allow_html=True)
st.markdown('<p class="big-font"><a href="https://public.tableau.com/app/profile/vickytc/viz/Hospital_16702548094680/Overview" style="font-size: 26px"><li>SunnyBrook Hospital Project using Tableau</li></a></p>', unsafe_allow_html=True)


with st.container():
    st.write("---")
    st.header("Get in Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/vickytc@yorku.ca" method="POST">
        <input type="hidden" name="_captcha value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column,right_column = st.columns(2)

    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty() 




