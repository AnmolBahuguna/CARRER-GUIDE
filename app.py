from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os



# Initialize Flask app
app = Flask(__name__, template_folder='FRONTEND')
CORS(app, resources={r"/*": {"origins": "*"}})


# ============= ROUTES FOR HTML PAGES =============
@app.route('/', methods=['GET', 'HEAD'])
def index():
    if request.method == 'HEAD':
        return '', 200
    return render_template('index.html')

@app.route('/animation')
def animation():
    return render_template('animation.html')

@app.route('/ba')
def ba():
    return render_template('ba.html')

@app.route('/bba')
def bba():
    return render_template('bba.html')

@app.route('/bca')
def bca():
    return render_template('bca.html')

@app.route('/bsc')
def bsc():
    return render_template('bsc.html')

@app.route('/btech')
def btech():
    return render_template('btech.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/law')
def law():
    return render_template('law.html')

@app.route('/logic')
def logic():
    return render_template('logic.html')

@app.route('/mbbs')
def mbbs():
    return render_template('mbbs.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# ============= EXPANDED CAREER DATA =============
CAREER_DATA = {
    "software_engineer": {
        "title": "Software Engineer",
        "skills": ["programming", "coding", "python", "java", "algorithms"],
        "description": "Design, develop, and maintain software applications",
        "education": "BTech/BCA in Computer Science",
        "salary": "Rs 5-15 LPA",
    },
    "data_scientist": {
        "title": "Data Scientist",
        "skills": ["statistics", "machine learning", "python", "data analysis"],
        "description": "Analyze complex data to help make decisions",
        "education": "BTech/MSc in Data Science or Computer Science",
        "salary": "Rs 8-20 LPA",
    },
    "doctor": {
        "title": "Medical Doctor",
        "skills": ["biology", "medicine", "patient care", "mbbs"],
        "description": "Diagnose and treat illnesses",
        "education": "MBBS + MD/MS",
        "salary": "Rs 10-50 LPA",
    },
    "lawyer": {
        "title": "Lawyer",
        "skills": ["law", "legal", "constitution", "advocacy"],
        "description": "Provide legal advice and represent clients",
        "education": "LLB/LLM",
        "salary": "Rs 5-30 LPA",
    },
    "business_analyst": {
        "title": "Business Analyst",
        "skills": ["business", "analysis", "bba", "mba", "management"],
        "description": "Analyze business processes and suggest improvements",
        "education": "BBA/MBA",
        "salary": "Rs 6-18 LPA",
    },
    "architect": {
        "title": "Architect",
        "skills": ["design", "creativity", "planning", "construction"],
        "description": "Design buildings and structures",
        "education": "B.Arch",
        "salary": "Rs 4-15 LPA",
    },
    "civil_engineer": {
        "title": "Civil Engineer",
        "skills": ["construction", "infrastructure", "planning"],
        "description": "Design and supervise construction projects",
        "education": "BTech Civil Engineering",
        "salary": "Rs 4-12 LPA",
    },
    "chartered_accountant": {
        "title": "Chartered Accountant",
        "skills": ["accounting", "taxation", "finance", "auditing"],
        "description": "Manage financial records and tax compliance",
        "education": "CA (ICAI)",
        "salary": "Rs 7-25 LPA",
    },
}

# ============= TEST ROUTE =============
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"status": True, "message": "Backend is running!"})

