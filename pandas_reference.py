# Thanks to StackOverflow for their 2024 survey data

import pandas as pd

# use the pd.read_csv function to get started and create your dataframe. You can use index_col parameter to index the data based on one of the columns instead of the default 0index
df = pd.read_csv('data/survey_results_public.csv', index_col="ResponseId")

schema_df = pd.read_csv('data/survey_results_schema.csv', index_col="qname")

# The dataframe .shape attribute will return the number of rows, columns contained int he dataframe
df.shape
# (89184, 83)

# Set how many rows and columns to view on print. You can print a dataframe by calling it
pd.set_option('display.max_columns', 84)
pd.set_option('display.max_rows', 5)
df

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 1	I agree	None of these	18-24 years old	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Other	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	2.850000e+05	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 89183	I agree	I am a developer by profession	Under 18 years old	Employed, part-time;Student, part-time	Hybrid (some remote, some in-person)	Hobby;School or academic work	Secondary school (e.g. American high school, G...	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	Udemy	3	NaN	System administrator	NaN	NaN	Investigate	Ask developers I know/work with;Visit develope...	Switzerland	NaN	NaN	Bash/Shell (all shells);C#;HTML/CSS;Java;JavaS...	Bash/Shell (all shells);HTML/CSS;JavaScript;Po...	MariaDB;Microsoft SQL Server;MongoDB;MySQL;Red...	Cassandra;Cosmos DB;Dynamodb;MariaDB;Microsoft...	Amazon Web Services (AWS);Cloudflare;Google Cl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Next.js;Node.js;React;WordPress	Angular;AngularJS;Express;Next.js;Node.js;Reac...	CUDA;NumPy;Torch/PyTorch	CUDA;Flutter;NumPy;TensorFlow;Torch/PyTorch	Docker;Kubernetes;npm;Podman;Vite	Ansible;APT;Docker;Kubernetes;npm;Pip;Podman;T...	Eclipse;IntelliJ IDEA;Nano;Notepad++;PyCharm;V...	Jupyter Notebook/JupyterLab;Notepad++;Visual S...	Arch;Debian;iOS;iPadOS;MacOS;Ubuntu;Windows;Wi...	BSD;Red Hat;Solaris;Ubuntu;Windows	Confluence;Jira;Trello	Azure Devops;Confluence;Jira	Cisco Webex Teams;Discord;Microsoft Teams;Sign...	Discord;Microsoft Teams;Skype	Bing AI;ChatGPT;WolframAlpha	Bing AI;ChatGPT;Google Bard AI	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	No	NaN	Yes, somewhat	Define Parameters more detailed. I believe in ...	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Somewhat distrust	Learning about a codebase;Project planning;Wri...	Learning about a codebase;Writing code;Debuggi...	Committing and reviewing code	NaN	Debugging and getting help;Deployment and moni...	NaN	NaN	Learning about a codebase;Writing code	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Neither easy nor difficult	NaN
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN

# df.loc[rows, columns] returns a subset of the data, using primarily str based references
df.loc[0:12, 'RemoteWork':'LearnCode']

# 	RemoteWork	CodingActivities	EdLevel	LearnCode
# ResponseId				
# 1	NaN	NaN	NaN	NaN
# 2	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...
# ...	...	...	...	...
# 11	Remote	Hobby	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Friend or family member...
# 12	Remote	Hobby	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Online Courses or Certification;Other online r...
# 12 rows × 4 columns

# df.iloc[rows, columns] returns a subset of the data, but using numbered indexes only
df.iloc[0:12, 4:7]

# 	RemoteWork	CodingActivities	EdLevel
# ResponseId			
# 1	NaN	NaN	NaN
# 2	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)
# ...	...	...	...
# 11	Remote	Hobby	Bachelor’s degree (B.A., B.S., B.Eng., etc.)
# 12	Remote	Hobby	Bachelor’s degree (B.A., B.S., B.Eng., etc.)
# 12 rows × 3 columns

# df.info() method returns the schema of a dataset
df.info()

# <class 'pandas.core.frame.DataFrame'>
# Index: 89184 entries, 1 to 89184
# Data columns (total 83 columns):

#  #   Column                               Non-Null Count  Dtype  
# ---  ------                               --------------  -----  
#  0   Q120                                 89184 non-null  object 
#  1   MainBranch                           89184 non-null  object 
#  2   Age                                  89184 non-null  object 
#  3   Employment                           87898 non-null  object 
#  4   RemoteWork                           73810 non-null  object 
# ...
#  77  TimeAnswering                        42629 non-null  object 
#  78  ProfessionalTech                     41783 non-null  object 
#  79  Industry                             36774 non-null  object 
#  80  SurveyLength                         86485 non-null  object 
#  81  SurveyEase                           86554 non-null  object 
#  82  ConvertedCompYearly                  48019 non-null  float64
# dtypes: float64(3), object(80)
# memory usage: 59.2+ MB

schema_df.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 78 entries, 0 to 77
# Data columns (total 6 columns):
#  #   Column      Non-Null Count  Dtype 
# ---  ------      --------------  ----- 
#  0   qid         78 non-null     object
#  1   qname       78 non-null     object
#  2   question    78 non-null     object
#  3   force_resp  67 non-null     object
#  4   type        78 non-null     object
#  5   selector    78 non-null     object
# dtypes: object(6)
# memory usage: 3.8+ KB

schema_df

# 	qid	question	force_resp	type	selector
# qname					
# S0	QID16	<div><span style="font-size:19px;"><strong>Hel...	False	DB	TB
# MetaInfo	QID12	Browser Meta Info	False	Meta	Browser
# ...	...	...	...	...	...
# Frequency_2	QID290	Interacting with people outside of your immedi...	NaN	MC	MAVR
# Frequency_3	QID290	Encountering knowledge silos (where one indivi...	NaN	MC	MAVR
# 78 rows × 5 columns


# We can use the second dataframe, which contains the full text versions of the questions asked on this survey, as a reference point. As we're using the question's shorthand / common key shared by both datasets as an index (e.g. 'force_resp'), we can search using it
schema_df.loc['Frequency_2', 'question']

# 'Interacting with people outside of your immediate team?'


# Create a filter - returns true or false
df['RemoteWork'] == 'Remote'

# ResponseId
# 1        False
# 2         True
#          ...  
# 89183    False
# 89184    False
# Name: RemoteWork, Length: 89184, dtype: bool


# If we want to just return the values, we can apply it as a filter
filt = (df['RemoteWork'] == 'Remote')
df[filt]

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Other	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	285000.0	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# 5	I agree	I am a developer by profession	25-34 years old	Employed, full-time;Independent contractor, fr...	Remote	Hobby;Contribute to open-source projects;Profe...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Online Courses or Certi...	Formal documentation provided by the owner of ...	Other;Codecademy;edX	6	4	Developer, full-stack	20 to 99 employees	I have some influence	Investigate	Start a free trial;Ask developers I know/work ...	Philippines	PHP\tPhilippine peso	1320000.0	HTML/CSS;JavaScript;TypeScript	HTML/CSS;JavaScript;Python;Rust;TypeScript	BigQuery;Elasticsearch;MongoDB;PostgreSQL	Elasticsearch;MongoDB;PostgreSQL;Redis;Supabase	Amazon Web Services (AWS);Firebase;Heroku;Netl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Gatsby;NestJS;Next.js;Node.js;React	Express;NestJS;Next.js;Node.js;React;Remix;Vue.js	NaN	NaN	Docker;npm;Webpack;Yarn	Docker;npm;Yarn	Vim;Visual Studio Code	Vim;Visual Studio Code	Other (Please Specify):	Other (Please Specify):	Confluence;Jira;Notion	Confluence;Jira;Notion	Discord;Google Meet;Slack;Zoom	Discord;Google Meet;Slack;Zoom	ChatGPT	ChatGPT	NaN	NaN	Stack Overflow;Stack Exchange	A few times per week	No	NaN	Neutral	Using AI to suggest better answer to my questi...	Yes	Very favorable	Increase productivity;Greater efficiency;Speed...	Somewhat trust	Project planning;Testing code;Committing and r...	Learning about a codebase;Writing code;Documen...	NaN	NaN	NaN	NaN	NaN	NaN	Yes	Individual contributor	6.0	Agree	Strongly agree	Agree	Agree	Neither agree nor disagree	Agree	Strongly agree	Agree	1-2 times a week	1-2 times a week	3-5 times a week	60-120 minutes a day	30-60 minutes a day	Microservices;Automated testing;Observability ...	Other	Appropriate in length	Neither easy nor difficult	23456.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 89179	I agree	I am a developer by profession	45-54 years old	Employed, full-time	Remote	Hobby	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Online Courses or Certification;On the job tra...	Formal documentation provided by the owner of ...	edX;Udemy;Pluralsight;Udacity	25	22	Developer, full-stack	10,000 or more employees	I have little or no influence	NaN	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	212021.0	JavaScript;TypeScript	Go;JavaScript;Python;TypeScript	Dynamodb	Dynamodb	Amazon Web Services (AWS)	Amazon Web Services (AWS)	Express;Node.js;Spring Boot	Node.js	Apache Kafka	NaN	Docker;Homebrew;Yarn	Docker;Godot;Homebrew;Vite;Yarn	IntelliJ IDEA;Nano;Visual Studio Code	Visual Studio Code	MacOS	MacOS;Ubuntu	Confluence;Jira;Markdown File;Stack Overflow f...	GitHub Discussions;Stack Overflow for Teams	Microsoft Teams;Slack;Zoom	Slack	NaN	NaN	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	Daily or almost daily	Yes	A few times per month or weekly	No, not really	Improve question writing	No, but I plan to soon	Favorable	NaN	Somewhat distrust	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Yes	Individual contributor	22.0	Strongly agree	Neither agree nor disagree	Disagree	Neither agree nor disagree	Agree	Agree	Strongly agree	Neither agree nor disagree	1-2 times a week	1-2 times a week	1-2 times a week	15-30 minutes a day	60-120 minutes a day	DevOps function;Microservices;Automated testin...	Insurance	Appropriate in length	Easy	NaN
# 89180	I agree	I am a developer by profession	25-34 years old	Employed, full-time;Independent contractor, fr...	Remote	Hobby;Bootstrapping a business;Freelance/contr...	Associate degree (A.A., A.S., etc.)	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	Udemy	20	5	Developer, front-end	100 to 499 employees	I have some influence	Investigate	NaN	Brazil	BRL\tBrazilian real	200000.0	HTML/CSS;Java;JavaScript;SQL;TypeScript	Bash/Shell (all shells);C;Go;HTML/CSS;JavaScri...	MongoDB;MySQL;PostgreSQL;SQLite	PostgreSQL;SQLite	Digital Ocean;Firebase;Google Cloud;Heroku;Vercel	Amazon Web Services (AWS);Heroku;Netlify;Vercel	Angular;AngularJS;Express;jQuery;Node.js;Nuxt....	Express;Node.js;Nuxt.js;Svelte;Vue.js	Flutter	NaN	Chocolatey;CMake;Docker;Maven (build tool);npm...	Docker;npm;Pip;Vite;Yarn	Android Studio;Atom;Eclipse;IntelliJ IDEA;Netb...	Visual Studio Code	Android;Windows	Android;Ubuntu;Windows	Asana;Confluence;Jira;Markdown File;Miro;Notio...	Markdown File;Miro;Wikis	Discord;Google Meet;Jitsi;Microsoft Teams;Slac...	Discord;Google Meet;Jitsi;Microsoft Teams;Tele...	ChatGPT	ChatGPT	Whispr AI	Whispr AI	Stack Overflow;Stack Exchange	Multiple times per day	Yes	I have never participated in Q&A on Stack Over...	Neutral	NaN	Yes	Very favorable	Increase productivity;Greater efficiency;Speed...	Somewhat trust	Learning about a codebase;Project planning;Wri...	Writing code;Documenting code;Debugging and ge...	Deployment and monitoring	NaN	NaN	NaN	NaN	Writing code;Documenting code;Debugging and ge...	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Too long	Neither easy nor difficult	NaN
# 30566 rows × 83 columns

# Filter columns, and return Remote Work and Years of Coding cols
df.loc[filt, ['RemoteWork', 'YearsCode']]

# ResponseId	RemoteWork	YearsCode
# 2	Remote	18
# 5	Remote	6
# ...	...	...
# 89179	Remote	25
# 89180	Remote	20
# 30566 rows × 2 columns

# We can use AND (&) and OR (|) operators
filt2 = (df['RemoteWork'] == 'Remote') & (df['YearsCode'] == '18')
df[filt2]

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Other	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	285000.0	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# 155	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Remote	Contribute to open-source projects;Professiona...	Master’s degree (M.A., M.S., M.Eng., MBA, etc.)	Books / Physical media;Other online resources ...	Formal documentation provided by the owner of ...	NaN	18	12	Developer Experience	10,000 or more employees	I have little or no influence	NaN	Ask developers I know/work with;Visit develope...	Portugal	EUR European Euro	65000.0	C++;Go;JavaScript;Python;TypeScript	Go;Kotlin;Python;Rust;Swift;TypeScript;Zig	MongoDB;MySQL	MySQL	Oracle Cloud Infrastructure (OCI)	Cloudflare;Fly.io;Netlify;Oracle Cloud Infrast...	Node.js;React	Deno;Next.js;Node.js;React;Remix;Svelte	Electron	React Native	CMake;Docker;Homebrew;LLVM's Clang;Make;Ninja;...	CMake;Docker;Homebrew;Kubernetes;LLVM's Clang;...	IntelliJ IDEA;Vim;Visual Studio Code	IntelliJ IDEA;Vim;Visual Studio Code	iOS;MacOS	Debian;Fedora;iOS;MacOS;Other Linux-based;Red ...	Confluence;Jira;Markdown File	Confluence;GitHub Discussions;Linear;Markdown ...	Slack;Telegram;Whatsapp;Zoom	Discord;Slack;Telegram;Whatsapp;Zoom	NaN	NaN	NaN	NaN	Stack Overflow	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I would prefer to not deal with AI tools altog...	No, and I don't plan to	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Yes	Individual contributor	12.0	Strongly agree	Agree	Disagree	Neither agree nor disagree	Agree	Neither agree nor disagree	Agree	Neither agree nor disagree	3-5 times a week	3-5 times a week	1-2 times a week	30-60 minutes a day	15-30 minutes a day	DevOps function;Automated testing;Developer po...	Information Services, IT, Software Development...	Appropriate in length	Easy	69608.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 88883	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects	Master’s degree (M.A., M.S., M.Eng., MBA, etc.)	Books / Physical media;On the job training;Oth...	Formal documentation provided by the owner of ...	NaN	18	15	Developer, front-end	1,000 to 4,999 employees	I have little or no influence	NaN	NaN	United States of America	USD\tUnited States dollar	230000.0	Bash/Shell (all shells);Groovy;HTML/CSS;JavaSc...	HTML/CSS	NaN	NaN	Amazon Web Services (AWS);Netlify	Netlify	Elm	Elm	NaN	NaN	npm;Vite	pnpm;Vite	Emacs;Helix;Visual Studio	Helix	Arch	MacOS	Jira	NaN	Discord;Slack;Zoom	Discord;Zoom	NaN	NaN	NaN	NaN	Stack Overflow;Stack Exchange	Less than once per month or monthly	No	NaN	No, not at all	NaN	No, and I don't plan to	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Neither easy nor difficult	230000.0
# 89112	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Remote	Hobby;Freelance/contract work	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Other online ...	Formal documentation provided by the owner of ...	NaN	18	12	Developer, back-end	10,000 or more employees	I have little or no influence	NaN	Start a free trial;Read ratings or reviews on ...	Turkey	TRY\tTurkish lira	750000.0	Bash/Shell (all shells);Dart;Java;Kotlin	Kotlin	Dynamodb	Dynamodb	Amazon Web Services (AWS);Firebase;Google Cloud	Amazon Web Services (AWS);Firebase;Google Cloud	Spring Boot	NaN	Flutter;Ktor	Ktor	Docker;Gradle;Homebrew;Kubernetes;Maven (build...	Gradle;Homebrew	IntelliJ IDEA;Sublime Text	Fleet;IntelliJ IDEA;Jupyter Notebook/JupyterLa...	MacOS	MacOS	Confluence;Jira;Notion	Confluence;Jira;Notion	Slack;Zoom	Slack;Zoom	ChatGPT;Google Bard AI	ChatGPT	GitHub Copilot;Tabnine	AWS CodeWhisperer;Codeium;GitHub Copilot	Stack Overflow;Stack Exchange;Collectives on S...	Daily or almost daily	Yes	Less than once per month or monthly	Yes, somewhat	SO should definitely use AI for various things...	Yes	Very favorable	Increase productivity;Greater efficiency;Speed...	Somewhat trust	Learning about a codebase;Project planning;Wri...	Writing code;Documenting code;Debugging and ge...	NaN	Writing code;Documenting code;Debugging and ge...	NaN	NaN	NaN	NaN	Yes	Individual contributor	12.0	Strongly agree	Disagree	Agree	Neither agree nor disagree	Neither agree nor disagree	Agree	Strongly agree	Disagree	1-2 times a week	1-2 times a week	Never	15-30 minutes a day	60-120 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	35255.0
# 756 rows × 83 columns


# We can use the NOT (~) operator, which will return the opposite
filt3 = (df['RemoteWork'] == 'Remote') | (df['YearsCode'] == '18')
df[~filt3]


# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 1	I agree	None of these	18-24 years old	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 3	I agree	I am a developer by profession	45-54 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;On the job tr...	Formal documentation provided by the owner of ...	NaN	27	23	Developer, back-end	5,000 to 9,999 employees	I have some influence	Given a list	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	2.500000e+05	Bash/Shell (all shells);Go	Haskell;OCaml;Rust	NaN	NaN	Amazon Web Services (AWS);Google Cloud;OpenSta...	NaN	NaN	NaN	NaN	NaN	Cargo;Docker;Kubernetes;Make;Nix	Cargo;Kubernetes;Nix	Emacs;Helix	Emacs;Helix	MacOS;Other Linux-based	MacOS;Other Linux-based	Markdown File;Stack Overflow for Teams	Markdown File	Microsoft Teams;Slack;Zoom	Slack;Zoom	NaN	NaN	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	Yes	Less than once per month or monthly	Neutral	NaN	No, and I don't plan to	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Yes	Individual contributor	23.0	Strongly agree	Neither agree nor disagree	Agree	Agree	Agree	Agree	Agree	Agree	6-10 times a week	6-10 times a week	3-5 times a week	30-60 minutes a day	30-60 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	250000.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 89183	I agree	I am a developer by profession	Under 18 years old	Employed, part-time;Student, part-time	Hybrid (some remote, some in-person)	Hobby;School or academic work	Secondary school (e.g. American high school, G...	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	Udemy	3	NaN	System administrator	NaN	NaN	Investigate	Ask developers I know/work with;Visit develope...	Switzerland	NaN	NaN	Bash/Shell (all shells);C#;HTML/CSS;Java;JavaS...	Bash/Shell (all shells);HTML/CSS;JavaScript;Po...	MariaDB;Microsoft SQL Server;MongoDB;MySQL;Red...	Cassandra;Cosmos DB;Dynamodb;MariaDB;Microsoft...	Amazon Web Services (AWS);Cloudflare;Google Cl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Next.js;Node.js;React;WordPress	Angular;AngularJS;Express;Next.js;Node.js;Reac...	CUDA;NumPy;Torch/PyTorch	CUDA;Flutter;NumPy;TensorFlow;Torch/PyTorch	Docker;Kubernetes;npm;Podman;Vite	Ansible;APT;Docker;Kubernetes;npm;Pip;Podman;T...	Eclipse;IntelliJ IDEA;Nano;Notepad++;PyCharm;V...	Jupyter Notebook/JupyterLab;Notepad++;Visual S...	Arch;Debian;iOS;iPadOS;MacOS;Ubuntu;Windows;Wi...	BSD;Red Hat;Solaris;Ubuntu;Windows	Confluence;Jira;Trello	Azure Devops;Confluence;Jira	Cisco Webex Teams;Discord;Microsoft Teams;Sign...	Discord;Microsoft Teams;Skype	Bing AI;ChatGPT;WolframAlpha	Bing AI;ChatGPT;Google Bard AI	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	No	NaN	Yes, somewhat	Define Parameters more detailed. I believe in ...	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Somewhat distrust	Learning about a codebase;Project planning;Wri...	Learning about a codebase;Writing code;Debuggi...	Committing and reviewing code	NaN	Debugging and getting help;Deployment and moni...	NaN	NaN	Learning about a codebase;Writing code	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Neither easy nor difficult	NaN
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN
# 57684 rows × 83 columns


# ConvertedCompYearly vs. DevType
high_salary = (df['ConvertedCompYearly'] > 70000)
df.loc[high_salary, ['Country', 'DevType', 'LanguageHaveWorkedWith', 'LanguageWantToWorkWith', 'ConvertedCompYearly']]


# 	Country	DevType	LanguageHaveWorkedWith	LanguageWantToWorkWith	ConvertedCompYearly
# ResponseId					
# 2	United States of America	Senior Executive (C-Suite, VP, etc.)	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	285000.0
# 3	United States of America	Developer, back-end	Bash/Shell (all shells);Go	Haskell;OCaml;Rust	250000.0
# ...	...	...	...	...	...
# 89157	United States of America	Engineering manager	Bash/Shell (all shells);C;C++;JavaScript;Julia	Julia;Zig	195000.0
# 89158	Canada	Developer, mobile	Java;Kotlin	NaN	319711.0
# 25719 rows × 5 columns


# Another common filtering function is to use .isin()
countries = ['United States of America', 'Canada']
filt = df['Country'].isin(countries)
df.loc[filt, 'Country']

# ResponseId
# 2        United States of America
# 3        United States of America
#                    ...           
# 89176    United States of America
# 89179    United States of America
# Name: Country, Length: 22154, dtype: object


# We can also use str functions in conjuntion with Pandas filters. na=False means ignore NaN answers.
filt = df['LanguageHaveWorkedWith'].str.contains('Python', na=False)
df.loc[filt, 'LanguageHaveWorkedWith']

# ResponseId
# 2                               HTML/CSS;JavaScript;Python
# 8        Go;HTML/CSS;JavaScript;Python;Rust;SQL;TypeScript
#                                ...                        
# 89182    Assembly;Bash/Shell (all shells);C;C#;Python;R...
# 89183    Bash/Shell (all shells);C#;HTML/CSS;Java;JavaS...
# Name: LanguageHaveWorkedWith, Length: 43158, dtype: object


# Remember, filters just apply a mask to the data set of True/False values - the data is displayed if True, and not if False
filt

# ResponseId
# 1        False
# 2         True
#          ...  
# 89183     True
# 89184    False
# Name: LanguageHaveWorkedWith, Length: 89184, dtype: bool


# df.columns attribute will show you which columns are contained in a dataset
df.columns

# Index(['Q120', 'MainBranch', 'Age', 'Employment', 'RemoteWork',
#        'CodingActivities', 'EdLevel', 'LearnCode', 'LearnCodeOnline',
#        'LearnCodeCoursesCert', 'YearsCode', 'YearsCodePro', 'DevType',
#        'OrgSize', 'PurchaseInfluence', 'TechList', 'BuyNewTool', 'Country',
#        'Currency', 'CompTotal', 'LanguageHaveWorkedWith',
#        'LanguageWantToWorkWith', 'DatabaseHaveWorkedWith',
#        'DatabaseWantToWorkWith', 'PlatformHaveWorkedWith',
#        'PlatformWantToWorkWith', 'WebframeHaveWorkedWith',
#        'WebframeWantToWorkWith', 'MiscTechHaveWorkedWith',
#        'MiscTechWantToWorkWith', 'ToolsTechHaveWorkedWith',
#        'ToolsTechWantToWorkWith', 'NEWCollabToolsHaveWorkedWith',
#        'NEWCollabToolsWantToWorkWith', 'OpSysPersonal use',
#        'OpSysProfessional use', 'OfficeStackAsyncHaveWorkedWith',
#        'OfficeStackAsyncWantToWorkWith', 'OfficeStackSyncHaveWorkedWith',
#        'OfficeStackSyncWantToWorkWith', 'AISearchHaveWorkedWith',
#        'AISearchWantToWorkWith', 'AIDevHaveWorkedWith', 'AIDevWantToWorkWith',
#        'NEWSOSites', 'SOVisitFreq', 'SOAccount', 'SOPartFreq', 'SOComm',
#        'SOAI', 'AISelect', 'AISent', 'AIAcc', 'AIBen',
#        'AIToolInterested in Using', 'AIToolCurrently Using',
#        'AIToolNot interested in Using', 'AINextVery different',
#        'AINextNeither different nor similar', 'AINextSomewhat similar',
#        'AINextVery similar', 'AINextSomewhat different', 'TBranch', 'ICorPM',
#        'WorkExp', 'Knowledge_1', 'Knowledge_2', 'Knowledge_3', 'Knowledge_4',
#        'Knowledge_5', 'Knowledge_6', 'Knowledge_7', 'Knowledge_8',
#        'Frequency_1', 'Frequency_2', 'Frequency_3', 'TimeSearching',
#        'TimeAnswering', 'ProfessionalTech', 'Industry', 'SurveyLength',
#        'SurveyEase', 'ConvertedCompYearly'],
#       dtype='object')


# You can overwrite the column names by using setting the column attribute, e.g. convert to uppercase
df.columns = [x.upper() for x in df.columns]


# We can also only rename certain columns by using .rename() method, and pass in a dictionary of items to rename
df.rename(columns = {'MainBranch': 'MyChangedColumnName'})

# 	Q120	MyChangedColumnName	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 1	I agree	None of these	18-24 years old	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Other	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	2.850000e+05	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 89183	I agree	I am a developer by profession	Under 18 years old	Employed, part-time;Student, part-time	Hybrid (some remote, some in-person)	Hobby;School or academic work	Secondary school (e.g. American high school, G...	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	Udemy	3	NaN	System administrator	NaN	NaN	Investigate	Ask developers I know/work with;Visit develope...	Switzerland	NaN	NaN	Bash/Shell (all shells);C#;HTML/CSS;Java;JavaS...	Bash/Shell (all shells);HTML/CSS;JavaScript;Po...	MariaDB;Microsoft SQL Server;MongoDB;MySQL;Red...	Cassandra;Cosmos DB;Dynamodb;MariaDB;Microsoft...	Amazon Web Services (AWS);Cloudflare;Google Cl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Next.js;Node.js;React;WordPress	Angular;AngularJS;Express;Next.js;Node.js;Reac...	CUDA;NumPy;Torch/PyTorch	CUDA;Flutter;NumPy;TensorFlow;Torch/PyTorch	Docker;Kubernetes;npm;Podman;Vite	Ansible;APT;Docker;Kubernetes;npm;Pip;Podman;T...	Eclipse;IntelliJ IDEA;Nano;Notepad++;PyCharm;V...	Jupyter Notebook/JupyterLab;Notepad++;Visual S...	Arch;Debian;iOS;iPadOS;MacOS;Ubuntu;Windows;Wi...	BSD;Red Hat;Solaris;Ubuntu;Windows	Confluence;Jira;Trello	Azure Devops;Confluence;Jira	Cisco Webex Teams;Discord;Microsoft Teams;Sign...	Discord;Microsoft Teams;Skype	Bing AI;ChatGPT;WolframAlpha	Bing AI;ChatGPT;Google Bard AI	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	No	NaN	Yes, somewhat	Define Parameters more detailed. I believe in ...	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Somewhat distrust	Learning about a codebase;Project planning;Wri...	Learning about a codebase;Writing code;Debuggi...	Committing and reviewing code	NaN	Debugging and getting help;Deployment and moni...	NaN	NaN	Learning about a codebase;Writing code	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Neither easy nor difficult	NaN
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN
# 89184 rows × 83 columns

# Note unless you specify inPlace = True, the change will not be permanent - here it's reverted
df

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 1	I agree	None of these	18-24 years old	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Other	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	2.850000e+05	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 89183	I agree	I am a developer by profession	Under 18 years old	Employed, part-time;Student, part-time	Hybrid (some remote, some in-person)	Hobby;School or academic work	Secondary school (e.g. American high school, G...	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	Udemy	3	NaN	System administrator	NaN	NaN	Investigate	Ask developers I know/work with;Visit develope...	Switzerland	NaN	NaN	Bash/Shell (all shells);C#;HTML/CSS;Java;JavaS...	Bash/Shell (all shells);HTML/CSS;JavaScript;Po...	MariaDB;Microsoft SQL Server;MongoDB;MySQL;Red...	Cassandra;Cosmos DB;Dynamodb;MariaDB;Microsoft...	Amazon Web Services (AWS);Cloudflare;Google Cl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Next.js;Node.js;React;WordPress	Angular;AngularJS;Express;Next.js;Node.js;Reac...	CUDA;NumPy;Torch/PyTorch	CUDA;Flutter;NumPy;TensorFlow;Torch/PyTorch	Docker;Kubernetes;npm;Podman;Vite	Ansible;APT;Docker;Kubernetes;npm;Pip;Podman;T...	Eclipse;IntelliJ IDEA;Nano;Notepad++;PyCharm;V...	Jupyter Notebook/JupyterLab;Notepad++;Visual S...	Arch;Debian;iOS;iPadOS;MacOS;Ubuntu;Windows;Wi...	BSD;Red Hat;Solaris;Ubuntu;Windows	Confluence;Jira;Trello	Azure Devops;Confluence;Jira	Cisco Webex Teams;Discord;Microsoft Teams;Sign...	Discord;Microsoft Teams;Skype	Bing AI;ChatGPT;WolframAlpha	Bing AI;ChatGPT;Google Bard AI	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	No	NaN	Yes, somewhat	Define Parameters more detailed. I believe in ...	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Somewhat distrust	Learning about a codebase;Project planning;Wri...	Learning about a codebase;Writing code;Debuggi...	Committing and reviewing code	NaN	Debugging and getting help;Deployment and moni...	NaN	NaN	Learning about a codebase;Writing code	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Neither easy nor difficult	NaN
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN
# 89184 rows × 83 columns


# You can change the value of a field by setting it equal to something
df.loc[1,'Employment'] = 'My field value change'
df.loc[1, 'Q120':'Employment']

# Q120                        I agree
# MainBranch            None of these
# Age                 18-24 years old
# Employment    My field value change
# Name: 1, dtype: object


# We can also use a filter to change values according to a set of criteria
# E.g. If LearnCodeCoursesCert == Other, change value to 'Unknown'

filt = (df['LearnCodeCoursesCert'] == 'Other')
df.loc[filt, 'LearnCodeCoursesCert'] = "Unknown"
df

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 1	I agree	None of these	18-24 years old	My field value change	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Unknown	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	2.850000e+05	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN
# 1	NaN	NaN	NaN	My field value change	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 89185 rows × 83 columns



# You can return a case insensitive list by using
df['Employment'].str.lower()
# Or you could make this a permanent change by assignment
df['Employment'] = df['Employment'].str.lower()

# ResponseId
# 1        False
# 2        False
#          ...  
# 89184    False
# 1        False
# Name: Employment, Length: 89185, dtype: bool



# You can use apply() to apply a function and transform a field's data - here we are turning the list into a string, and then returning a len()
df['LanguageHaveWorkedWith'].apply(str).apply(len)

# .apply() will pass the data into the function called, i.e. data.apply(len) will become len(data)
# Note: We are not using parentheses here because we do not want to execute the function yet, we just want to pass in the function name

# ResponseId
# 1         3
# 2        26
#          ..
# 89184    31
# 1         3
# Name: LanguageHaveWorkedWith, Length: 89185, dtype: int64


# We can also create custom functions to transform our data
def get_str_len(data):
    return len(str(data))

df['LanguageHaveWorkedWith'].apply(get_str_len)

# ResponseId
# 1         3
# 2        26
#          ..
# 89184    31
# 1         3
# Name: LanguageHaveWorkedWith, Length: 89185, dtype: int64

# Another way of doing this is to pass in a lambda filter instead of a function name, which allows for simple processing
df['Country'].apply(lambda x: str(x).lower())

# ResponseId
# 1                                 nan
# 2            united states of america
#                      ...             
# 89184    iran, islamic republic of...
# 1                                 nan
# Name: Country, Length: 89185, dtype: object

# If you use apply() to a dataframe, it will return the length of each series (results per column)
df.apply(len)

# Q120                   89185
# MainBranch             89185
#                        ...  
# SurveyEase             89185
# ConvertedCompYearly    89185
# Length: 83, dtype: int64


# By default the axis is 'rows', but you can change it to columns to change the direction in which the data is read
df.apply(len, axis='columns')

# ResponseId
# 1        83
# 2        83
#          ..
# 89184    83
# 1        83
# Length: 89185, dtype: int64



# You can use map() to apply methods to 2D data (rows and cols). Here we're fetching str lengths for each cell
df[0:5].map(str).map(len)

# Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 1	7	13	15	21	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3	3
# 2	7	30	15	19	6	133	44	234	335	7	2	1	36	16	32	11	122	24	24	8	26	72	8	35	40	21	26	36	27	45	43	55	22	22	58	47	59	39	91	25	7	16	14	14	29	21	3	31	15	156	3	11	22	17	65	42	3	3	3	3	3	3	3	14	4	14	5	14	5	5	5	5	14	16	16	5	19	19	67	67	21	4	8
# 3	7	30	15	19	36	73	44	144	213	3	2	2	19	24	21	12	98	24	24	8	26	18	3	3	61	3	3	3	3	3	32	20	11	11	23	23	38	13	26	10	3	3	3	3	121	31	3	35	7	3	23	3	3	3	3	3	3	3	3	3	3	3	3	22	4	14	26	5	5	5	5	5	5	17	17	16	19	19	219	67	21	4	8
# 4	7	30	15	19	36	5	44	125	170	3	2	1	20	20	21	11	98	24	24	8	67	59	16	16	17	17	44	28	3	3	30	17	45	26	16	16	4	4	46	30	3	3	3	3	29	20	3	35	14	39	23	3	3	3	3	3	3	3	3	3	3	3	3	22	3	14	17	14	14	5	26	5	5	16	16	16	19	19	82	3	21	4	8
# 5	7	30	15	72	


# You can also pass in a dictionary to .map() to substitute values in the data when returning them
df['RemoteWork'][0:4].map({'Remote': 'At Home'})

# Note: Values that are NOT 'Remote' will be replaced with NaN using .map()

# ResponseId
# 1        NaN
# 2    At Home
# 3        NaN
# 4        NaN
# Name: RemoteWork, dtype: object


# You can use .replace() instead of .map() to avoid values being replaced with NaN
df['RemoteWork'][0:4].replace({'Remote': 'At Home'})

# ResponseId
# 1                                     NaN
# 2                                 At Home
# 3    Hybrid (some remote, some in-person)
# 4    Hybrid (some remote, some in-person)
# Name: RemoteWork, dtype: object



# We can pass a columns argument into rename() to rename columns
df[0:5].rename(columns={"Q120": "Consent"})

# Note: This will not be permanent, unless you add an 'inPlace = True' argument at the end of the function

# 	Consent	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 1	I agree	None of these	18-24 years old	My field value change	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Unknown	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	285000.0	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# 3	I agree	I am a developer by profession	45-54 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;On the job tr...	Formal documentation provided by the owner of ...	NaN	27	23	Developer, back-end	5,000 to 9,999 employees	I have some influence	Given a list	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	250000.0	Bash/Shell (all shells);Go	Haskell;OCaml;Rust	NaN	NaN	Amazon Web Services (AWS);Google Cloud;OpenSta...	NaN	NaN	NaN	NaN	NaN	Cargo;Docker;Kubernetes;Make;Nix	Cargo;Kubernetes;Nix	Emacs;Helix	Emacs;Helix	MacOS;Other Linux-based	MacOS;Other Linux-based	Markdown File;Stack Overflow for Teams	Markdown File	Microsoft Teams;Slack;Zoom	Slack;Zoom	NaN	NaN	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	Yes	Less than once per month or monthly	Neutral	NaN	No, and I don't plan to	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Yes	Individual contributor	23.0	Strongly agree	Neither agree nor disagree	Agree	Agree	Agree	Agree	Agree	Agree	6-10 times a week	6-10 times a week	3-5 times a week	30-60 minutes a day	30-60 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	250000.0
# 4	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Friend or family member;Other online...	Formal documentation provided by the owner of ...	NaN	12	7	Developer, front-end	100 to 499 employees	I have some influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	156000.0	Bash/Shell (all shells);HTML/CSS;JavaScript;PH...	Bash/Shell (all shells);HTML/CSS;JavaScript;Ru...	PostgreSQL;Redis	PostgreSQL;Redis	Cloudflare;Heroku	Cloudflare;Heroku	Node.js;React;Ruby on Rails;Vue.js;WordPress	Node.js;Ruby on Rails;Vue.js	NaN	NaN	Homebrew;npm;Vite;Webpack;Yarn	Homebrew;npm;Vite	IntelliJ IDEA;Vim;Visual Studio Code;WebStorm	IntelliJ IDEA;Vim;WebStorm	iOS;iPadOS;MacOS	iOS;iPadOS;MacOS	Jira	Jira	Discord;Google Meet;Microsoft Teams;Slack;Zoom	Discord;Google Meet;Slack;Zoom	NaN	NaN	NaN	NaN	Stack Overflow;Stack Exchange	A few times per week	Yes	Less than once per month or monthly	No, not really	I'm wearing of Stack Overflow using AI.	No, and I don't plan to	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Yes	Individual contributor	7.0	Strongly agree	Strongly disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Agree	Agree	1-2 times a week	10+ times a week	1-2 times a week	15-30 minutes a day	30-60 minutes a day	Automated testing;Continuous integration (CI) ...	NaN	Appropriate in length	Easy	156000.0
# 5	I agree	I am a developer by profession	25-34 years old	Employed, full-time;Independent contractor, fr...	Remote



# A useful way of using Map() is to interpret the results of the data as more useful data types
df['SOAccount'][0:5].map({'Yes': True, 'No': False})

# ResponseId
# 1      NaN
# 2     True
# 3     True
# 4     True
# 5    False
# Name: SOAccount, dtype: object


df['PlatformHaveWorkedWith'][0:5]

# ResponseId
# 1                                                  NaN
# 2             Amazon Web Services (AWS);Netlify;Vercel
# 3    Amazon Web Services (AWS);Google Cloud;OpenSta...
# 4                                    Cloudflare;Heroku
# 5    Amazon Web Services (AWS);Firebase;Heroku;Netl...
# Name: PlatformHaveWorkedWith, dtype: object


# How can we easily see if a survey respondent can use Amazon Web Services (AWS)?
# Let's first get a mask for whether the user's listed skills contact AWS
filt = (df['PlatformHaveWorkedWith'][0:5].str.contains('Amazon Web Services'))
filt

# ResponseId
# 1      NaN
# 2     True
# 3     True
# 4    False
# 5     True
# Name: PlatformHaveWorkedWith, dtype: object



# Then let's add a new column to the data to help
df['Uses AWS'] = filt.map({True: 'Yes', False: 'No', 'NaN': 'No'})
df[0:12]

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly	Uses AWS
# ResponseId																																																																																				
# 1	I agree	None of these	18-24 years old	My field value change	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Unknown	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	285000.0	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0	Yes
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 11	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Friend or family member...	Formal documentation provided by the owner of ...	NaN	14	3	Developer, desktop or enterprise applications	100 to 499 employees	I have little or no influence	NaN	Start a free trial;Visit developer communities...	United States of America	USD\tUnited States dollar	NaN	C#;C++;HTML/CSS;JavaScript;Python	Python	MongoDB	Firebase Realtime Database	Amazon Web Services (AWS)	NaN	ASP.NET CORE;Flask;Vue.js	NaN	.NET (5+) ;.NET Framework (1.0 - 4.8)	NaN	MSBuild;NuGet;Pip;Visual Studio Solution	NaN	Jupyter Notebook/JupyterLab;Visual Studio Code	Jupyter Notebook/JupyterLab;Visual Studio Code	Windows	Windows	NaN	NaN	Discord;Microsoft Teams;Slack	NaN	Bing AI;ChatGPT;Google Bard AI;WolframAlpha	NaN	NaN	NaN	Stack Overflow;Stack Exchange	A few times per week	No	NaN	No, not really	I think AI might be helpful sort of as a searc...	No, and I don't plan to	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Yes	Individual contributor	3.0	Disagree	Strongly agree	Neither agree nor disagree	Disagree	Disagree	Agree	Agree	Disagree	1-2 times a week	1-2 times a week	6-10 times a week	30-60 minutes a day	60-120 minutes a day	Automated testing;Continuous integration (CI) ...	Other	Appropriate in length	Neither easy nor difficult	NaN	NaN
# 12	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	NaN	10	9	Developer, full-stack	100 to 499 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	Australia	AUD\tAustralian dollar	118000.0	C#;HTML/CSS;JavaScript;Kotlin;PowerShell;Pytho...	C#;HTML/CSS;JavaScript;SQL;TypeScript	Cosmos DB;Microsoft SQL Server;MySQL;Redis	Microsoft SQL Server;PostgreSQL	Digital Ocean;Microsoft Azure;Netlify	Microsoft Azure;Netlify	ASP.NET CORE;Node.js;Vue.js	Nuxt.js;Qwik;Solid.js;Svelte;Vue.js	.NET (5+)	.NET (5+) ;Flutter	Docker;Gradle;npm;NuGet;Vite;Webpack	npm;pnpm;Vite	Android Studio;Notepad++;Visual Studio Code	Notepad++;Visual Studio Code	MacOS	Windows	Azure Devops	NaN	Microsoft Teams;Zoom	Microsoft Teams	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Impro...	Somewhat trust	NaN	Writing code;Testing code	NaN	NaN	NaN	NaN	NaN	NaN	No	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Easy	78003.0	NaN
# 12 rows × 84 columns



# Let's try and drop the column now
df.drop(columns=['Uses AWS'])

# This is only temporary - we can make it permanent by adding inPlace = True as an argument
df.drop(columns=['Uses AWS'], inplace = True)

df

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 1	I agree	None of these	18-24 years old	My field value change	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Unknown	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	2.850000e+05	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN
# 1	NaN	NaN	NaN	My field value change	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 89185 rows × 83 columns


# You could also do something like this on another dataset
df['Full name'] = df['First name'] + ' ' + df['Last name']

# You could later split these into multiple columns by doing something like this
df[['first', 'last']] = df['Full name'].str.split(' ', expand=True)


# Adding a row of data:
# Let's use the .loc() method to get the last row reference + 1 to add a row of data
len(df['Q120']) # last row reference = 89185

df.loc[ len(df['Q120']) + 1 ] = {'Q120': 'I disagree'}
df.tail()

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 89183	I agree	I am a developer by profession	Under 18 years old	Employed, part-time;Student, part-time	Hybrid (some remote, some in-person)	Hobby;School or academic work	Secondary school (e.g. American high school, G...	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	Udemy	3	NaN	System administrator	NaN	NaN	Investigate	Ask developers I know/work with;Visit develope...	Switzerland	NaN	NaN	Bash/Shell (all shells);C#;HTML/CSS;Java;JavaS...	Bash/Shell (all shells);HTML/CSS;JavaScript;Po...	MariaDB;Microsoft SQL Server;MongoDB;MySQL;Red...	Cassandra;Cosmos DB;Dynamodb;MariaDB;Microsoft...	Amazon Web Services (AWS);Cloudflare;Google Cl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Next.js;Node.js;React;WordPress	Angular;AngularJS;Express;Next.js;Node.js;Reac...	CUDA;NumPy;Torch/PyTorch	CUDA;Flutter;NumPy;TensorFlow;Torch/PyTorch	Docker;Kubernetes;npm;Podman;Vite	Ansible;APT;Docker;Kubernetes;npm;Pip;Podman;T...	Eclipse;IntelliJ IDEA;Nano;Notepad++;PyCharm;V...	Jupyter Notebook/JupyterLab;Notepad++;Visual S...	Arch;Debian;iOS;iPadOS;MacOS;Ubuntu;Windows;Wi...	BSD;Red Hat;Solaris;Ubuntu;Windows	Confluence;Jira;Trello	Azure Devops;Confluence;Jira	Cisco Webex Teams;Discord;Microsoft Teams;Sign...	Discord;Microsoft Teams;Skype	Bing AI;ChatGPT;WolframAlpha	Bing AI;ChatGPT;Google Bard AI	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	No	NaN	Yes, somewhat	Define Parameters more detailed. I believe in ...	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Somewhat distrust	Learning about a codebase;Project planning;Wri...	Learning about a codebase;Writing code;Debuggi...	Committing and reviewing code	NaN	Debugging and getting help;Deployment and moni...	NaN	NaN	Learning about a codebase;Writing code	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Neither easy nor difficult	NaN
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN
# 1	NaN	NaN	NaN	My field value change	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 89186	I disagree	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 89187	I disagree	NaN



# You can drop the rows again like this. Use inplace=True to make the deletion permanent
df.drop(index = len(df['Q120']), inplace=True)
df.tail()

# Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 89182	I agree	I code primarily as a hobby	Prefer not to say	I prefer not to say	NaN	NaN	Something else	Books / Physical media;Hackathons (virtual or ...	NaN	Codecademy;Coursera	10	NaN	NaN	NaN	NaN	NaN	NaN	Israel	NaN	NaN	Assembly;Bash/Shell (all shells);C;C#;Python;R...	Python;Rust	SQLite	NaN	Amazon Web Services (AWS)	Amazon Web Services (AWS);Microsoft Azure	NaN	NaN	NumPy;Pandas;TensorFlow	NumPy;Pandas;Torch/PyTorch	Cargo	Cargo;Docker;Kubernetes;Terraform	Jupyter Notebook/JupyterLab;Neovim;Visual Stud...	Jupyter Notebook/JupyterLab;Neovim;Visual Stud...	Windows	NaN	NaN	NaN	NaN	NaN	ChatGPT;Quora Poe	ChatGPT;Quora Poe	NaN	NaN	Stack Overflow;Stack Exchange	NaN	NaN	NaN	NaN	NaN	No, but I plan to soon	Very favorable	NaN	Highly trust	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Too long	Neither easy nor difficult	NaN
# 89183	I agree	I am a developer by profession	Under 18 years old	Employed, part-time;Student, part-time	Hybrid (some remote, some in-person)	Hobby;School or academic work	Secondary school (e.g. American high school, G...	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	Udemy	3	NaN	System administrator	NaN	NaN	Investigate	Ask developers I know/work with;Visit develope...	Switzerland	NaN	NaN	Bash/Shell (all shells);C#;HTML/CSS;Java;JavaS...	Bash/Shell (all shells);HTML/CSS;JavaScript;Po...	MariaDB;Microsoft SQL Server;MongoDB;MySQL;Red...	Cassandra;Cosmos DB;Dynamodb;MariaDB;Microsoft...	Amazon Web Services (AWS);Cloudflare;Google Cl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Next.js;Node.js;React;WordPress	Angular;AngularJS;Express;Next.js;Node.js;Reac...	CUDA;NumPy;Torch/PyTorch	CUDA;Flutter;NumPy;TensorFlow;Torch/PyTorch	Docker;Kubernetes;npm;Podman;Vite	Ansible;APT;Docker;Kubernetes;npm;Pip;Podman;T...	Eclipse;IntelliJ IDEA;Nano;Notepad++;PyCharm;V...	Jupyter Notebook/JupyterLab;Notepad++;Visual S...	Arch;Debian;iOS;iPadOS;MacOS;Ubuntu;Windows;Wi...	BSD;Red Hat;Solaris;Ubuntu;Windows	Confluence;Jira;Trello	Azure Devops;Confluence;Jira	Cisco Webex Teams;Discord;Microsoft Teams;Sign...	Discord;Microsoft Teams;Skype	Bing AI;ChatGPT;WolframAlpha	Bing AI;ChatGPT;Google Bard AI	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	No	NaN	Yes, somewhat	Define Parameters more detailed. I believe in ...	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Somewhat distrust	Learning about a codebase;Project planning;Wri...	Learning about a codebase;Writing code;Debuggi...	Committing and reviewing code	NaN	Debugging and getting help;Deployment and moni...	NaN	NaN	Learning about a codebase;Writing code	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Neither easy nor difficult	NaN
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN
# 1	NaN	NaN	NaN	My field value change	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN
# 89186	I disagree	NaN	NaN	NaN



# You can also conditionally drop rows using a condition like this
filt = (df['LearnCodeCoursesCert'].isnull())

df.drop(index=df[filt].index)

# 	Q120	MainBranch	Age	Employment	RemoteWork	CodingActivities	EdLevel	LearnCode	LearnCodeOnline	LearnCodeCoursesCert	YearsCode	YearsCodePro	DevType	OrgSize	PurchaseInfluence	TechList	BuyNewTool	Country	Currency	CompTotal	LanguageHaveWorkedWith	LanguageWantToWorkWith	DatabaseHaveWorkedWith	DatabaseWantToWorkWith	PlatformHaveWorkedWith	PlatformWantToWorkWith	WebframeHaveWorkedWith	WebframeWantToWorkWith	MiscTechHaveWorkedWith	MiscTechWantToWorkWith	ToolsTechHaveWorkedWith	ToolsTechWantToWorkWith	NEWCollabToolsHaveWorkedWith	NEWCollabToolsWantToWorkWith	OpSysPersonal use	OpSysProfessional use	OfficeStackAsyncHaveWorkedWith	OfficeStackAsyncWantToWorkWith	OfficeStackSyncHaveWorkedWith	OfficeStackSyncWantToWorkWith	AISearchHaveWorkedWith	AISearchWantToWorkWith	AIDevHaveWorkedWith	AIDevWantToWorkWith	NEWSOSites	SOVisitFreq	SOAccount	SOPartFreq	SOComm	SOAI	AISelect	AISent	AIAcc	AIBen	AIToolInterested in Using	AIToolCurrently Using	AIToolNot interested in Using	AINextVery different	AINextNeither different nor similar	AINextSomewhat similar	AINextVery similar	AINextSomewhat different	TBranch	ICorPM	WorkExp	Knowledge_1	Knowledge_2	Knowledge_3	Knowledge_4	Knowledge_5	Knowledge_6	Knowledge_7	Knowledge_8	Frequency_1	Frequency_2	Frequency_3	TimeSearching	TimeAnswering	ProfessionalTech	Industry	SurveyLength	SurveyEase	ConvertedCompYearly
# ResponseId																																																																																			
# 2	I agree	I am a developer by profession	25-34 years old	Employed, full-time	Remote	Hobby;Contribute to open-source projects;Boots...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Colleague;Friend or fam...	Formal documentation provided by the owner of ...	Unknown	18	9	Senior Executive (C-Suite, VP, etc.)	2 to 9 employees	I have a great deal of influence	Investigate	Start a free trial;Ask developers I know/work ...	United States of America	USD\tUnited States dollar	2.850000e+05	HTML/CSS;JavaScript;Python	Bash/Shell (all shells);C#;Dart;Elixir;GDScrip...	Supabase	Firebase Realtime Database;Supabase	Amazon Web Services (AWS);Netlify;Vercel	Fly.io;Netlify;Render	Next.js;React;Remix;Vue.js	Deno;Elm;Nuxt.js;React;Svelte;Vue.js	Electron;React Native;Tauri	Capacitor;Electron;Tauri;Uno Platform;Xamarin	Docker;Kubernetes;npm;Pip;Vite;Webpack;Yarn	Godot;npm;pnpm;Unity 3D;Unreal Engine;Vite;Web...	Vim;Visual Studio Code	Vim;Visual Studio Code	iOS;iPadOS;MacOS;Windows;Windows Subsystem for...	MacOS;Windows;Windows Subsystem for Linux (WSL)	Asana;Basecamp;GitHub Discussions;Jira;Linear;...	GitHub Discussions;Linear;Notion;Trello	Cisco Webex Teams;Discord;Google Chat;Google M...	Discord;Signal;Slack;Zoom	ChatGPT	ChatGPT;Neeva AI	GitHub Copilot	GitHub Copilot	Stack Overflow;Stack Exchange	Daily or almost daily	Yes	A few times per month or weekly	Yes, definitely	I don't think it's super necessary, but I thin...	Yes	Indifferent	Other (please explain)	Somewhat distrust	Learning about a codebase;Writing code;Debuggi...	Writing code;Committing and reviewing code	NaN	NaN	NaN	NaN	NaN	NaN	Yes	People manager	10.0	Strongly agree	Agree	Strongly agree	Agree	Agree	Agree	Agree	Strongly agree	1-2 times a week	10+ times a week	Never	15-30 minutes a day	15-30 minutes a day	DevOps function;Microservices;Automated testin...	Information Services, IT, Software Development...	Appropriate in length	Easy	285000.0
# 5	I agree	I am a developer by profession	25-34 years old	Employed, full-time;Independent contractor, fr...	Remote	Hobby;Contribute to open-source projects;Profe...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Books / Physical media;Online Courses or Certi...	Formal documentation provided by the owner of ...	Other;Codecademy;edX	6	4	Developer, full-stack	20 to 99 employees	I have some influence	Investigate	Start a free trial;Ask developers I know/work ...	Philippines	PHP\tPhilippine peso	1.320000e+06	HTML/CSS;JavaScript;TypeScript	HTML/CSS;JavaScript;Python;Rust;TypeScript	BigQuery;Elasticsearch;MongoDB;PostgreSQL	Elasticsearch;MongoDB;PostgreSQL;Redis;Supabase	Amazon Web Services (AWS);Firebase;Heroku;Netl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Gatsby;NestJS;Next.js;Node.js;React	Express;NestJS;Next.js;Node.js;React;Remix;Vue.js	NaN	NaN	Docker;npm;Webpack;Yarn	Docker;npm;Yarn	Vim;Visual Studio Code	Vim;Visual Studio Code	Other (Please Specify):	Other (Please Specify):	Confluence;Jira;Notion	Confluence;Jira;Notion	Discord;Google Meet;Slack;Zoom	Discord;Google Meet;Slack;Zoom	ChatGPT	ChatGPT	NaN	NaN	Stack Overflow;Stack Exchange	A few times per week	No	NaN	Neutral	Using AI to suggest better answer to my questi...	Yes	Very favorable	Increase productivity;Greater efficiency;Speed...	Somewhat trust	Project planning;Testing code;Committing and r...	Learning about a codebase;Writing code;Documen...	NaN	NaN	NaN	NaN	NaN	NaN	Yes	Individual contributor	6.0	Agree	Strongly agree	Agree	Agree	Neither agree nor disagree	Agree	Strongly agree	Agree	1-2 times a week	1-2 times a week	3-5 times a week	60-120 minutes a day	30-60 minutes a day	Microservices;Automated testing;Observability ...	Other	Appropriate in length	Neither easy nor difficult	23456.0
# ...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
# 89183	I agree	I am a developer by profession	Under 18 years old	Employed, part-time;Student, part-time	Hybrid (some remote, some in-person)	Hobby;School or academic work	Secondary school (e.g. American high school, G...	Online Courses or Certification;Other online r...	Formal documentation provided by the owner of ...	Udemy	3	NaN	System administrator	NaN	NaN	Investigate	Ask developers I know/work with;Visit develope...	Switzerland	NaN	NaN	Bash/Shell (all shells);C#;HTML/CSS;Java;JavaS...	Bash/Shell (all shells);HTML/CSS;JavaScript;Po...	MariaDB;Microsoft SQL Server;MongoDB;MySQL;Red...	Cassandra;Cosmos DB;Dynamodb;MariaDB;Microsoft...	Amazon Web Services (AWS);Cloudflare;Google Cl...	Amazon Web Services (AWS);Cloudflare;Digital O...	Express;Next.js;Node.js;React;WordPress	Angular;AngularJS;Express;Next.js;Node.js;Reac...	CUDA;NumPy;Torch/PyTorch	CUDA;Flutter;NumPy;TensorFlow;Torch/PyTorch	Docker;Kubernetes;npm;Podman;Vite	Ansible;APT;Docker;Kubernetes;npm;Pip;Podman;T...	Eclipse;IntelliJ IDEA;Nano;Notepad++;PyCharm;V...	Jupyter Notebook/JupyterLab;Notepad++;Visual S...	Arch;Debian;iOS;iPadOS;MacOS;Ubuntu;Windows;Wi...	BSD;Red Hat;Solaris;Ubuntu;Windows	Confluence;Jira;Trello	Azure Devops;Confluence;Jira	Cisco Webex Teams;Discord;Microsoft Teams;Sign...	Discord;Microsoft Teams;Skype	Bing AI;ChatGPT;WolframAlpha	Bing AI;ChatGPT;Google Bard AI	NaN	NaN	Stack Overflow;Stack Exchange;Stack Overflow f...	A few times per month or weekly	No	NaN	Yes, somewhat	Define Parameters more detailed. I believe in ...	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Somewhat distrust	Learning about a codebase;Project planning;Wri...	Learning about a codebase;Writing code;Debuggi...	Committing and reviewing code	NaN	Debugging and getting help;Deployment and moni...	NaN	NaN	Learning about a codebase;Writing code	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	Appropriate in length	Neither easy nor difficult	NaN
# 89184	I agree	I am a developer by profession	35-44 years old	Employed, full-time	Hybrid (some remote, some in-person)	Hobby;Professional development or self-paced l...	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	Colleague;Online Courses or Certification;Othe...	Formal documentation provided by the owner of ...	Codecademy;Pluralsight;Coursera	17	12	Developer, full-stack	100 to 499 employees	I have some influence	NaN	Start a free trial;Ask developers I know/work ...	Iran, Islamic Republic of...	IRR\tIranian rial	3.300000e+09	C#;Go;JavaScript;SQL;TypeScript	C#;Go;JavaScript;SQL;TypeScript	Microsoft SQL Server;Redis;SQLite	Microsoft SQL Server;Redis;SQLite	Hetzner	Hetzner;Microsoft Azure	Angular;ASP.NET;ASP.NET CORE;Blazor;Node.js	Angular;ASP.NET;ASP.NET CORE;Blazor;Deno;Node....	.NET (5+) ;.NET Framework (1.0 - 4.8)	.NET (5+) ;Apache Kafka;RabbitMQ;Tauri	Docker;npm;NuGet;pnpm;Vite;Webpack;Yarn	Bun;Docker;npm;NuGet;pnpm;Vite;Yarn	Visual Studio;Visual Studio Code	Visual Studio;Visual Studio Code	Windows	Windows	NaN	NaN	Google Meet;Skype;Telegram;Whatsapp	Google Meet;Skype;Telegram;Whatsapp	ChatGPT	ChatGPT	GitHub Copilot	GitHub Copilot	Stack Overflow	A few times per week	Yes	Less than once per month or monthly	Yes, somewhat	NaN	Yes	Favorable	Increase productivity;Greater efficiency;Speed...	Neither trust nor distrust	Learning about a codebase;Writing code	Learning about a codebase;Writing code	NaN	Learning about a codebase	NaN	NaN	NaN	Writing code	Yes	People manager	14.0	Agree	Neither agree nor disagree	Neither agree nor disagree	Strongly agree	Strongly agree	Agree	Neither agree nor disagree	Neither agree nor disagree	Never	1-2 times a week	1-2 times a week	60-120 minutes a day	30-60 minutes a day	DevOps function;Developer portal or other cent...	Information Services, IT, Software Development...	Appropriate in length	Easy	NaN
# 37076 rows × 83 columns



# ==========================
# More basic functions
# ==========================

# Sorting values
# --------------

# Basic sorting can be done with sort_values
df.sort_values(by="Col Name Here", ascending=False)

# You can also pass in multiple column names as a list - in this case, Last Name will be the primary sort
df.sort_values(by=["Last Name","First Name"], ascending=False)

# You can also pass in multiple values to ascending= - in this case, Last Name would be in descending order, First Name would be in ascending order
df.sort_values(by=["Last Name","First Name"], ascending=[False, True])

# You can make any sorting permanent by adding inplace=True
df.sort_values(by="Col Name Here", ascending=False, inplace=True)

# Or reset the sort by sorting by index again
df.sort_index()

# You can also sort individual column results instead of the whole table
df['Last Name'].sort_values()


# Min and Max values
# ------------------

# You can use .nlargest() method to return the largest values from a column in the dataset
df["ConvertedCompYearly"].nlargest(10)

# This would give the full table info for the largest 10 results in ConvertedCompYearly
df.nlargest(10, "ConvertedCompYearly")

# The .nsmallest() method can be used to find the min values
df["ConvertedCompYearly"].nsmallest(10)


# Mean, Mode and Median
# ----------------------

# Get the Mean value of a specific column's values
df["ConvertedCompYearly"].mean()

# Get the Mode value of a specific column's values
df["ConvertedCompYearly"].mode()

# Get the Median value of a specific column's values
df["ConvertedCompYearly"].median()

# You can also run .median() on the full dataset to get values of all applicable columns
df.median()


# Describe
# ---------

# You can use the .describe() method to get a range of useful information, including count, mean, standard deviation, min, 25% quartile, 50% quartile, 75% quartile and max values of all relevant rows 
df.describe()

# You can run the .describe() method on a single column too
df["ConvertedCompYearly"].describe()


# Counts and Value Counts
# -----------------------

# You can use the .count() method to return how many values exist in that column (i.e. non NaN / missing values)
df["ConvertedCompYearly"].count()

# If you want to see how many respondents answered which answer, you can create a table that summarises this info by running .value_counts()
df["Hobbyist"].value_counts()
## Yes - 20900
## No - 10110
## NaN - 11024


# Group By
# --------
# Note: the Pandas documentation explains that the Group By function includes three steps:
# Split -> Apply Function -> Combine Results

# Part 1 - Split

# .groupby() will create a pandas groupby object, which will group the results into groups that share a country
country_group = df.groupby(["Country"])
# Then running .get_group() will return only the results where the values include United States
country_group.get_group("United States")

# Part 2 - Apply function and get results

# This would be a way to get most popular social media platforms by country - sorted by country as a primary index and social media as the secondary index
country_group['SocialMedia'].value_counts()

# This would show median yearly compensation values per country
country_group['ConvertedCompYearly'].median()
# We can also use .loc() method to find a specific named index (i.e. named country)
country_group['ConvertedCompYearly'].median().loc('Germany')

# We can run more than one function on the data running the .agg() method
country_group['ConvertedCompYearly'].agg(['median', 'mean']).loc['Canada']
## median 1513512.000
## mean 124125.124


