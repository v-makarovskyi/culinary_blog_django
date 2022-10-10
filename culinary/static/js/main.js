//SET background 
const divsBg = document.querySelectorAll(".set-bg");
divsBg.forEach((item) => {
    const bg = item.dataset.setbg
    item.style.backgroundImage = "url("+ bg + ")"
});

//////////////////////////////////////////////////////////////////////////////

//Humberger MENU -- header
const open = document.querySelector(".humberger__open");
const wrapper = document.querySelector(".humberger__menu__wrapper");
const overlay = document.querySelector(".humberger__menu__overlay");

open.addEventListener("click", () => {
  wrapper.classList.add("show__humberger__menu__wrapper");
  overlay.classList.add("active");
});

overlay.addEventListener("click", () => {
  wrapper.classList.remove("show__humberger__menu__wrapper");
  overlay.classList.remove("active");
});
