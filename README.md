Social Media Analyzer 
A Advanced Topic Modeling and Sentiment Dashboard using NLP (Reddit Data) .machine learning project for topic discovery and sentiment insight visualization
Overview 🌍
AI, Machine Learning, Data This project analyzes public Reddit posts related to The pipeline collects, cleans, analyzes, and . Science, and Career Guidance visualizes social media data using Natural Language Processing (NLP), Topic Modeling, and Sentiment Analysis techniques. The goal is to provide an displaying detected topics (via LDA) and interactive Streamlit Dashboard .sentiment trends with WordClouds for each topic
This detailed document outlines the architecture, methodology, technologies, and execution steps required to deploy and understand the Social Media Analyzer .project
Project Structure 
,The repository is organized logically to separate data handling, analysis modules .and the final presentation layer (Streamlit application)
/social_media_analyzer

│

 # Streamlit dashboard (Dark mode + Persian font integration) ──├

│

/src ──├

andling Sentiment Analysis (e.g., using VADER or custom models) ──├   │

eprocessing, tokenization, stop-word removal, and lemmatization ──├   │

ichlet Allocation (LDA) model training and topic interpretation ──├   │

mbine CSV files from various subreddits into one master dataset ──├   │

ng routines, potentially integrating with PRAW or similar tools ──└   │











│

/data ──├

ory for untouched, original JSON/CSV outputs from the collector ──├   │

rocessed dataset used for model training and dashboard sourcing ──├   │

G files representing the top keywords for each discovered topic ──├   │

 # A static screenshot capturing the main Streamlit interface ──├   │

topic3_wordcloud.png      # Specific example visualization file ──└   │

│

# Exact list of Python package dependencies required for execution ──├

