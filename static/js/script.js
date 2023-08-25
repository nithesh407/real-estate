'use strict';

/**
 * element toggle function
 */

const elemToggleFunc = function (elem) { elem.classList.toggle("active"); }



/**
 * navbar toggle
 */

const navbar = document.querySelector("[data-navbar]");
const overlay = document.querySelector("[data-overlay]");
const navCloseBtn = document.querySelector("[data-nav-close-btn]");
const navOpenBtn = document.querySelector("[data-nav-open-btn]");
const navbarLinks = document.querySelectorAll("[data-nav-link]");

const navElemArr = [overlay, navCloseBtn, navOpenBtn];

/**
 * close navbar when click on any navbar link
 */

for (let i = 0; i < navbarLinks.length; i++) { navElemArr.push(navbarLinks[i]); }

/**
 * addd event on all elements for toggling navbar
 */

for (let i = 0; i < navElemArr.length; i++) {
  navElemArr[i].addEventListener("click", function () {
    elemToggleFunc(navbar);
    elemToggleFunc(overlay);
  });
}



/**
 * header active state
 */

const header = document.querySelector("[data-header]");

window.addEventListener("scroll", function () {
  window.scrollY >= 400 ? header.classList.add("active")
    : header.classList.remove("active");
}); 

$(document).ready(function(){
  $(window).scroll(function(){
      // scroll navbar on scroll script
      if (this.scrollY > 20){
          $('.navbar').addClass("sticky");
          $('.menu-btn').addClass('sticky');
      }else{
          $('.navbar').removeClass("sticky");
          $('.menu-btn').removeClass("sticky");

          $('.navbar').removeClass('active');
          $('.navbar .menu').removeClass('active');
          $('.menu-btn i').removeClass('active');
      }
      
      // scroll-up button show/hide script
      if (this.scrollY > 200){
          $('.scroll-up').addClass('show');
      }else{
          $('.scroll-up').removeClass('show');
      }
  });

  // animate the gallery section by changing the background image
  
  var count = 1;
  var url = "";
  
  const phrases = [["Embrace", "Your Passion"], ["Build", "Your Future"], ["Follow", "Your Path"]];
  var text1 = "";
  var text2 = "";

  function updateGallery(){
      if (count == 3){
          count = 1;
      }else{
          count++;
      }

      text1 = phrases[count - 1][1];
      text2 = phrases[count - 1][0];

      url = '/static/images/' + '0' + String(count) + '-gallery'; 

      $('.gallery').css('background-image', 'url(' + url + '.jpg' + ')');
      $('.gallery-content .text-1').html(text1);
      $('.gallery-content .text-2').html(text2);
  }

  var timeInterval = 4000;
  var currentInterval = setInterval(updateGallery, timeInterval);

  // slide-up script
  $('.scroll-up').click(function(){
      $('html').animate({scrollTop: 0});
      // removing smooth scroll on slide-up button click
      $('html').css('scrollBehaviour', 'auto');
  });

  $('.navbar .menu li a').click(function(){
      // applying again smooth scroll on menu items click
      $('html').css("scrollBehavior", "smooth");
  });

  // toggle menu/navbar script
  $('.menu-btn, .menu li a').click(function(){
      $('.navbar').toggleClass('active');
      $('.navbar .menu').toggleClass('active');
      $('.menu-btn i').toggleClass('active');
  });
});
