import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.markdown(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-HSGDVVJX6K"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-HSGDVVJX6K');
    </script>
   
    """,
    unsafe_allow_html=True
)

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
    st.header(":red[Passionate for understanding users' needs and good at multitasking!]")
    st.write("I enjoy finding ways to automate stuff and interpret data efficiently.")
    st.write("[Explore more about my work>](https://github.com/vicky-playground)")

with right_column:
    st_lottie(lottie_gif, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("About Me")
    st.write('##')
    st.write(
        """
        Unlike many peers in the industry who started their careers by choosing business and information technology as their undergrad majors, my journey had a rather bumpy start. Not fully aware of my interests, I chose what I was good at, mathematics, as my area of study and pursued statistics as a major. However, I slowly lost my passion for learning and felt disoriented about my future as I started skipping classes with a group of disaffected students. Without a clear future direction, my grades in National Taipei University suffered, and eventually, I decided to withdraw from the program and found employment to seek clarity.

I landed my first IT-related position as a junior business developer at a cross-national travel e-commerce company, three years after I withdrew from my program and then learned Python for exploratory data analysis. There, I discovered my passion for the alignment of technology and business strategy. To gain insights and find core competence, I did analyses for hotel booking demand, industry trends, competitors, supplier profitability, and feature usage. Also, I collaborated with cross-functional teams to liaise software-related functions to perform system analyses and make minimum viable product proposals to meet market demand. One major milestone was identifying a gap in the system and user booking experience while being responsible for consolidating the booking information of more than 1,200 hotels. To maximize profit and minimize the risk of overbooking, I took the initiative to approach my supervisor and take upon myself to monitor and troubleshoot all the listing API integration. The process made me realize that, not only do I have a passion for programming, but I also have an innate talent for seeing the missing puzzle pieces and providing solutions. Having finally found my passion and new clarity about my future career path, I decided to return to Fu Jen Catholic University to officially obtain a bachelor's degree in Software Engineering and Digital Innovation Applications while working full-time.

Two years ago, I successfully advanced my career and secured a position as a business relationship manager at an HR management system company. To lower the churn rate and raise the usage, I actively engage with Product to collaboratively create a UX roadmap from research to wireframing and write product specs, and offer clients solutions on a daily basis. By conducting usability testing, analyzing user activity, dissecting formulas of employment insurance with Java, and handling data with SQL, I preventively spot problems to ensure the system runs optimally and complies with labor law. To better strengthen my solid skills in the IT field, I applied for the master's degree in Information Systems and Technology at YorkU, and luckily got the fellowship covering all the tuition and most of the costs of living.

I was once young and rebellious but now I have found ways to harness that energy into something I love and am passionate about: growing business by analyzing data and satifying customers with providing right solutions. Having once been lost, I am now ever more ambitious and motivated to dedicate myself to the industry of information technology and pursue further studies without hesitation. My authentic happiness lies in surpassing yesterday's self. This driving force can be proved by the activities I attended, the GitHub projects I built, and Medium articles written in my leisure time. My intrinsic drive allows me to evolve and learn constantly without external force. With the hard skills and soft skills accumulated from the past, I am confident that my determination and thirst for success make me the ideal candidate for your company. Thank you for your consideration and I look forward to joining the team.


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
        st.markdown("[Checkout the project source code here...](https://github.com/vicky-playground/origin)")


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