.README.md                     # Project documentation (this file) ──└
Workflow Breakdown ⚙️
:The project follows a standard, rigorous Machine Learning operational flow
NLP
Technique
Core Module(s)
Description
Step
Focus
Automated download of 
post titles and bodies
Data
External script/PRAW
from predefined
Data .1
Acquisition
integration
/subreddits (e.g., r
Collection
/MachineLearning, r 
.(cscareerquestions
,Tokenization 
lowercasing, removal of
Text

prepare_data.py

,URLs, punctuation
Data .2
Preprocessing

boilerplate text, and
Cleaning
/applying lemmatization 
.stemming
Training the Latent
Unsupervised

topic_modeler.py

Dirichlet Allocation (LDA)
Topic .3


model. Typically, 5 topics

Learning


Modeling


are selected based on

.coherence scores

NLP
Technique
Core Module(s)
Description
Step
Focus
,For each identified topic
generating a WordCloud
Text
 ,
topic_modeler.py
based on the top
.4
Visualization

analyzer.py
weighted terms and
Visualization
visualizing overall
.sentiment distribution
Deploying the cleaned
Interactive
(Streamlit)

app.py

,data, model artifacts
.5



and visualizations into an
Dashboard
Reporting







interactive web
Creation
.application
Technologies Used 💻
This project leverages a robust stack of modern data science and web
:development libraries
The primary programming language, chosen for its extensive : +Python 3.10	 •
.ecosystem in ML/NLP
for efficient DataFrame operations NumPy and Pandas : Data Manipulation	 •
.and numerical computation
for basic text processing (Natural Language Toolkit) NLTK : Core NLP	 •
for highly optimized Topic Modeling (LDA Gensim utilities and
.(implementation
potentially for feature extraction like TF-IDF) scikit-learn : Machine Learning	 •
.(or for base model structures
 for static plot generation, and the Seaborn and Matplotlib : Visualization	 •
.library for thematic visualization WordCloud
is used to rapidly prototype and deploy the Streamlit : Interactive Interface	 •
.results as a production-ready, dark-themed dashboard

Topic Modeling Deep Dive (LDA) 📊
Latent Dirichlet Allocation (LDA) models the corpus as a mixture of topics, where .each topic is a distribution over words
Let $D$ be the corpus (set of documents/posts). We seek to find latent topics $T .where $K=5$ in this project ,$}t_1, t_2, \dots, t_K{ =
:$The model assumes the following generative process for each document $d
			$ Choose a distribution over topics, $\theta_d$, from a Dirichlet prior	 .1 						$$alpha$: $$\theta_d \sim \text}Dirichlet{(\alpha)\ 				$For each word $w$ in the document $d$: a. Choose a topic $z	 .2 		$ corresponding to that word, based on the document's topic distribution $theta_d$: $$z \sim \text}Multinomial{(\theta_d)$$ b. Choose the word $w\ 			$ from the topic's word distribution $\phi_z$, drawn from a Dirichlet prior beta$: $$\phi_z \sim \text}Dirichlet{(\beta)$$ $$w \sim \text}Multinomial{\ 							$$(phi_z\)
The goal of the training process is to infer the word distributions $\phi_z$ (the topics) that best explain the observed word sequence in the corpus, given the .topic proportions $\theta_d$ for each document
To select the optimal number of topics ($K$), the Normalized :Coherence Score Pointwise Mutual Information (NPMI) coherence score is often maximized. A high coherence score indicates that the words defining a topic are semantically .related
Sentiment Analysis Methodology
Sentiment is typically calculated across the cleaned text using a lexicon-based ,approach, such as VADER (Valence Aware Dictionary and sEntiment Reasoner) :which is tuned for social media text
The compound score $S_}compound{$ is calculated: $$S_}compound{ = 0.75 times S_}pos{ + 0.25 \times S_}neu{$$ where $S_}pos{$, $S_}neu{$, and\

S_}neg{$ are the normalized proportion of positive, neutral, and negative words$ .in the text, respectively
If $S_}compound{ \ge 0.05$ :Positive	 •
If $S_}compound{ \le -0.05$ :Negative	 •
		.Otherwise :Neutral	 •
These scores are then aggregated by the predicted LDA topic to see which .discussions lean towards positive or negative sentiment
Screenshots (Conceptual Representation) 💻
Due to the nature of this static documentation, the images referenced are .placeholders demonstrating the intended output fidelity
Dashboard Overview
This section of the )
data/dashboard_overview.png
 :Reference(
dashboard shows the overall sentiment distribution (pie chart), the timeline of posts, and perhaps a selector for viewing specific topics. The dark theme and .Persian script rendering are critical here
Topic Visualization Example
This shows a WordCloud )
data/topic3_wordcloud.png
 :Reference(
generated using the most significant terms ($\phi_z$) for Topic 3. Larger words represent higher probability weights within that specific topic distribution. For
 ,
docker
 ,
kubernetes
 example, if Topic 3 is about 'Deployment', words like




.would appear prominently

aws

 and ,

cloud

How to Run Locally 
Follow these steps meticulously to set up the execution environment and launch :the application

.Ensure you have Python 3.8+ installed :Prerequisites
Clone the repository from the source 1⃣ #
git clone https://github.com/shahpari2kht/-social_media_analyzer.git
cd social_media_analyzer
Create and activate a dedicated virtual environment (Recommended) 2⃣ #
python3 -m venv venv
:Activation Commands (choose one based on OS) #
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows CMD/PowerShell #
Install all required dependencies listed in requirements.txt 3⃣ #

pip install -r requirements.txt
e the Streamlit application to launch the dashboard in your browser 4⃣ #



streamlit run app.py
need to )
fetch_more_subreddits.sh
 Note: If data collection scripts )like
be run, they must be executed prior to Step 4, and you must ensure API keys
.are properly configured in the environment )e.g., Reddit credentials(
Key Insights Achieved 
:The implementation delivers significant results across analysis and presentation
Successfully applied LDA to categorize large volumes of :Topic Extraction	 .1
distinct, interpretable discussion topics 5 unstructured text data into
.relevant to the tech sector
 Provided accessible visualizations through :Visual Interpretation	 .2
mapping high-probability topic keywords directly to the visual , WordClouds
.representation
,Integrated sentiment scores with topic clusters :Sentiment Correlation	 .3
allowing users to immediately see which areas of discussion (e.g., job
.hunting vs. model performance) carry positive or negative connotations
-dark Developed a modern, responsive, and accessible :User Interface	 .4
that correctly handles the complexities of themed Streamlit dashboard

ensuring readability for all target , non-Latin scripts (Persian/Farsi) rendering .users
License 🏷️
MIT License Copyright (c) 2025 Shahpar
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the ,Software without restriction, including without limitation the rights to use, copy ,modify, merge, publish, distribute, sublicense, and/or sell copies of the Software and to permit persons to whom the Software is furnished to do so, subject to the :following conditions
The above copyright notice and this permission notice shall be included in all .copies or substantial portions of the Software
( تحلیل شبکههای اجتماعی )نسخه فارسی
This section serves as a localized documentation summary for Persian-speaking .users, mirroring the functionality described above
هوش مصنوعی، یادگیری ماشین، و با موضوعات مرتبط باReddit این پروژه به تحلیل دادههای(، و سپس در قالبLDA)  میپردازد. دادهها جمعآوری، پاکسازی، مدلسازی موضوعیعلم داده )با حالت تیره و پشتیبانی از فونت فارسی( نمایش داده میشوند.Streamlit داشبورد
ساختار و اهداف اصلی
هدف اصلی، تبدیل دادههای متنی خام به بینشهای ساختاریافته است. این کار با استفاده ازمدلسازی موضوعی برای شناسایی مکالمات اصلی و تحلیل احساسات برای درک لحن عمومیانجام میشود.
مراحل اجرا )خالصه(
 با استفاده از اسکریپتهای اختصاصی.Reddit  → استخراج پستها از .1

 → حذف نویز، استاپوردها و نرمالسازی متون برای آمادهسازی مدل.پیشپردازش متون	 .2
 تاپیک مهم و مجزا از بدنه متون.۵  → استخراج(LDA) مدلسازی موضوعی	 .3
 برای هر تاپیک جهت نمایش کلمات کلیدی غالب.WordCloud  → ساختبصریسازی	 .4
 → مشاهدٔه نتایج با فونت فارسی و تم تیره. Streamlit داشبورد تعاملی	 .5
نمونه خروجیها
 این رابط کاربری تعاملی، خالصهای از تحلیل احساسات کلی و تفکیکنمای کلی داشبورد:
موضوعی را ارائه میدهد. 
Placeholder
 نمونهای از بصریسازی کلمات مرتبط با یکی از تاپیکهای استخراج شده. :۳ ابر کلمات تاپیک
Placeholder
 توسعه یافته با تمرکز بر تحلیل زبان طبیعی، مصورسازی داده و طراحی

داشبوردهای دادهمحور با پوشش کامل پشتیبانی از زبان فارسی در محیط
