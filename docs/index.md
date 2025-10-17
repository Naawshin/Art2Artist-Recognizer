---
layout: page
title: Art2Artist Recognizer
subtitle: Discover the Artist Behind Every Masterpiece
cover-img: /Art2Artist-Recognizer/assets/img/art-background.png
---

<style>
/* Hero Section */
.hero-section {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(248, 249, 250, 0.95) 100%);
    padding: 3rem 2.5rem;
    border-radius: 20px;
    margin: 2rem 0;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
}

.hero-section h1 {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 1rem;
    line-height: 1.2;
}

.hero-section .subtitle {
    font-size: 1.3rem;
    color: #555;
    margin-bottom: 2rem;
    font-weight: 300;
}

.hero-section .description {
    font-size: 1.1rem;
    color: #666;
    max-width: 700px;
    margin: 0 auto 2rem;
    line-height: 1.8;
}

/* CTA Button */
.cta-button {
    display: inline-block;
    padding: 18px 45px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white !important;
    text-decoration: none;
    border-radius: 50px;
    font-size: 1.2rem;
    font-weight: 700;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    position: relative;
    overflow: hidden;
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5);
    color: white !important;
    text-decoration: none;
}

.cta-button:before {
    content: "🎨";
    margin-right: 10px;
    font-size: 1.3rem;
}

/* Features Section */
.features-section {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(252, 252, 252, 0.9) 100%);
    padding: 2.5rem;
    border-radius: 20px;
    margin: 2rem 0;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
}

.feature-card {
    background: white;
    padding: 2rem;
    border-radius: 15px;
    margin-bottom: 1.5rem;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
    border-left: 4px solid transparent;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.12);
}

.feature-card.purple { border-left-color: #667eea; }
.feature-card.pink { border-left-color: #f093fb; }
.feature-card.orange { border-left-color: #fa709a; }

.feature-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    display: block;
}

.feature-card h3 {
    color: #2c3e50;
    font-size: 1.5rem;
    margin-bottom: 0.8rem;
    font-weight: 700;
}

.feature-card p {
    color: #666;
    font-size: 1rem;
    line-height: 1.6;
    margin: 0;
}

/* Artists Section */
.artists-section {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 249, 250, 0.9) 100%);
    padding: 2.5rem;
    border-radius: 20px;
    margin: 2rem 0;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
}

.artists-section h2 {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 2.5rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.artist-category {
    background: white;
    padding: 1.8rem;
    border-radius: 15px;
    margin-bottom: 1.5rem;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

.artist-category:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
}

.artist-category h3 {
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 1.2rem;
    padding-bottom: 0.8rem;
    border-bottom: 3px solid;
    display: flex;
    align-items: center;
}

.artist-category h3 span {
    margin-right: 10px;
    font-size: 1.8rem;
}

.artist-category.expression h3 { 
    color: #667eea;
    border-bottom-color: #667eea;
}
.artist-category.classical h3 { 
    color: #f093fb;
    border-bottom-color: #f093fb;
}
.artist-category.impressionist h3 { 
    color: #fa709a;
    border-bottom-color: #fa709a;
}
.artist-category.global h3 { 
    color: #4facfe;
    border-bottom-color: #4facfe;
}

.artist-category ul {
    list-style: none;
    padding-left: 0;
    margin: 0;
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.5rem;
}

.artist-category li {
    padding: 0.6rem 0.8rem;
    position: relative;
    padding-left: 2rem;
    color: #444;
    font-size: 1rem;
    transition: all 0.2s ease;
    border-radius: 8px;
}

.artist-category li:hover {
    background: rgba(102, 126, 234, 0.05);
    padding-left: 2.5rem;
}

.artist-category li:before {
    content: "✦";
    position: absolute;
    left: 0.5rem;
    color: #667eea;
    font-size: 1rem;
}

/* Stats Section */
.stats-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2.5rem;
    border-radius: 20px;
    margin: 2rem 0;
    text-align: center;
    color: white;
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
}

.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.stat-item {
    text-align: center;
}

.stat-number {
    font-size: 3rem;
    font-weight: 800;
    display: block;
    margin-bottom: 0.5rem;
}

