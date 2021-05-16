# Text Variables
Note = '(This resume was entirely generated in Python. Please, scan the QR code in order to get the full sourcecode)'
Name = 'LUIS SÁNCHEZ GRISOLÍA'
Title = 'Data analyst & Business Administration'
Header = 'As a financial analyst, I was able to develop crucial analytical skills and attention to detail. Numbers are my\npassion, but I also like people; that is why I love contributing to the success of a team and I am always willing to\ncommunicate my point of view. I am pursuing a career in which I hope to develop further as a data analyst and\nhelp the company create value.'
WorkHeader = 'WORK EXPERIENCE'
WorkOneTitle = 'Business Financial Analyst'
WorkOneCompany = 'MERCEDES BENZ SPAIN   |   Jan 2018 - Feb 2020'
WorkOneDesc = '∘ Analyze tendencies, deviations and profitability reporting findings and assisting\n  the company in decision-making\n∘ Partnership with Sales and Operations department for, through sales analytics,\n  monitor new business quality and performance \n∘ Prepare forecast and monthly monitoring of the business plan of the company\n  for the incoming year. Deviation lower than 3% in 2020\n∘ Project controlling : set-up, monitoring and follow-up. A total of 4 projects\n  were successfully controlled'
WorkTwoTitle = 'Junior Operations Manager'
WorkTwoCompany = 'VOLKSWAGEN FINANCAL SERVICES   |   Jan 2017 - Jan 2018'
WorkTwoDesc = '∘ Legal entity customer solvency analysis and first operating decree. More than\n  200 operations studied of which approximately 85% were final approved\n∘ Analyze all retail credit applications submitted to Volkswagen Financial\n  Services by dealers\n∘ Negotiate and calculate the conditions of the operations with the sales teams of\n  the dealerships when necessary'
WorkThreeTitle = 'Internship - Finance and Accounting'
WorkThreeCompany = 'ROBERT BOSCH SPAIN   |   Jun 2016 - Sep 2016'
WorkThreeDesc = '∘ Credit line management of new customers based on their annual accounts;\n  74 successful customers and 15 rejected reports\n∘ Accounting of collections and payments'
WorkFourTitle = 'Internship - Sales'
WorkFourCompany = 'UNICASH   |   Jun 2015 - Sep 2015'
WorkFourDesc = '∘ Sales team support in 10 commercial routes\n∘ First contact with potential customers in the different routes'
EduHeader = 'EDUCATION'
EduOneTitle = 'Data Analytics bootcamp'
EduOneUni = 'Ironhack (Madrid)'
EduOneTime = 'Feb 2020 - Aug 2020'
EduOneDesc = 'Data analytics bootcamp is an intensive education program designed to equip students\nwith the skills they need, combining programming and mathematics, to perform robust\nanalysis of large amounts of data that answer real-world problems' 
EduTwoTitle = 'Business Administration Degree'
EduTwoUni = 'Universidad San Pablo CEU (Madrid)'
EduTwoTime = '2013 - 2017'
EduThreeTitle = 'Economics - Exchange program in Taiwan'
EduThreeUni = 'Tunghai University (Taiwan)'
EduThreeTime = '2016 - 2017'
EduFourTitle = 'Civil Engineering'
EduFourUni = 'Universidad Politécnica de Madrid'
EduFourTime = '2010 - 2013'
ProfileHeader = 'PROFILE'
Profile = '⌂ Madrid, Spain\n☎ +34 667750435\n✉  lsgrisolia@gmail.com\nin  linkedin.com/in/luissanchezgrisolia\nGitHub:github.com/luissanchezgrisolia'
TechHeader = 'TECHNOLOGIES'
TechDesc = 'SQL                     ••••◦\nPython                 •••◦◦\nPandas                 ••••◦\nNumPy                •••◦◦\nMongoDB           •••◦◦\nTableau               ••◦◦◦\nMicrosoft Excel  •••••\nGitHub                •••◦◦'
LangHeader = 'LANGUAGES'
LangDesc = 'Spanish - Native\nEnglish - Advanced'
CertHeader = 'CERTIFICATIONS'
CertOneDesc = 'Postgraduate Certification in\nBusiness Administration'
CertOneUni = 'Universidad Autónoma de Madrid\n2019'
CertTwoDesc = 'Economics Course'
CertTwoUni = 'University of Toronto (Canada)\n2009'
CertThreeDesc = 'Advanced Certificate in English'
CertThreeUni = 'Cambridge University\n2015'
ActHeader = 'OTHER ACTIVITIES'
ActOneTime = '2011 - 2013'
ActOneDesc = 'In charge of the organization\n“cultural activities volunteering” at\nthe “CMU Jaime del Amo”'
ActTwoTime = '2014 - 2016'
ActTwoDesc = 'Member of the Finance Club of\nthe Universidad San Pablo CEU'
ActThreeTime = '2009 - Present'
ActThreeDesc = 'Auto-investing in stock exchange\nsince 2009 with a 9% profit'
ActFourTime = '2016'
ActFourDesc = 'Winning team of the Taiwanese university\ncontest "Development of the best product"'


