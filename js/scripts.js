/*!
* Start Bootstrap - Agency v7.0.10 (https://startbootstrap.com/theme/agency)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-agency/blob/master/LICENSE)
*/
//
// Scripts
// 

document.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    }
});

$(document).ready(function(){
    var images=[
        'img/Rotterdam/Kubus.jpg',
        'img/Rotterdam/Museum_Boijmans.jpg',
        'img/Rotterdam/Museum_Rotterdam.jpg',
        'img/Rotterdam/Rotterdam_Skyline.jpg',
        'img/Rotterdam/Rotterdam_spring.jpg'
        // 'img/rotterdam.jpg',
        // 'img/rotterdam1.jpg'
        // 'img/img01.jpg',
        // 'img/img02.jpg',
        // 'img/img03.jpg',
        // 'img/img04.jpg',
        // 'img/img05.jpg',
        // 'img/img06.jpg',
        // 'img/img07.jpg',
        // 'img/img08.jpg',
		// 'img/img09.jpg',
		// 'img/img10.jpg',
		// 'img/img11.jpg',
		// 'img/img12.jpg',
		// 'img/img13.jpg',
		// 'img/img14.jpg',
		// 'img/img15.jpg',
		// 'img/img16.jpg'
];

    var randomNumber = Math.floor(Math.random() * images.length);
    var bgImg = 'url(' + images[randomNumber] + ')';

    $('header.masthead').css({'background-image':bgImg, 'background-size':'cover', });

});

$(document).ready(function(){

    $('header.workhead').css({
        "color": "#fff",
        "text-align": "center",
        "background-color": "#159957",
    });

});