# ============= ENHANCED CHATBOT API =============
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data received"}), 400
            
        message = data.get('message', '').lower()
        
        response_text = ""
        suggestions = []
        
        # GREETINGS
        if any(word in message for word in ['hello', 'hi', 'hey', 'namaste', 'good morning', 'good evening']):
            response_text = "Hello! 👋 I'm your Career Guidance AI. I can help you with:\n\n📚 Courses: BTech, MBBS, BBA, BCA, BSc, BA, B.Arch, Law, BDS, BPharm\n💼 Careers: Engineering, Medical, Business, Law, Design, etc.\n💰 Salary Information\n🎯 Career Suggestions based on interests\n\nWhat would you like to explore?"
            suggestions = ["Tell me about BTech", "Medical courses", "High paying careers", "I need career guidance"]
        
        # BTech/ENGINEERING
        elif any(word in message for word in ['btech', 'engineering', 'b.tech', 'b tech']):
            response_text = "🎓 BTech (Bachelor of Technology) - 4-year Engineering Degree\n\n📌 Popular Branches:\n• Computer Science (CSE) - Software/AI/ML\n• Information Technology (IT) - Software Development\n• Electronics & Communication (ECE) - Electronics/Telecom\n• Mechanical Engineering - Manufacturing/Automotive\n• Civil Engineering - Construction/Infrastructure\n• Electrical Engineering - Power/Electronics\n• Chemical Engineering - Process/Chemical Industries\n\n💼 Career Prospects: Excellent! High demand in IT, core engineering sectors\n💰 Salary: Rs 4-25 LPA (varies by branch & company)\n🏆 Top Colleges: IITs, NITs, BITS Pilani, VIT, DTU\n📝 Entrance: JEE Main, JEE Advanced, State CETs"
            suggestions = ["CSE vs IT difference?", "Best BTech branch?", "JEE preparation tips", "Mechanical Engineering"]
        
        # COMPUTER SCIENCE SPECIFIC
        elif any(word in message for word in ['cse', 'computer science', 'cs branch']):
            response_text = "💻 BTech Computer Science Engineering (CSE)\n\n📚 What You'll Learn:\n• Programming (C, C++, Java, Python)\n• Data Structures & Algorithms\n• Database Management\n• Web Development\n• Machine Learning & AI\n• Computer Networks\n• Operating Systems\n\n💼 Career Options:\n• Software Engineer - Rs 6-20 LPA\n• Data Scientist - Rs 8-25 LPA\n• Full Stack Developer - Rs 5-18 LPA\n• AI/ML Engineer - Rs 8-30 LPA\n• Cybersecurity Expert - Rs 6-20 LPA\n\n🌟 Why CSE?: Highest placements, diverse opportunities, remote work possible"
            suggestions = ["IT vs CSE?", "Programming languages to learn", "Software Engineer career", "AI/ML career"]
        
        # MECHANICAL ENGINEERING
        elif any(word in message for word in ['mechanical', 'mech engineering', 'manufacturing']):
            response_text = "⚙️ BTech Mechanical Engineering\n\n📚 Core Subjects:\n• Thermodynamics\n• Fluid Mechanics\n• Machine Design\n• Manufacturing Processes\n• CAD/CAM\n• Robotics & Automation\n\n💼 Career Paths:\n• Mechanical Engineer - Rs 4-12 LPA\n• Automotive Engineer - Rs 5-15 LPA\n• HVAC Engineer - Rs 4-10 LPA\n• CAD Designer - Rs 3-10 LPA\n• Production Manager - Rs 6-18 LPA\n\n🏭 Industries: Automobile, Manufacturing, Aerospace, Oil & Gas\n🎯 Scope: Core engineering field with traditional & modern opportunities"
            suggestions = ["Automobile industry jobs", "CAD career", "Manufacturing jobs", "Mechanical vs Civil?"]
        
        # CIVIL ENGINEERING
        elif any(word in message for word in ['civil engineering', 'construction', 'infrastructure']):
            response_text = "🏗️ BTech Civil Engineering\n\n📚 Key Areas:\n• Structural Engineering\n• Transportation Engineering\n• Environmental Engineering\n• Geotechnical Engineering\n• Construction Management\n• Surveying & GIS\n\n💼 Career Options:\n• Civil Engineer - Rs 3-10 LPA\n• Structural Engineer - Rs 4-15 LPA\n• Site Engineer - Rs 3-8 LPA\n• Project Manager - Rs 6-20 LPA\n• Urban Planner - Rs 4-12 LPA\n\n🏢 Employers: L&T, Tata Projects, Government PWD, Real Estate companies\n🌍 Scope: Infrastructure boom in India = Good opportunities!"
            suggestions = ["Government jobs in civil?", "Site engineer work", "Structural engineering", "Civil vs Architecture?"]
        
        # ELECTRICAL/ELECTRONICS
        elif any(word in message for word in ['electrical', 'electronics', 'ece', 'eee']):
            response_text = "⚡ Electrical & Electronics Engineering\n\n🔌 ECE (Electronics & Communication):\n• VLSI Design\n• Embedded Systems\n• Signal Processing\n• Communication Systems\n\n💡 EEE (Electrical & Electronics):\n• Power Systems\n• Electrical Machines\n• Control Systems\n• Power Electronics\n\n💼 Careers:\n• Electronics Engineer - Rs 4-15 LPA\n• VLSI Engineer - Rs 5-18 LPA\n• Power Engineer - Rs 4-12 LPA\n• Telecom Engineer - Rs 5-15 LPA\n\n🏭 Industries: Electronics, Power, Telecom, Semiconductors"
            suggestions = ["ECE vs EEE difference?", "VLSI career", "Telecom industry jobs", "Power sector jobs"]
        
        # MBBS/MEDICAL
        elif any(word in message for word in ['mbbs', 'doctor', 'medical', 'medicine']):
            response_text = "🩺 MBBS (Bachelor of Medicine, Bachelor of Surgery)\n\n⏱️ Duration: 5.5 years (4.5 years + 1 year internship)\n\n📚 What You'll Study:\n• Anatomy, Physiology, Biochemistry\n• Pathology, Microbiology, Pharmacology\n• Community Medicine, Forensic Medicine\n• Medicine, Surgery, Pediatrics, Gynecology\n\n👨‍⚕️ Career Path:\n1. Complete MBBS\n2. Do MD/MS (3 years) in specialization\n3. Become Specialist Doctor\n\n💼 Specializations:\n• Cardiologist - Heart specialist\n• Orthopedic - Bone specialist\n• Dermatologist - Skin specialist\n• Pediatrician - Child specialist\n• Surgeon - Perform surgeries\n\n💰 Salary: Rs 10-50 LPA (after specialization)\n📝 Entrance: NEET UG\n🏥 Top Colleges: AIIMS, JIPMER, CMC Vellore, AFMC"
            suggestions = ["NEET preparation", "After MBBS options", "Doctor salary details", "MD specializations"]
        
        # BDS (DENTAL)
        elif any(word in message for word in ['bds', 'dental', 'dentist', 'teeth']):
            response_text = "🦷 BDS (Bachelor of Dental Surgery)\n\n⏱️ Duration: 5 years (4 years + 1 year internship)\n\n📚 Study Areas:\n• Dental Anatomy\n• Oral Pathology\n• Orthodontics (braces)\n• Prosthodontics (artificial teeth)\n• Oral Surgery\n• Periodontology (gums)\n\n💼 Career Options:\n• Dentist (Clinic/Hospital) - Rs 4-15 LPA\n• Orthodontist - Rs 6-20 LPA\n• Dental Surgeon - Rs 5-18 LPA\n• Start Your Own Clinic\n• Teaching in Dental Colleges\n\n📝 Entrance: NEET UG\n💰 Average Salary: Rs 4-15 LPA\n🏥 Practice: Government hospitals, Private clinics, Own practice"
            suggestions = ["BDS vs MBBS?", "Dentist salary", "Own dental clinic", "After BDS options"]
        
        # PHARMACY
        elif any(word in message for word in ['pharmacy', 'bpharm', 'b pharm', 'pharmacist']):
            response_text = "💊 B.Pharm (Bachelor of Pharmacy)\n\n⏱️ Duration: 4 years\n\n📚 What You'll Learn:\n• Pharmaceutical Chemistry\n• Pharmacology (drug effects)\n• Pharmaceutics (drug formulation)\n• Pharmacognosy (medicinal plants)\n• Clinical Pharmacy\n• Drug Regulatory Affairs\n\n💼 Career Options:\n• Pharmacist (Hospital/Retail) - Rs 3-8 LPA\n• Drug Inspector - Rs 4-10 LPA\n• Medical Representative - Rs 3-10 LPA\n• Research Scientist - Rs 5-15 LPA\n• Quality Control Analyst - Rs 4-12 LPA\n• Pharmaceutical Company Jobs\n\n🎓 Higher Studies: M.Pharm, MBA (Pharma), PhD\n💰 Salary: Rs 3-15 LPA\n🏢 Employers: Sun Pharma, Cipla, Dr. Reddy's, Hospitals"
            suggestions = ["Pharmacist vs Doctor?", "Pharmacy career scope", "Medical representative job", "D.Pharm vs B.Pharm?"]
        
        # BBA/MANAGEMENT
        elif any(word in message for word in ['bba', 'business administration', 'management course']):
            response_text = "💼 BBA (Bachelor of Business Administration)\n\n⏱️ Duration: 3 years\n\n📚 Core Subjects:\n• Marketing Management\n• Financial Management\n• Human Resource Management\n• Operations Management\n• Business Analytics\n• Entrepreneurship\n• Organizational Behavior\n\n💼 Career Options:\n• Business Analyst - Rs 4-12 LPA\n• Marketing Executive - Rs 3-10 LPA\n• HR Executive - Rs 3-8 LPA\n• Sales Manager - Rs 4-15 LPA\n• Business Development Manager - Rs 5-18 LPA\n\n🎓 After BBA: MBA is highly recommended!\n💰 Salary: Rs 3-12 LPA (BBA), Rs 8-30 LPA (After MBA)\n🏢 Top Colleges: Shaheed Sukhdev, Christ University, NMIMS"
            suggestions = ["MBA after BBA?", "BBA vs BCom?", "Marketing career", "Business Analyst details"]
        
        # MBA
        elif any(word in message for word in ['mba', 'master of business', 'management degree']):
            response_text = "🎯 MBA (Master of Business Administration)\n\n⏱️ Duration: 2 years\n\n📚 Specializations:\n• MBA Finance - Banking, Investment\n• MBA Marketing - Brand Management, Sales\n• MBA HR - Human Resource Management\n• MBA Operations - Supply Chain, Logistics\n• MBA IT - Technology Management\n• MBA Healthcare - Hospital Management\n\n💼 Top Career Options:\n• Management Consultant - Rs 10-30 LPA\n• Investment Banker - Rs 15-50 LPA\n• Product Manager - Rs 12-35 LPA\n• Operations Manager - Rs 8-25 LPA\n• Business Head - Rs 15-60 LPA\n\n📝 Entrance: CAT, XAT, GMAT, MAT, CMAT\n💰 Salary: Rs 8-50 LPA (depends on college)\n🏆 Top B-Schools: IIMs, XLRI, FMS Delhi, ISB Hyderabad"
            suggestions = ["CAT preparation", "MBA Finance vs Marketing", "IIM admission", "MBA salary packages"]
        
        # LAW
        elif any(word in message for word in ['law', 'lawyer', 'llb', 'advocate', 'legal']):
            response_text = "⚖️ Law Courses in India\n\n📚 Degree Options:\n• BA LLB - 5 years (after 12th)\n• BBA LLB - 5 years (after 12th)\n• LLB - 3 years (after graduation)\n\n💼 Career Options:\n• Corporate Lawyer - Rs 6-30 LPA\n• Criminal Lawyer - Rs 5-25 LPA\n• Civil Lawyer - Rs 4-20 LPA\n• Legal Advisor - Rs 5-18 LPA\n• Judge (after clearing exams) - Rs 8-20 LPA\n• Legal Consultant - Rs 6-25 LPA\n\n🏛️ Practice Areas:\n• Corporate Law (highest paying)\n• Criminal Law\n• Civil Law\n• Family Law\n• Intellectual Property Law\n• Cyber Law\n\n📝 Entrance: CLAT, AILET, LSAT\n🏛️ Top Colleges: NLUs (NLSIU Bangalore, NALSAR Hyderabad)"
            suggestions = ["Corporate law career", "CLAT preparation", "Lawyer salary", "Criminal vs Civil law"]
        
        # BCA
        elif any(word in message for word in ['bca', 'computer application', 'computer applications']):
            response_text = "💻 BCA (Bachelor of Computer Applications)\n\n⏱️ Duration: 3 years\n\n📚 Curriculum:\n• Programming (C, C++, Java, Python)\n• Web Development (HTML, CSS, JavaScript)\n• Database Management (SQL, MongoDB)\n• Software Engineering\n• Data Structures\n• Computer Networks\n• Mobile App Development\n\n💼 Career Options:\n• Software Developer - Rs 3-10 LPA\n• Web Developer - Rs 3-12 LPA\n• System Analyst - Rs 4-12 LPA\n• Network Administrator - Rs 3-8 LPA\n• Database Administrator - Rs 4-12 LPA\n\n🎓 After BCA: MCA (Master of Computer Applications) recommended\n💰 Salary: Rs 3-12 LPA\n🆚 BCA vs BTech CSE: BCA is 3 years, focuses more on applications than theory"
            suggestions = ["BCA vs BTech?", "After BCA options", "MCA details", "Web Developer career"]
        
        # BSc
        elif any(word in message for word in ['bsc', 'bachelor of science', 'b.sc']):
            response_text = "🔬 BSc (Bachelor of Science)\n\n⏱️ Duration: 3 years\n\n📚 Popular Specializations:\n• BSc Physics\n• BSc Chemistry\n• BSc Mathematics\n• BSc Computer Science\n• BSc Biology/Biotechnology\n• BSc Agriculture\n• BSc Nursing\n• BSc Microbiology\n\n💼 Career Options:\n• Research Scientist - Rs 4-15 LPA\n• Lab Technician - Rs 2-6 LPA\n• Teacher/Lecturer - Rs 3-10 LPA\n• Data Analyst - Rs 4-12 LPA\n• Quality Analyst - Rs 3-8 LPA\n\n🎓 After BSc:\n• MSc (Higher studies in specialization)\n• B.Ed (Teaching)\n• MCA (For BSc CS/IT students)\n• MBA\n\n💰 Salary: Rs 2-12 LPA (varies by field)"
            suggestions = ["BSc vs BTech?", "After BSc options", "MSc details", "Research career"]
        
        # BA (ARTS)
        elif any(word in message for word in ['ba ', 'bachelor of arts', 'b.a ', 'arts course']):
            response_text = "🎨 BA (Bachelor of Arts)\n\n⏱️ Duration: 3 years\n\n📚 Popular Subjects:\n• English Literature\n• History\n• Political Science\n• Economics\n• Psychology\n• Sociology\n• Journalism & Mass Communication\n• Fine Arts\n\n💼 Career Options:\n• Content Writer - Rs 3-8 LPA\n• Journalist - Rs 3-10 LPA\n• Civil Services (UPSC) - Rs 9-18 LPA\n• HR Executive - Rs 3-8 LPA\n• Teacher - Rs 3-10 LPA\n• Social Worker - Rs 2-6 LPA\n\n🎓 After BA:\n• MA (Specialization)\n• MBA\n• B.Ed (Teaching)\n• UPSC/State PSC preparation\n• LLB\n\n💰 Salary: Rs 2-10 LPA"
            suggestions = ["BA vs BSc?", "UPSC preparation", "After BA options", "Journalism career"]
        
        # ARCHITECTURE
        elif any(word in message for word in ['architecture', 'b.arch', 'barch', 'architect']):
            response_text = "🏛️ B.Arch (Bachelor of Architecture)\n\n⏱️ Duration: 5 years\n\n📚 What You'll Learn:\n• Architectural Design\n• Building Construction\n• Urban Planning\n• Landscape Architecture\n• Structural Systems\n• CAD/3D Modeling (AutoCAD, Revit, SketchUp)\n• Sustainable Architecture\n\n💼 Career Options:\n• Architect - Rs 4-15 LPA\n• Urban Planner - Rs 5-18 LPA\n• Interior Designer - Rs 3-12 LPA\n• Landscape Architect - Rs 4-12 LPA\n• Architectural Consultant - Rs 6-20 LPA\n\n📝 Entrance: NATA (National Aptitude Test in Architecture)\n💰 Salary: Rs 4-20 LPA\n🎨 Skills Needed: Creativity, drawing, design thinking\n🏢 Practice: Can start your own firm after experience!"
            suggestions = ["NATA exam details", "Architecture vs Civil?", "Interior design career", "Architect salary growth"]
        
        # COMMERCE/CA
        elif any(word in message for word in ['ca', 'chartered accountant', 'commerce', 'accountancy']):
            response_text = "📊 CA (Chartered Accountant)\n\n⏱️ Duration: 4-5 years (after 12th)\n\n📚 CA Course Structure:\n1. CA Foundation (4 months)\n2. CA Intermediate (8 months)\n3. Articleship (3 years practical training)\n4. CA Final (6 months)\n\n💼 Career Options:\n• Chartered Accountant (Practice) - Rs 8-30 LPA\n• Tax Consultant - Rs 6-25 LPA\n• Financial Analyst - Rs 7-20 LPA\n• Auditor - Rs 6-18 LPA\n• CFO (Chief Financial Officer) - Rs 20-80 LPA\n\n🏢 Work Areas:\n• Income Tax\n• GST\n• Auditing\n• Financial Planning\n• Corporate Finance\n\n💰 Salary: Rs 7-50 LPA (highly respected profession)\n🎯 Why CA?: High prestige, excellent salary, job security"
            suggestions = ["CA vs MBA?", "CA preparation tips", "BCom vs CA?", "Tax consultant career"]
        
        # HOTEL MANAGEMENT
        elif any(word in message for word in ['hotel management', 'hospitality', 'bhmct', 'hotel course']):
            response_text = "🏨 Hotel Management & Hospitality\n\n📚 Courses:\n• BHM (Bachelor of Hotel Management) - 3 years\n• BHMCT (Hotel Management & Catering Technology) - 4 years\n• Diploma in Hotel Management - 1-2 years\n\n💼 Career Options:\n• Hotel Manager - Rs 4-15 LPA\n• Chef - Rs 3-12 LPA\n• Event Manager - Rs 4-12 LPA\n• Restaurant Manager - Rs 3-10 LPA\n• Cruise Ship Jobs - Rs 5-20 LPA\n• Aviation Catering - Rs 4-12 LPA\n\n🌍 Specializations:\n• Food & Beverage Service\n• Front Office Operations\n• Housekeeping Management\n• Kitchen/Culinary Arts\n\n🏢 Employers: Taj, Oberoi, Marriott, ITC Hotels\n💰 Salary: Rs 3-15 LPA (international opportunities available!)"
            suggestions = ["Chef career", "Cruise ship jobs", "Hotel management scope", "Event management"]
        
        # FASHION DESIGN
        elif any(word in message for word in ['fashion', 'design', 'nift', 'fashion designer']):
            response_text = "👗 Fashion Design & Styling\n\n📚 Courses:\n• B.Des Fashion Design - 4 years\n• BSc Fashion Design - 3 years\n• Diploma in Fashion Design - 1-2 years\n\n💼 Career Options:\n• Fashion Designer - Rs 3-15 LPA\n• Textile Designer - Rs 3-10 LPA\n• Fashion Stylist - Rs 4-12 LPA\n• Costume Designer - Rs 3-10 LPA\n• Fashion Merchandiser - Rs 4-12 LPA\n• Fashion Blogger/Influencer - Rs 5-20 LPA\n\n🏆 Top Institutes: NIFT, Pearl Academy, NID\n📝 Entrance: NIFT Entrance Exam, NID DAT\n💰 Salary: Rs 3-20 LPA\n🎨 Skills: Creativity, sketching, fabric knowledge, trend awareness\n🌟 Bonus: Can start your own fashion brand!"
            suggestions = ["NIFT admission", "Fashion designer salary", "Textile design career", "Fashion blogging"]
        
        # ANIMATION/VFX
        elif any(word in message for word in ['animation', 'vfx', '3d', 'graphics design', 'animator']):
            response_text = "🎬 Animation & VFX\n\n📚 Courses:\n• BSc Animation & VFX - 3 years\n• Diploma in Animation - 1-2 years\n• Certificate Courses - 6 months to 1 year\n\n💼 Career Options:\n• 3D Animator - Rs 3-12 LPA\n• VFX Artist - Rs 4-15 LPA\n• Game Designer - Rs 4-15 LPA\n• Motion Graphics Designer - Rs 3-10 LPA\n• Character Designer - Rs 4-12 LPA\n• Video Editor - Rs 3-10 LPA\n\n🎨 Tools You'll Learn:\n• Maya, Blender, 3ds Max\n• After Effects, Premiere Pro\n• Unity, Unreal Engine (for games)\n\n🎬 Industries: Movies, Gaming, Advertising, YouTube\n💰 Salary: Rs 3-15 LPA\n🌟 Growing Field: OTT platforms increasing demand!"
            suggestions = ["Game design career", "VFX artist salary", "Animation courses", "YouTube career"]
        
        # CAREER SUGGESTIONS
        elif any(word in message for word in ['suggest', 'recommend', 'which career', 'confused', 'help me choose']):
            response_text = "🎯 Let me help you find the perfect career!\n\nTell me about your interests:\n\n1️⃣ TECHNOLOGY LOVER?\n• Like computers, coding, apps?\n→ BTech CSE, BCA, Data Science\n\n2️⃣ WANT TO HELP PEOPLE?\n• Interested in medicine, healthcare?\n→ MBBS, BDS, Pharmacy, Nursing\n\n3️⃣ BUSINESS MINDED?\n• Like management, entrepreneurship?\n→ BBA, MBA, CA, Commerce\n\n4️⃣ CREATIVE PERSON?\n• Love art, design, fashion?\n→ Fashion Design, Architecture, Animation\n\n5️⃣ LOVE SCIENCE & RESEARCH?\n• Enjoy experiments, discoveries?\n→ BSc, MSc, Research careers\n\n6️⃣ ANALYTICAL THINKER?\n• Good with logic, law, debates?\n→ Law, CA, Data Analytics\n\nWhat describes you best?"
            suggestions = ["I love technology", "I want to help people", "I'm creative", "I like business"]
        
        # SOFTWARE ENGINEERING
        elif any(word in message for word in ['software engineer', 'software developer', 'coding career']):
            career = CAREER_DATA['software_engineer']
            response_text = f"💻 {career['title']}\n\n📋 Job Description:\n{career['description']}\n\n🛠️ Skills Required:\n{', '.join(career['skills'])}\n\n🎓 Education: {career['education']}\n💰 Salary: {career['salary']}\n\n👨‍💻 Job Roles:\n• Full Stack Developer - Build complete websites\n• Backend Developer - Server-side programming\n• Frontend Developer - UI/UX development\n• Mobile App Developer - iOS/Android apps\n• DevOps Engineer - Deployment & automation\n\n🏢 Top Recruiters: Google, Microsoft, Amazon, Flipkart, TCS, Infosys\n📈 Career Growth: Can reach Rs 50+ LPA in 5-7 years!"
            suggestions = ["Programming languages", "Full Stack vs Backend?", "How to start coding?", "Software engineer day"]
        
        # BUSINESS ANALYST
        elif any(word in message for word in ['business analyst', 'business analysis']):
            career = CAREER_DATA['business_analyst']
            response_text = f"💼 {career['title']}\n\n📋 Job Description:\n{career['description']}\n\n🛠️ Skills: {', '.join(career['skills'])}\n\n🎓 Education: {career['education']}\n💰 Salary: {career['salary']}\n\n📊 What You'll Do:\n• Analyze business requirements\n• Create reports and presentations\n• Identify process improvements\n• Work with stakeholders\n• Data analysis & visualization\n\n🔧 Tools:\n• Excel (Advanced)\n• SQL\n• Tableau/Power BI\n• JIRA\n• SAP/ERP systems\n\n🏢 Industries: IT, Banking, Consulting, E-commerce, Healthcare"
            suggestions = ["Business Analyst skills", "Excel for BA", "BA vs Data Analyst", "How to become BA?"]
        
        # GOVERNMENT JOBS
        elif any(word in message for word in ['government job', 'sarkari naukri', 'upsc', 'ssc', 'railway']):
            response_text = "🏛️ Government Jobs in India\n\n📚 Major Exams:\n\n1️⃣ UPSC (Union Public Service Commission):\n• IAS, IPS, IFS - Rs 9-18 LPA\n• Age: 21-32 years\n• 3 stages: Prelims, Mains, Interview\n\n2️⃣ SSC (Staff Selection Commission):\n• SSC CGL - Rs 4-9 LPA\n• SSC CHSL - Rs 2-5 LPA\n• Age: 18-27 years\n\n3️⃣ Banking:\n• IBPS PO - Rs 4-8 LPA\n• SBI PO - Rs 5-10 LPA\n• RBI Grade B - Rs 7-15 LPA\n\n4️⃣ Railways:\n• RRB NTPC - Rs 2-6 LPA\n• RRB JE - Rs 4-8 LPA\n\n5️⃣ Defence:\n• NDA - Indian Army, Navy, Air Force\n• CDS - Combined Defence Services\n\n✅ Benefits: Job security, pension, medical, prestige"
            suggestions = ["UPSC preparation tips", "SSC CGL exam pattern", "Bank PO preparation", "Railway jobs details"]
        
        # DIGITAL MARKETING
        elif any(word in message for word in ['digital marketing', 'seo', 'social media marketing', 'marketing online']):
            response_text = "📱 Digital Marketing Career\n\n📚 What You'll Learn:\n• SEO (Search Engine Optimization)\n• SEM (Search Engine Marketing)\n• Social Media Marketing (Facebook, Instagram, LinkedIn)\n• Content Marketing\n• Email Marketing\n• Google Analytics\n• PPC (Pay Per Click) Advertising\n\n💼 Career Options:\n• Digital Marketing Manager - Rs 5-15 LPA\n• SEO Specialist - Rs 3-10 LPA\n• Social Media Manager - Rs 3-12 LPA\n• Content Strategist - Rs 4-12 LPA\n• PPC Specialist - Rs 4-10 LPA\n\n🎓 Education: Any degree + Digital Marketing certification\n💰 Salary: Rs 3-15 LPA\n\n📊 Certifications:\n• Google Digital Marketing Certificate\n• HubSpot Content Marketing\n• Facebook Blueprint\n• Google Analytics Certification\n\n🌟 Why Digital Marketing?: High demand, freelancing opportunities, work from home possible!"
            suggestions = ["SEO career", "Social media manager", "Google certifications", "Freelance digital marketing"]
        
        # CYBER SECURITY
        elif any(word in message for word in ['cyber security', 'ethical hacking', 'security', 'hacking career']):
            response_text = "🔐 Cyber Security Career\n\n📚 What You'll Learn:\n• Network Security\n• Ethical Hacking\n• Penetration Testing\n• Cryptography\n• Security Auditing\n• Incident Response\n• Malware Analysis\n\n💼 Career Options:\n• Cyber Security Analyst - Rs 5-15 LPA\n• Ethical Hacker - Rs 6-20 LPA\n• Security Consultant - Rs 7-18 LPA\n• Penetration Tester - Rs 6-18 LPA\n• Security Architect - Rs 12-30 LPA\n\n🎓 Education: BTech CSE/IT + Certifications\n💰 Salary: Rs 5-25 LPA\n\n📜 Important Certifications:\n• CEH (Certified Ethical Hacker)\n• CISSP\n• CompTIA Security+\n• OSCP\n\n🌟 Why Cyber Security?: Rapidly growing field, high demand, excellent pay!"
            suggestions = ["Ethical hacker career", "CEH certification", "Penetration testing", "How to start cyber security?"]
        
        # SALARY INFORMATION
        elif any(word in message for word in ['salary', 'pay', 'earning', 'income', 'package']):
            response_text = "💰 Average Salaries by Career (in India)\n\n🔝 HIGH PAYING (15+ LPA):\n• Software Engineer (FAANG) - Rs 20-50 LPA\n• Data Scientist - Rs 15-30 LPA\n• Investment Banker - Rs 15-40 LPA\n• Product Manager - Rs 15-35 LPA\n• Management Consultant - Rs 15-35 LPA\n\n💼 GOOD PAYING (8-15 LPA):\n• Doctor (after specialization) - Rs 10-30 LPA\n• Chartered Accountant - Rs 8-20 LPA\n• Corporate Lawyer - Rs 10-25 LPA\n• Architect - Rs 8-18 LPA\n• Civil Services (IAS/IPS) - Rs 9-18 LPA\n\n✅ AVERAGE PAYING (4-8 LPA):\n• Mechanical Engineer - Rs 4-10 LPA\n• Civil Engineer - Rs 4-10 LPA\n• Pharmacist - Rs 4-10 LPA\n• Business Analyst - Rs 5-12 LPA\n• Digital Marketing Manager - Rs 5-12 LPA\n\n📌 Note: Salaries vary by company, location, experience, and skills!"
            suggestions = ["Highest paying jobs", "Engineer salary comparison", "Medical field salary", "Tech vs Non-tech salary"]
        
        # STUDY ABROAD
        elif any(word in message for word in ['study abroad', 'foreign education', 'usa', 'uk', 'canada', 'australia']):
            response_text = "✈️ Studying Abroad\n\n🌍 Popular Destinations:\n\n1️⃣ USA:\n• Top for Engineering, Business, Medicine\n• Universities: MIT, Stanford, Harvard, UC Berkeley\n• Tests: GRE, GMAT, TOEFL/IELTS, SAT\n• Cost: $30,000 - $70,000/year\n\n2️⃣ UK:\n• Shorter duration (1 year Masters)\n• Universities: Oxford, Cambridge, Imperial College\n• Tests: IELTS, GRE/GMAT\n• Cost: £15,000 - £35,000/year\n\n3️⃣ Canada:\n• Easy immigration after studies\n• Universities: Toronto, UBC, McGill\n• Tests: IELTS, GRE/GMAT\n• Cost: CAD 15,000 - 35,000/year\n\n4️⃣ Germany:\n• Free/Low-cost education\n• Strong in Engineering\n• Tests: IELTS/TOEFL, GRE\n• Cost: €0 - €3,000/year (public universities)\n\n5️⃣ Australia:\n• Good for IT, Business\n• Universities: Melbourne, Sydney, ANU\n• Tests: IELTS, GRE/GMAT\n• Cost: AUD 20,000 - 45,000/year\n\n💼 Job prospects after study often excellent!"
            suggestions = ["USA vs UK for Masters?", "Study in Germany", "Canada PR after study", "Scholarships abroad"]
        
        # FREELANCING
        elif any(word in message for word in ['freelance', 'freelancing', 'work from home', 'remote work', 'gig']):
            response_text = "💻 Freelancing Careers\n\n📚 Top Freelance Skills:\n\n1️⃣ TECH:\n• Web Development - Rs 500-3000/hour\n• Mobile App Development - Rs 800-3500/hour\n• UI/UX Design - Rs 400-2000/hour\n• Data Science/ML - Rs 1000-4000/hour\n\n2️⃣ CREATIVE:\n• Graphic Design - Rs 300-1500/hour\n• Video Editing - Rs 400-2000/hour\n• Content Writing - Rs 200-1000/hour\n• Animation - Rs 500-2500/hour\n\n3️⃣ MARKETING:\n• Digital Marketing - Rs 400-2000/hour\n• SEO Specialist - Rs 300-1500/hour\n• Social Media Manager - Rs 300-1500/hour\n\n4️⃣ BUSINESS:\n• Virtual Assistant - Rs 200-800/hour\n• Consulting - Rs 1000-5000/hour\n• Accounting - Rs 300-1500/hour\n\n🌐 Platforms: Upwork, Fiverr, Freelancer.com, Toptal\n💰 Earning Potential: Rs 30,000 - Rs 3,00,000+/month\n✅ Benefits: Flexible hours, work from anywhere, be your own boss!"
            suggestions = ["Web development freelancing", "How to start freelancing?", "Upwork vs Fiverr", "Freelance graphic design"]
        
        # ENTREPRENEURSHIP
        elif any(word in message for word in ['business', 'startup', 'entrepreneur', 'own company', 'start business']):
            response_text = "🚀 Entrepreneurship & Starting Your Own Business\n\n💡 Popular Startup Ideas:\n\n1️⃣ TECH:\n• SaaS Product (Software as a Service)\n• Mobile App Development\n• E-commerce Platform\n• EdTech (Online Learning)\n• FinTech (Financial Technology)\n\n2️⃣ SERVICE BASED:\n• Digital Marketing Agency\n• Consulting Firm\n• Event Management\n• Coaching/Training Institute\n• Recruitment Agency\n\n3️⃣ TRADITIONAL:\n• Restaurant/Cafe\n• Retail Store\n• Manufacturing Unit\n• Export/Import Business\n\n📚 What You Need:\n• Business Idea & Market Research\n• Business Plan\n• Initial Capital/Funding\n• Legal Registration (LLP, Pvt Ltd)\n• Marketing Strategy\n\n💰 Funding Options:\n• Self-funded (Bootstrapping)\n• Angel Investors\n• Venture Capital\n• Bank Loans\n• Government Schemes (MUDRA, Startup India)\n\n🎓 Helpful: BBA, MBA, B.Tech (for tech startups)\n📈 Success Rate: Challenging but rewarding - many unicorns from India!"
            suggestions = ["Tech startup ideas", "How to get funding?", "Startup registration", "Business plan template"]
        
        # COURSES AFTER 12TH
        elif any(word in message for word in ['after 12th', 'after class 12', 'what to do after 12', 'courses after 12']):
            response_text = "🎓 Career Options After 12th\n\n📚 SCIENCE STREAM:\n• BTech/BE - Engineering\n• MBBS - Medicine\n• BDS - Dental\n• B.Pharm - Pharmacy\n• BSc - Pure Sciences\n• B.Arch - Architecture\n• BCA - Computer Applications\n• BSc Nursing\n\n💼 COMMERCE STREAM:\n• BCom - Commerce\n• BBA - Business Administration\n• CA - Chartered Accountancy\n• CS - Company Secretary\n• BMS - Management Studies\n• BBM - Business Management\n\n📖 ARTS STREAM:\n• BA - Arts (Various subjects)\n• BBA - Business Administration\n• LLB (5-year integrated)\n• Mass Communication\n• Hotel Management\n• Fashion Design\n• Animation/VFX\n\n🌟 SKILL-BASED:\n• Digital Marketing\n• Graphic Design\n• Web Development (Coding bootcamps)\n• Photography/Videography\n\n💡 My Advice: Choose based on your interests, not just marks or peer pressure!"
            suggestions = ["Best course after 12th Science", "Commerce career options", "Arts vs Commerce", "Skill courses"]
        
        # DEFAULT/GENERAL RESPONSE
        else:
            # Check if question contains "difference" or "vs"
            if 'difference' in message or ' vs ' in message or 'compare' in message:
                response_text = "🤔 I can help you compare careers and courses!\n\nPopular comparisons:\n• BTech vs BCA\n• MBBS vs BDS\n• BBA vs BCom\n• CSE vs IT\n• Data Scientist vs Software Engineer\n• CA vs MBA\n• BSc vs BTech\n• Mechanical vs Civil Engineering\n\nWhich comparison would you like to know about?"
                suggestions = ["BTech vs BCA", "MBBS vs BDS", "CSE vs IT", "CA vs MBA"]
            else:
                response_text = "I'm here to help with career guidance! 😊\n\nI can help you with:\n\n📚 Courses: BTech, MBBS, BBA, BCA, BSc, BA, Law, B.Arch, etc.\n💼 Career Advice: Which field suits you\n💰 Salary Information\n🎯 Career Paths\n🌍 Study Abroad\n💻 Freelancing & Entrepreneurship\n🏛️ Government Jobs\n\nWhat would you like to know?"
                suggestions = ["Engineering courses", "Medical field", "Business courses", "Career suggestions"]
        
        return jsonify({
            "response": response_text,
            "suggestions": suggestions
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": f"Server error: {str(e)}"}), 500

# ============= RUN APP =============
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=False)