# Setting style for bar graphs
import matplotlib.pyplot as plt
%matplotlib inline


# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(11, 13))

# Decorative Lines

plt.axhline(y=.96, xmin=0, xmax=.8, color='#64B5F6', linewidth=1)                   #After name hor line
plt.axvline(x=.02, ymin=.325, ymax=0.80, color='#CFD8DC', alpha=0.8, linewidth=1)  #Time line work
plt.axhline(y=.835, xmin=0.0, xmax=0.225, color='#B3E5FC', linewidth=12)           #Workexp. square 
plt.axhline(y=0.805, xmin=0.018, xmax=0.02, color='#CFD8DC', linewidth=5)          #Work line square 1
plt.axhline(y=0.63, xmin=0.018, xmax=0.02, color='#CFD8DC', linewidth=5)           #Work line square 2
plt.axhline(y=0.485, xmin=0.018, xmax=0.02, color='#CFD8DC', linewidth=5)          #Work line square 3
plt.axhline(y=0.385, xmin=0.018, xmax=0.02, color='#CFD8DC', linewidth=5)          #Work line square 4
plt.axhline(y=.295, xmin=0.0, xmax=0.136, color='#B3E5FC', linewidth=12)           #Education square
plt.axhline(y=.835, xmin=0.755, xmax=0.842, color='#B3E5FC', linewidth=12)         #Profile square
plt.axhline(y=.77, xmin=0.758, xmax=0.7581, color='#2196F3', linewidth=10)         #LinkedIn square
plt.axhline(y=.72, xmin=0.755, xmax=0.922, color='#B3E5FC', linewidth=12)          #Tech square
plt.axhline(y=.555, xmin=0.755, xmax=0.882, color='#B3E5FC', linewidth=12)         #Lang square
plt.axhline(y=.475, xmin=0.755, xmax=0.934, color='#B3E5FC', linewidth=12)         #Certf square
plt.axhline(y=.245, xmin=0.755, xmax=0.957, color='#B3E5FC', linewidth=12)         #Act square


# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text

