document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;

  /* ------------------------- MODE SWITCH (signature) ------------------- */
  const modeButtons = document.querySelectorAll("[data-mode-btn]");
  const thumb = document.querySelector(".mode-switch .thumb");

  function applyMode(mode) {
    body.setAttribute("data-mode", mode);
    modeButtons.forEach((b) => b.classList.toggle("active", b.dataset.modeBtn === mode));
    document.querySelectorAll("[data-se][data-da]").forEach((el) => {
      el.textContent = mode === "se" ? el.dataset.se : el.dataset.da;
    });
    document.querySelectorAll("[data-track]").forEach((el) => {
      const track = el.dataset.track;
      el.style.display = track === "both" || track === mode ? "" : "none";
    });
    localStorage.setItem("portfolio-mode", mode);
    restartTyping(mode);
  }

   modeButtons.forEach((btn) => {
    btn.addEventListener("click", () => applyMode(btn.dataset.modeBtn));
  });

  /* ------------------------- TERMINAL TYPING ---------------------------- */
  const typingEl = document.querySelector("[data-typing]");
  const rolesByMode = {
    se: ["Software Engineer", "Django Developer", "Python Backend Dev", "Problem Solver"],
    da: ["Data Analyst", "Power BI Developer", "Python for Data", "Insight Hunter"],
  };
  let typingTimeout;

  function restartTyping(mode) {
    if (!typingEl) return;
    clearTimeout(typingTimeout);
    const words = rolesByMode[mode];
    let wordIndex = 0;
    let charIndex = 0;
    let deleting = false;

    function tick() {
      const word = words[wordIndex];
      if (!deleting) {
        charIndex++;
        typingEl.textContent = word.slice(0, charIndex);
        if (charIndex === word.length) {
          deleting = true;
          typingTimeout = setTimeout(tick, 1400);
          return;
        }
      } else {
        charIndex--;
        typingEl.textContent = word.slice(0, charIndex);
        if (charIndex === 0) {
          deleting = false;
          wordIndex = (wordIndex + 1) % words.length;
        }
      }
      typingTimeout = setTimeout(tick, deleting ? 40 : 85);
    }
    tick();
  }

  const savedMode = localStorage.getItem("portfolio-mode") || "se";
  applyMode(savedMode);
  /* ------------------------- NAVBAR SCROLL ------------------------------ */
  const navbar = document.querySelector(".navbar");
  window.addEventListener("scroll", () => {
    navbar.classList.toggle("scrolled", window.scrollY > 30);
  });

  /* ------------------------- ACTIVE NAV LINK ----------------------------- */
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav-links a, .mobile-nav a");
  const spy = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          navLinks.forEach((l) => l.classList.remove("active"));
          document
            .querySelectorAll(`a[href="#${entry.target.id}"]`)
            .forEach((l) => l.classList.add("active"));
        }
      });
    },
    { rootMargin: "-45% 0px -50% 0px" }
  );
  sections.forEach((s) => spy.observe(s));

  /* ------------------------- MOBILE NAV ---------------------------------- */
  const hamburger = document.querySelector(".hamburger");
  const mobileNav = document.querySelector(".mobile-nav");
  const closeBtn = document.querySelector(".mobile-nav .close-btn");
  if (hamburger && mobileNav) {
    hamburger.addEventListener("click", () => mobileNav.classList.add("open"));
    closeBtn.addEventListener("click", () => mobileNav.classList.remove("open"));
    mobileNav.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => mobileNav.classList.remove("open"))
    );
  }

  /* ------------------------- SCROLL REVEAL -------------------------------- */
  /* ------------------------- SCROLL REVEAL -------------------------------- */
  try {
    const revealEls = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window) {
      revealEls.forEach((el) => el.classList.add("pre"));
      const revealObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("in");
              revealObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.15 }
      );
      revealEls.forEach((el) => revealObserver.observe(el));
    }
  } catch (e) {
    console.warn("Reveal animation skipped:", e);
  }

  /* ------------------------- SKILL BARS ------------------------------------ */
    /* ------------------------- SKILL BARS ------------------------------------
     Bars already render at full width from the server (fail-safe). JS only
     adds the "grow from 0" animation on top, if IntersectionObserver exists. */
    try {
    if ("IntersectionObserver" in window) {
      const skillBars = document.querySelectorAll(".skill-bar-fill");
      const barObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.style.width = entry.target.dataset.value + "%";
              barObserver.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.4 }
      );
      skillBars.forEach((el) => barObserver.observe(el));
    }
  } catch (e) {
    console.warn("Skill bar animation skipped:", e);
  }
  /* ------------------------- PROJECT FILTER --------------------------------- */
  const filterBtns = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll("[data-category]");
  filterBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      filterBtns.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const cat = btn.dataset.filter;
      projectCards.forEach((card) => {
        const show = cat === "all" || card.dataset.category === cat;
        card.style.display = show ? "" : "none";
      });
    });
  });
});
