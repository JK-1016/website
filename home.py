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
st.image(Image.open("images/banner.png"),caption = "How my coworkers described me.")
lottie_gif = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_zboivc9e.json")
img_proj1 = Image.open("images/1.png")
img_proj2 = Image.open("images/2.png")
img_proj3 = Image.open("images/3.png")

left_column,right_column = st.columns(2)

with left_column:
    st.subheader("Hi, I am Vicky :wave:")
    st.header(":red[Passion for finding insights from data!]")
    st.write("I enjoy finding ways to streamline business process and interpret data efficiently.")
    st.write("**[My links >](https://linktr.ee/vickytc)**")

with right_column:
    st_lottie(lottie_gif, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("About Me")
    st.write('##')
    st.write(
        """
**:blue[Always exploring!]** 

My intrinsic drive allows me to evolve and learn constantly without external force. I have a degree in software engineering while working full-time. It was certainly a challenge but it has allowed me to develop better time management skills.
As far as my technical skillset is concerned, I’m familiar with SDLC not only from working with the engineering team but also from hands-on experience. One of my side projects was a travel website built from scratch using HTML, CSS, JavaScript, Python, and SQL. Also, I tapped into AWS EC2 to make it in the cloud now: http://3.15.192.155:3000/

In addition to my technical skills, I possess a strong commitment to project success. I have a proven track record of lowering the churn rate by 3% overall and executing successful projects with great ROI (560%).
The two tech companies I worked for before were a cloud-based software company and an eCommerce respectively. Both used agile methodology to build products, and therefore I’m used to daily stand-up meetings to collaborate with multi-functional teams. 
My commitment to succeed also allows me to be the first and only business developer in AsiaYo who was assigned to work alongside a team of engineers to handle anomaly detection of API integration. After being promoted to a key account manager in the midst of company downsizing due to the pandemic, I’ve broadened my skills in team training, user journey optimization, and business analytics. I also deliberately fought for opportunities to build product requirements documents with the developers. This process made me realize that I felt the most rewarded when I increased higher engagement rate and consequently reduced the churn rate by creating value for the users. Therefore, I honed in and secured a position as a Solution Implementation Consultant at Swingvy, a Samsung-funded Singaporean HR information system company, to help Taiwanese clients troubleshoot their issues, assist them with data wrangling and analyses, and worked closely with the engineering team based in Korea to redesign the product to cater to Taiwanese customers and comply with the local law.

Recently, machine learning is what I’m studying in the master's degree at YorkU. I’ve implemented various types of machine learning models in Python including regressors and classifiers after preprocessing datasets. Also, I will attend Canadian AI this June to learn more about cutting-edge technology and give a presentation about explainable AI. 

My professional trajectory has shown that I am always moving towards my goal. With the hard skills and soft skills accumulated from the past, I can confidently say that I'm ready for an opportunity for me to showcase my skills and determination for success.
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
st.markdown('<p class="big-font"><a href="https://public.tableau.com/app/profile/vickytc/viz/SunnybrookTeam/Summary" style="font-size: 26px"><li>SunnyBrook Hospital Project using Tableau</li></a></p>', unsafe_allow_html=True)


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