plt.annotate(Name, (0,1), weight='bold', fontsize=22)
plt.annotate(Title, (0,.97), weight='regular', fontsize=16)
plt.annotate(Note, (0,.945), weight='regular', fontsize=9, alpha=.6)
plt.annotate(Header, (0,.87), weight='regular', fontsize=11)
plt.annotate(WorkHeader, (.007,.83), weight='bold', fontsize=11)
plt.annotate(WorkOneTitle, (.04,.80), weight='bold', fontsize=11)
plt.annotate(WorkOneCompany, (.04,.78), weight='regular', fontsize=10)
plt.annotate(WorkOneDesc, (.04,.655), weight='regular', fontsize=10)
plt.annotate(WorkTwoTitle, (.04,.625), weight='bold', fontsize=11)
plt.annotate(WorkTwoCompany, (.04,.605), weight='regular', fontsize=10)
plt.annotate(WorkTwoDesc, (.04,.51), weight='regular', fontsize=10)
plt.annotate(WorkThreeTitle, (.04,.48), weight='bold', fontsize=11)
plt.annotate(WorkThreeCompany, (.04,.46), weight='regular', fontsize=10)
plt.annotate(WorkThreeDesc, (.04,.41), weight='regular', fontsize=10)
plt.annotate(WorkFourTitle, (.04,.38), weight='bold', fontsize=11)
plt.annotate(WorkFourCompany, (.04,.36), weight='regular', fontsize=10)
plt.annotate(WorkFourDesc, (.04,.325), weight='regular', fontsize=10)
plt.annotate(EduHeader, (.007,.29), weight='bold', fontsize=11)
plt.annotate(EduOneTitle, (0,.26), weight='bold', fontsize=11)
plt.annotate(EduOneUni, (0,.243), weight='regular', fontsize=10)
plt.annotate(EduOneTime, (0,.225), weight='regular', fontsize=10)
plt.annotate(EduOneDesc, (0,.18), weight='regular', fontsize=10)
plt.annotate(EduTwoTitle, (0,.155), weight='bold', fontsize=11)
plt.annotate(EduTwoUni, (0,.138), weight='regular', fontsize=10)
plt.annotate(EduTwoTime, (0,.122), weight='regular', fontsize=10)
plt.annotate(EduThreeTitle, (0,.095), weight='bold', fontsize=11)
plt.annotate(EduThreeUni, (0,.078), weight='regular', fontsize=10)
plt.annotate(EduThreeTime, (0,.062), weight='regular', fontsize=10)
plt.annotate(EduFourTitle, (0,.035), weight='bold', fontsize=11)
plt.annotate(EduFourUni, (0,.018), weight='regular', fontsize=10)
plt.annotate(EduFourTime, (0,.002), weight='regular', fontsize=10)
plt.annotate(ProfileHeader, (.75,.83), weight='bold', fontsize=11)
plt.annotate(Profile, (.75,.751), weight='regular', fontsize=10)
plt.annotate(TechHeader, (.75,.715), weight='bold', fontsize=11)
plt.annotate(TechDesc, (.75,.59), weight='regular', fontsize=10)
plt.annotate(LangHeader, (.75,.55), weight='bold', fontsize=11)
plt.annotate(LangDesc, (.75,.51), weight='regular', fontsize=10)
plt.annotate(CertHeader, (.75,.47), weight='bold', fontsize=11)
plt.annotate(CertOneDesc, (.75,.43), weight='bold', fontsize=10)
plt.annotate(CertOneUni, (.75,.40), weight='regular', fontsize=10)
plt.annotate(CertTwoDesc, (.75,.37), weight='bold', fontsize=10)
plt.annotate(CertTwoUni, (.75,.34), weight='regular', fontsize=10)
plt.annotate(CertThreeDesc, (.75,.31), weight='bold', fontsize=10)
plt.annotate(CertThreeUni, (.75,.28), weight='regular', fontsize=10)
plt.annotate(ActHeader, (.75,.24), weight='bold', fontsize=11)
plt.annotate(ActOneTime, (.75,.21), weight='regular', fontsize=10,alpha=.7)
plt.annotate(ActOneDesc, (.75,.165), weight='regular', fontsize=10)
plt.annotate(ActTwoTime, (.75,.14), weight='regular', fontsize=10,alpha=.7)
plt.annotate(ActTwoDesc, (.75,.11), weight='regular', fontsize=10)
plt.annotate(ActThreeTime, (.75,.085), weight='regular', fontsize=10,alpha=.7)
plt.annotate(ActThreeDesc, (.75,.055), weight='regular', fontsize=10)
plt.annotate(ActFourTime, (.75,.03), weight='regular', fontsize=10,alpha=.7)
plt.annotate(ActFourDesc, (.75,.0), weight='regular', fontsize=10)


#add qr code
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
arr_code = mpimg.imread('qr_cv.png')
imagebox = OffsetImage(arr_code, zoom=0.25)
ab = AnnotationBbox(imagebox, (0.92, .96))
ax.add_artist(ab)

#plt.savefig('resumeexample.png', dpi=300, bbox_inches='tight')
plt.savefig('CV_Luis_Sanchez.pdf') 
