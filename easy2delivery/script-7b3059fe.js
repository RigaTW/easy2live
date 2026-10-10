document.addEventListener('DOMContentLoaded', () => {

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // ScrollSpy Logic for Navbar
    const sections = document.querySelectorAll('section');
    const navLinksList = document.querySelectorAll('.nav-links a');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop - 150) {
                // Determine current section ID based on scroll position
                current = section.getAttribute('id');
            }
        });

        navLinksList.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').substring(1) === current) {
                link.classList.add('active');
            }
        });
    });

    // Mobile Menu Logic
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const body = document.body;

    // Create the overlay container dynamically
    const mobileMenuOverlay = document.createElement('div');
    mobileMenuOverlay.classList.add('mobile-menu-overlay');

    // Clone the standard nav-links into the mobile menu overlay
    const mobileNavLinks = document.createElement('div');
    mobileNavLinks.classList.add('mobile-nav-links');

    // Copy nav links to the mobile menu so it stays aligned with content JS
    const originalNavLinks = document.querySelector('.nav-links').innerHTML;
    mobileNavLinks.innerHTML = originalNavLinks;

    mobileMenuOverlay.appendChild(mobileNavLinks);
    body.appendChild(mobileMenuOverlay);

    // Toggle menu state
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenuOverlay.classList.toggle('active');
            const icon = mobileMenuBtn.querySelector('i');
            if (mobileMenuOverlay.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
                body.style.overflow = 'hidden'; // prevent background scrolling
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
                body.style.overflow = '';
            }
        });
    }

    // Close menu when a link inside it is clicked
    mobileMenuOverlay.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            mobileMenuOverlay.classList.remove('active');
            const icon = mobileMenuBtn.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
            body.style.overflow = '';
        });
    });

    // Removed JavaScript-based 3D rotation as it conflicts with the new smooth CSS floating animation.
    // The phone mockup now relies entirely on CSS @keyframes for a more premium floating effect.

    // Add entry animations using Intersection Observer
    const animatedElements = document.querySelectorAll('.feature-card, .pro-container, .section-header');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    });

    animatedElements.forEach(el => {
        // Setup initial state for animation
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(el);
    });

});
// ==========================================
// Dynamic Content Loading System
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
    if (typeof SITE_CONTENT !== 'undefined') {
        const c = SITE_CONTENT;
        const setHtml = (selector, content) => {
            const el = document.querySelector(selector);
            if (el && content) el.innerHTML = content;
        };
        const setText = (selector, content) => {
            const el = document.querySelector(selector);
            if (el && content) el.textContent = content;
        };

        document.querySelectorAll('.logo-text').forEach(el => {
            el.innerHTML = `${c.brandNameBase}<span class="logo-number">${c.brandNameNum}</span>${c.brandNameSuffix}`;
        });
        const navLinks = document.querySelectorAll('.nav-links a');
        if (navLinks.length >= 3) {
            navLinks[0].textContent = c.navLink1; navLinks[1].textContent = c.navLink2; navLinks[2].textContent = c.navLink3;
        }
        const btnsStore = document.querySelectorAll('a[href="#download"]');
        if (btnsStore.length >= 1) {
            btnsStore[0].innerHTML = `<i class="fab fa-google-play"></i> ${c.btnGooglePlay}`;
        }

        setHtml('.badge', `<i class="fas fa-bolt"></i> ${c.heroBadge}`);
        setHtml('.hero-title', `${c.heroTitleLine1}<br><span class="gradient-text">${c.heroTitleLine2}</span>`);
        setHtml('.hero-subtitle', c.heroSubtitle);
        setHtml('.hero-actions .btn', `<i class="fas fa-rocket"></i> ${c.heroBtnText}`);
        setHtml('.trust-indicators span', c.heroTrustText);

        setHtml('#features .section-header h2', c.featuresTitle);
        setHtml('#features .section-header p', c.featuresSubtitle);
        const featureCards = document.querySelectorAll('.bento-card');
        if (featureCards.length >= 4) {
            setHtml('.bento-card:nth-child(1) h3', c.feature1Title); setHtml('.bento-card:nth-child(1) p', c.feature1Desc);
            setHtml('.bento-card:nth-child(2) h3', c.feature2Title); setHtml('.bento-card:nth-child(2) p', c.feature2Desc);
            setHtml('.bento-card:nth-child(3) h3', c.feature3Title); setHtml('.bento-card:nth-child(3) p', c.feature3Desc);
            setHtml('.bento-card:nth-child(4) h3', c.feature4Title); setHtml('.bento-card:nth-child(4) p', c.feature4Desc);
        }

        setHtml('#showcase .section-header h2', c.showcaseTitle); setHtml('#showcase .section-header p', c.showcaseSubtitle);
        const showcaseItems = document.querySelectorAll('.showcase-item');
        if (showcaseItems.length >= 4) {
            setHtml('.showcase-item:nth-child(1) .showcase-text h3', `<i class="fas fa-camera retro-icon"></i> ${c.showcase1Title}`); setHtml('.showcase-item:nth-child(1) .showcase-text p', c.showcase1Desc);
            setHtml('.showcase-item:nth-child(2) .showcase-text h3', `<i class="fas fa-map-marked-alt retro-icon"></i> ${c.showcase2Title}`); setHtml('.showcase-item:nth-child(2) .showcase-text p', c.showcase2Desc);
            setHtml('.showcase-item:nth-child(3) .showcase-text h3', `<i class="fas fa-motorcycle retro-icon"></i> ${c.showcase3Title}`); setHtml('.showcase-item:nth-child(3) .showcase-text p', c.showcase3Desc);
            setHtml('.showcase-item:nth-child(4) .showcase-text h3', `<i class="fas fa-charging-station retro-icon"></i> ${c.showcase4Title}`); setHtml('.showcase-item:nth-child(4) .showcase-text p', c.showcase4Desc);
        }

        setHtml('.pro-content h2', c.proTitle); setHtml('.pro-content p', c.proSubtitle);
        const proList = document.querySelectorAll('.pro-benefits li');
        if (proList.length >= 3) {
            proList[0].innerHTML = `<i class="fas fa-check-circle"></i> ${c.proBenefit1}`;
            proList[1].innerHTML = `<i class="fas fa-check-circle"></i> ${c.proBenefit2}`;
            proList[2].innerHTML = `<i class="fas fa-check-circle"></i> ${c.proBenefit3}`;
        }
        setHtml('.pro-content .btn', c.proBtnText); setText('.card-logo', c.proCardName);

        setHtml('.cta-section h2', c.ctaTitle); setHtml('.cta-section p', c.ctaSubtitle);

        setHtml('.faq-section h2', c.faqTitle); setHtml('.faq-section p', c.faqSubtitle);
        const faqItemsRender = document.querySelectorAll('.faq-item');
        if (faqItemsRender.length >= 3) {
            setHtml('.faq-item:nth-child(1) .faq-question span', c.faq1Question); setHtml('.faq-item:nth-child(1) .faq-answer', c.faq1Answer);
            setHtml('.faq-item:nth-child(2) .faq-question span', c.faq2Question); setHtml('.faq-item:nth-child(2) .faq-answer', c.faq2Answer);
            setHtml('.faq-item:nth-child(3) .faq-question span', c.faq3Question); setHtml('.faq-item:nth-child(3) .faq-answer', c.faq3Answer);
        }

        setHtml('.footer-brand p', c.footerSlogan);
        const legalLinks = document.querySelectorAll('.legal-links a');
        if (legalLinks.length >= 2) {
            legalLinks[0].textContent = c.footerPrivacy;
            legalLinks[1].textContent = c.footerFeedback;
        }
        setHtml('.footer-text p:first-child', c.footerCopyright);
    }
    // FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');

        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Close all other items
            faqItems.forEach(otherItem => {
                otherItem.classList.remove('active');
                otherItem.querySelector('.faq-answer').style.maxHeight = null;
            });

            // Toggle current item
            if (!isActive) {
                item.classList.add('active');
                answer.style.maxHeight = answer.scrollHeight + "px";
            }
        });
    });

});
