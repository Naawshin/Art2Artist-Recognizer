---
title: About Me
layout: default
---

<style>
    .about-container {
        max-width: 1000px;
        margin: 0 auto;
        padding: 3rem 2rem;
    }

    .about-header {
        text-align: center;
        margin-bottom: 3rem;
    }

    .about-header h1 {
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }

    .about-header p {
        font-size: 1.2rem;
        color: #666;
    }

    .profile-section {
        background: linear-gradient(135deg, #f5f9ff 0%, #f0f4ff 100%);
        border-radius: 20px;
        padding: 3rem;
        margin-bottom: 3rem;
        border: 1px solid rgba(102, 126, 234, 0.2);
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
        align-items: center;
    }

    .profile-image {
        text-align: center;
    }

    .profile-image-placeholder {
        width: 200px;
        height: 200px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 80px;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.25);
    }

    .profile-info h2 {
        font-size: 2rem;
        font-weight: 900;
        color: #1a1a2e;
        margin-bottom: 0.5rem;
    }

    .profile-info p {
        color: #667eea;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1.5rem;
    }

    .profile-info .bio {
        font-size: 1rem;
        color: #555;
        line-height: 1.8;
        margin-bottom: 1.5rem;
    }

    .social-links {
        display: flex;
        gap: 1rem;
    }

    .social-links a {
        display: inline-block;
        width: 45px;
        height: 45px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-decoration: none;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }

    .social-links a:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }

    .section {
        background: white;
        border-radius: 20px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    }

    .section h2 {
        font-size: 1.8rem;
        font-weight: 900;
        color: #1a1a2e;
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 3px solid #667eea;
    }

    .skills-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
    }

    .skill-item {
        background: linear-gradient(135deg, #f5f9ff 0%, #f0f4ff 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 4px solid #667eea;
    }

    .skill-item h3 {
        font-size: 1.1rem;
        font-weight: 800;
        color: #667eea;
        margin-bottom: 0.5rem;
    }

    .skill-item p {
        color: #555;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    .projects-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
    }

    .project-card {
        background: linear-gradient(135deg, #f5f9ff 0%, #f0f4ff 100%);
        padding: 2rem;
        border-radius: 15px;
        border-top: 4px solid #667eea;
        transition: all 0.3s ease;
    }

    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
    }

    .project-card h3 {
        font-size: 1.3rem;
        font-weight: 800;
        color: #1a1a2e;
        margin-bottom: 0.8rem;
    }

    .project-card p {
        color: #555;
        font-size: 0.95rem;
        line-height: 1.7;
        margin-bottom: 1rem;
    }

    .project-tags {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
    }

    .tag {
        background: #667eea;
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .timeline {
        position: relative;
        padding: 2rem 0;
    }

    .timeline-item {
        margin-bottom: 2rem;
        position: relative;
        padding-left: 2.5rem;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        width: 12px;
        height: 12px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 0 0 3px #667eea;
    }

    .timeline-item::after {
        content: '';
        position: absolute;
        left: 5px;
        top: 12px;
        width: 2px;
        height: calc(100% + 1rem);
        background: #e0e7ff;
    }

    .timeline-item:last-child::after {
        display: none;
    }

    .timeline-item h3 {
        font-size: 1.1rem;
        font-weight: 800;
        color: #1a1a2e;
        margin-bottom: 0.3rem;
    }

    .timeline-item .year {
        color: #667eea;
        font-weight: 600;
        font-size: 0.9rem;
    }

    .timeline-item p {
        color: #555;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-top: 0.5rem;
    }

    .cta-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        color: white;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
    }

    .cta-section h2 {
        font-size: 2rem;
        margin-bottom: 1rem;
        color: white;
        border: none;
        padding: 0;
    }

    .cta-section p {
        font-size: 1.1rem;
        margin-bottom: 2rem;
        color: rgba(255, 255, 255, 0.95);
    }

    .cta-button {
        display: inline-block;
        padding: 14px 45px;
        background: white;
        color: #667eea;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }

    .cta-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        color: #667eea;
    }

    @media (max-width: 900px) {
        .profile-section {
            grid-template-columns: 1fr;
            text-align: center;
        }

        .social-links {
            justify-content: center;
        }

        .skills-grid, .projects-grid {
            grid-template-columns: 1fr;
        }

        .about-header h1 {
            font-size: 2rem;
        }
    }

    @media (max-width: 600px) {
        .about-container {
            padding: 1.5rem 1rem;
        }

        .section {
            padding: 1.5rem;
        }

        .profile-image-placeholder {
            width: 150px;
            height: 150px;
            font-size: 60px;
        }

        .section h2 {
            font-size: 1.5rem;
        }
    }
</style>

<div class="about-container">
    <!-- Header -->
    <div class="about-header">
        <h1>About Me</h1>
        <p>Data Science | Machine Learning | Art & Technology</p>
    </div>

    <!-- Profile Section -->
    <div class="profile-section">
        <div class="profile-image">
            <div class="profile-image-placeholder">👩‍💻</div>
        </div>
        <div class="profile-info">
            <h2>Nowshin Tabasum</h2>
            <p>AI/ML Developer & Data Scientist</p>
            <p class="bio">
                I'm passionate about building intelligent systems that bridge art and technology. 
                With a strong foundation in machine learning and computer vision, I create innovative 
                solutions that make AI accessible and meaningful. Currently focused on deep learning 
                applications in image classification and artistic recognition.
            </p>
            <div class="social-links">
                <a href="https://github.com/naawshin" title="GitHub">🔗</a>
                <a href="mailto:nawshintabassum88@gmail.com" title="Email">📧</a>
                <a href="https://linkedin.com" title="LinkedIn">💼</a>
            </div>
        </div>
    </div>

    <!-- Skills Section -->
    <div class="section">
        <h2>🛠️ Skills & Expertise</h2>
        <div class="skills-grid">
            <div class="skill-item">
                <h3>Machine Learning</h3>
                <p>Deep learning, neural networks, TensorFlow, PyTorch, scikit-learn, model optimization</p>
            </div>
            <div class="skill-item">
                <h3>Computer Vision</h3>
                <p>Image classification, CNN architectures, image processing, OpenCV</p>
            </div>
            <div class="skill-item">
                <h3>Data Analysis</h3>
                <p>Data preprocessing, exploratory analysis, pandas, numpy, visualization</p>
            </div>
            <div class="skill-item">
                <h3>Web Development</h3>
                <p>Full-stack development, APIs, deployment, Gradio, Flask, modern frontend</p>
            </div>
            <div class="skill-item">
                <h3>Programming Languages</h3>
                <p>Python, JavaScript, HTML/CSS, SQL, Git & version control</p>
            </div>
            <div class="skill-item">
                <h3>Cloud & Deployment</h3>
                <p>Hugging Face Spaces, model deployment, cloud services, containerization</p>
            </div>
        </div>
    </div>

    <!-- Projects Section -->
    <div class="section">
        <h2>🎨 Featured Projects</h2>
        <div class="projects-grid">
            <div class="project-card">
                <h3>Art2Artist Recognizer</h3>
                <p>
                    An AI-powered image classification model that identifies artworks from 20 famous artists 
                    using deep learning. Trained on 16,000+ artworks with high accuracy.
                </p>
                <div class="project-tags">
                    <span class="tag">Deep Learning</span>
                    <span class="tag">CNN</span>
                    <span class="tag">Image Classification</span>
                </div>
            </div>
            <div class="project-card">
                <h3>Personal Portfolio</h3>
                <p>
                    Beautiful, responsive portfolio website showcasing projects and skills. 
                    Built with Jekyll and custom CSS with focus on elegant design.
                </p>
                <div class="project-tags">
                    <span class="tag">Jekyll</span>
                    <span class="tag">Web Design</span>
                    <span class="tag">Frontend</span>
                </div>
            </div>
        </div>
    </div>

    <!-- Education & Experience Timeline -->
    <div class="section">
        <h2>📚 Education & Experience</h2>
        <div class="timeline">
            <div class="timeline-item">
                <h3>AI/ML Developer</h3>
                <span class="year">Current</span>
                <p>Building innovative AI solutions and deploying machine learning models in production environments.</p>
            </div>
            <div class="timeline-item">
                <h3>Data Science Specialization</h3>
                <span class="year">2023</span>
                <p>Completed comprehensive training in machine learning, deep learning, and data analysis methodologies.</p>
            </div>
            <div class="timeline-item">
                <h3>Computer Science Background</h3>
                <span class="year">2019</span>
                <p>Strong foundation in algorithms, data structures, and software engineering principles.</p>
            </div>
        </div>
    </div>

    <!-- Call to Action -->
    <div class="cta-section">
        <h2>Let's Collaborate</h2>
        <p>Interested in working together or have a project in mind?</p>
        <a href="mailto:nawshintabassum88@gmail.com" class="cta-button">Get In Touch</a>
    </div>
</div>