.stat-label {
    font-size: 1rem;
    opacity: 0.9;
    font-weight: 300;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-section h1 {
        font-size: 2rem;
    }
    
    .hero-section .subtitle {
        font-size: 1.1rem;
    }
    
    .artist-category ul {
        grid-template-columns: 1fr;
    }
}
</style>

<div class="hero-section">
    <h1>🎨 Art2Artist Recognizer</h1>
    <div class="subtitle">Powered by Deep Learning AI</div>
    <div class="description">
        Upload any artwork image and instantly discover which legendary artist created it. Our advanced neural network analyzes artistic styles, brushstrokes, and compositions across 20 iconic masters of art history.
    </div>
    <a href="{{ '/art2artist_recognizer' | relative_url }}" class="cta-button">Start Recognizing Art</a>
</div>

<div class="stats-section">
    <h2 style="margin-bottom: 1.5rem; font-size: 2rem;">Trained on Thousands of Masterpieces</h2>
    <div class="stats-grid">
        <div class="stat-item">
            <span class="stat-number">20</span>
            <span class="stat-label">Famous Artists</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">500+</span>
            <span class="stat-label">Years of Art</span>
        </div>
        <div class="stat-item">
            <span class="stat-number">AI</span>
            <span class="stat-label">Deep Learning</span>
        </div>
    </div>
</div>

<div class="features-section">
    <div class="row">
        <div class="col-md-4">
            <div class="feature-card purple">
                <span class="feature-icon">🤖</span>
                <h3>AI-Powered Recognition</h3>
                <p>Our deep learning model has been trained on thousands of artworks to accurately identify artistic styles and techniques.</p>
            </div>
        </div>
        <div class="col-md-4">
            <div class="feature-card pink">
                <span class="feature-icon">⚡</span>
                <h3>Instant Results</h3>
                <p>Upload your image and get immediate classification results with confidence scores for each artist.</p>
            </div>
        </div>
        <div class="col-md-4">
            <div class="feature-card orange">
                <span class="feature-icon">🎭</span>
                <h3>20 Legendary Artists</h3>
                <p>From Renaissance masters to modern expressionists, covering 500+ years of art history.</p>
            </div>
        </div>
    </div>
</div>

<div class="artists-section">
    <h2>🖼️ Supported Artists</h2>
    
    <div class="row">
        <div class="col-md-6">
            <div class="artist-category expression">
                <h3><span>🎭</span> Expression & Modern</h3>
                <ul>
                    <li>Edvard Munch</li>
                    <li>Vincent van Gogh</li>
                    <li>Gustav Klimt</li>
                    <li>Jackson Pollock</li>
                    <li>Mark Rothko</li>
                    <li>Joan Miró</li>
                    <li>Salvador Dalí</li>
                </ul>
            </div>
        </div>
        
        <div class="col-md-6">
            <div class="artist-category classical">
                <h3><span>🏛️</span> Classical & Renaissance</h3>
                <ul>
                    <li>Leonardo da Vinci</li>
                    <li>Michelangelo</li>
                    <li>Raphael</li>
                    <li>Caravaggio</li>
                    <li>Rembrandt van Rijn</li>
                </ul>
            </div>
        </div>
    </div>
    
    <div class="row">
        <div class="col-md-6">
            <div class="artist-category impressionist">
                <h3><span>🌅</span> Impressionists</h3>
                <ul>
                    <li>Claude Monet</li>
                    <li>Edgar Degas</li>
                    <li>Pierre-Auguste Renoir</li>
                    <li>Paul Cézanne</li>
                </ul>
            </div>
        </div>
        
        <div class="col-md-6">
            <div class="artist-category global">
                <h3><span>🌎</span> Global Masters</h3>
                <ul>
                    <li>Frida Kahlo</li>
                    <li>Diego Rivera</li>
                    <li>Henri Matisse</li>
                    <li>Pablo Picasso</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<div class="hero-section" style="margin-top: 3rem;">
    <h2 style="font-size: 2rem; margin-bottom: 1rem;">Ready to Explore Art History?</h2>
    <p style="color: #666; margin-bottom: 2rem;">Start identifying masterpieces with our AI-powered recognition system</p>
    <a href="{{ '/art2artist_recognizer' | relative_url }}" class="cta-button">Launch the App</a>
</div>