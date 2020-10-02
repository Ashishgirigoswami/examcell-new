/**
 * Custom JS - Custom js for APEZ template
 * @version v1.6.0
 * @copyright 2018 Pepdev.
 */

/**
* OnDOMLoad
* ThemeSlider
* ResponsiveMenu
* ThemeAccordion
* FormAjaxsubmit
* Contact Submit Form
* Slider
* CountDown
* Modal
* Gallery
*/

(function ($) {
    "use strict";

    $('body').prepend('<div class="setting">' +
        '<div class="setting-wrapper">' +
        '<div class="setting-handle"><i class="fa fa-cogs"></i></div>' +
        '<div class="setting-container">' +
        '<div class="setting-layout">'+
        '<p class="text-center">Layout</p>'+
        '<div class="layout">'+
        '<a href="#" data-layout="wide">Wide</a>'+
        '<a href="#" data-layout="boxed">Boxed</a>'+
        '</div>'+
        '</div>'+
        '<div class="setting-color">'+
        '<p class="text-center pt-3">Theme Color</p>'+
        '<a theme="blue" style="background-color: #3483FF"></a>'+
        '<a theme="turquoise" style="background-color: #1BA9B6"></a>'+
        '<a theme="teal" style="background-color: #009688"></a>'+
        '<a theme="navy" style="background-color: #000080"></a>'+
        '<a theme="orange" style="background-color: #FF9D3F"></a>'+
        '<a theme="yellow" style="background-color: #FF8B00"></a>'+
        '<a theme="chocolate" style="background-color: #D2691E"></a>'+
        '<a theme="brown" style="background-color: #795548"></a>'+
        '<a theme="lightgreen" style="background-color: #54C799"></a>'+
        '<a theme="green" style="background-color: #05AC4E"></a>'+
        '<a theme="red" style="background-color: #F91941"></a>'+
        '<a theme="lightred" style="background-color: #FF513F"></a>'+
        '<a theme="purple" style="background-color: #8B91DD"></a>'+
        '<a theme="indigo" style="background-color: #3F51B5"></a>'+
        '<a theme="pink" style="background-color: #CB328B"></a>'+
        '</div>'+
        '</div>' +
        '</div>' +
        '</div>');

    /*$('.color').scrollToFixed({
        marginTop: 200
    });
    */
    $('.setting-handle').click(function () {
        if ($('.setting-wrapper').css('right') === '0px') {
            $('.setting-wrapper').css('right', '-164px');
        } else {
            $('.setting-wrapper').css('right', '0');
        }
    });

    function store(name, val) {
        if (typeof (Storage) !== "undefined") {
            localStorage.setItem(name, val);
        } else {
            window.alert('Please use a modern browser to properly view this template!');
        }
    }

    function get(name) {
        if (localStorage.getItem(name) !== null) {
            return localStorage.getItem(name)
        } else {
            return null;
        }
    }

    function appendLink(name) {
        var $head = $("head");
        var $headlinklast = $head.find("link[rel='stylesheet']:last");
        var linkElement = '<link rel="stylesheet" id="theme" href="dist/css/style-'+name+'.css" type="text/css">';
        if ($headlinklast.length){
            $headlinklast.after(linkElement);
        }
        else {
            $head.append(linkElement);
        }
    }

    var currentTheme = get('theme'), currentlayout = get('layout');
    if(currentTheme) {
        appendLink(currentTheme)
    }
    if (currentlayout) {
        $('.wrapper').addClass(currentlayout);
        if (currentlayout === "boxed") {
            $('.setting-layout a:nth-child(2)').addClass('active');
        } else {
            $('.setting-layout a:nth-child(1)').addClass('active');
        }
    } else {
        $('.setting-layout a:nth-child(1)').addClass('active');
    }

    $(".setting-color a").click(function(e){
        e.preventDefault();
        var currentStyle = $(this).attr('theme');
        if ($('#theme').length) {
            var currentStyle = $(this).attr('theme');
            store('theme', currentStyle);
            $('#theme').attr({href: 'dist/css/style-'+currentStyle+'.css'})
        } else {
            appendLink(currentStyle);
        }
    });

    $('.setting-layout a').click(function (e) {
        e.preventDefault();
        var ele = $(this);
        $('.setting-layout a').removeClass('active');
        if (ele.data('layout') === 'boxed') {
            store('layout', 'boxed');
            $('.wrapper').addClass('boxed');
            ele.addClass('active');
        } else {
            store('layout', 'wide');
            $('.wrapper').removeClass('boxed');
            ele.addClass('active');
        }   
    })


    //*************************************************
    //OnDOMLoad  **************************************
    //*************************************************

    $('[data-toggle="tooltip"]').tooltip();
    $(window).on('load', function () {
        $('.slider-wrapper').flexslider({
            animation: "fade",
            animationLoop: true,
            pauseOnHover: true,
            keyboard: true,
            controlNav: false
        });
        $('.slider-height').removeClass();
        $('.thumbnail-slider').flexslider({
            animation: "slide",
            controlNav: "thumbnails"
        });
    });

    //*************************************************
    //ThemeSlider  ************************************
    //*************************************************
    $('.theme-flexslider').flexslider({
        animation: "slide",
        animationLoop: true,
        pauseOnHover: true
    });

    $(".theme-owlslider").owlCarousel({
        items: 1,
        dots: true
    });

    //*************************************************
    //ResponsiveMenu  *********************************
    //*************************************************
    
    /*$('.header-light').scrollToFixed({
        preFixed: function () {
            $('.header-light').addClass('hdr-fixed-light');
        },
        postFixed: function () {
            $('.header-light').removeClass('hdr-fixed-light');
        }
    });

    $('.header-dark').scrollToFixed({
        preFixed: function () {
            $('.header-dark').addClass('hdr-fixed-dark');
        },
        postFixed: function () {
            $('.header-dark').removeClass('hdr-fixed-dark');
        }
    });

    $('.header-colored').scrollToFixed({
        preFixed: function () {
            $('.header-colored').addClass('hdr-fixed-colored');
        },
        postFixed: function () {
            $('.header-colored').removeClass('hdr-fixed-colored');
        }
    });

    $('.header-gradient').scrollToFixed({
        preFixed: function () {
            $('.header-gradient').addClass('hdr-fixed-gradient');
        },
        postFixed: function () {
            $('.header-gradient').removeClass('hdr-fixed-gradient');
        }
    });*/

    $('body').on('click', '#menu-bar', function () {
        var menu = $('.menu');
        $('body').css('overflow', 'hidden');
        menu.css('left', '0');
        menu.show();
    });

    $('body').on('click', '.mobile-menu-close', function () {
        var menu = $('.menu');
        $('body').css('overflow', 'visible');
        menu.css('left', '-130%');
        menu.hide();
    });

    $(window).on('resize', function () {
        var menu = $('.menu');
        if ($(window).width() > 992) {
            $('body').css('overflow', 'visible');
            menu.css('display', 'block');
            menu.css('left', 'inherit');
        } else {
            menu.css('display', 'none');
            menu.css('left', '-130%');
        }
    });

    $('.menu').on('click', '.hdr-search', function () {
        $('.search-bar').css('display', 'table');
        return false;
    });

    $('body').on('click', '.search-close', function () {
        var ele = $('.search-bar');
        ele.addClass('zoomOut');
        setTimeout(function(){ 
            ele.css('display', 'none');
            ele.removeClass('zoomOut');
        }, 400);
    });

    //*************************************************
    //Side Panel **************************************
    //*************************************************
    //Open Left Panel
    $('.open-left-panel').on('click', function () {
        $('.side-panel-left').addClass('active');
        $('.overlay').fadeIn();
    });
     //Open Right Panel
     $('.open-right-panel').on('click', function () {
        $('.side-panel-right').addClass('active');
        $('.overlay').fadeIn();
    });
    //CLose Panel
    $('.close-panel, .overlay').on('click', function () {
        $('.side-panel').removeClass('active');
        $('.overlay').fadeOut();
    });

    //*************************************************
    //ThemeAccordion **********************************
    //*************************************************
    $('.theme-accordion:nth-child(1) .theme-accordion-bdy').slideDown();
    $('.theme-accordion:nth-child(1) .theme-accordion-control .fa').addClass('fa-minus');
    $('body').on('click', '.theme-accordion-hdr', function () {
        var ele = $(this);
        $('.theme-accordion-bdy').slideUp();
        $('.theme-accordion-control .fa').removeClass('fa-minus');
        if (ele.parents('.theme-accordion').find('.theme-accordion-bdy').css('display') === "none") {
            ele.find('.theme-accordion-control .fa').addClass('fa-minus');
            ele.parents('.theme-accordion').find('.theme-accordion-bdy').slideDown();
        } else {
            ele.find('.theme-accordion-control .fa').removeClass('fa-minus');
            ele.parents('.theme-accordion').find('.theme-accordion-bdy').slideUp();
        }
    });

    //Processing Button
    $('body').on('click', '.button-process', function () {
        var ele = $(this);
        ele.button('loading');
        setTimeout(function () { ele.button('reset'); }, 8000);
    });

    //*************************************************
    //Contact Submit Form *****************************
    //*************************************************

    $('body').on('click', '.contact-submit', function () {
        var ele = $(this), data = {};
        ele.button('loading');
        data.name = $('#name').val();
        data.email = $('#email').val();
        data.mobile = $('#phone').val();
        data.subject = $('#subject').val();
        data.message = $('#message').val();
        $.ajax({
            type: 'post',
            url: 'inc/contact-form.php',
            data: { name: data.name, email: data.email, mobile: data.mobile, subject: data.subject, message: data.message },
            error: function () {
                $('.contact-error .alert').remove();
                $('.contact-error').append('<div class="alert alert-danger" role="alert">Server Error Please try again after some time...</div>');
            },
            success: function (response) {
                var data = $.parseJSON(response);
                if (data.flag === "1") {
                    ele.button('reset');
                    $('.contact-error .alert').remove();
                    $('.contact-error').append('<div class="alert alert-danger" role="alert">Please enter ' + data.error + ' ! ! !</div>');
                } else {
                    ele.button('reset');
                    $('.contact-error .alert').remove();
                    $('.contact-error').append('<div class="alert alert-success" role="alert">Request Created Successfully.</div>');
                }
            }
        });
    });

    //*************************************************
    //Slider ******************************************
    //*************************************************
    //Testimonial Slider
    $(".testimonial-container").owlCarousel({
        items: 1,
        dots: true
    });

    $('.multi-item-slider').owlCarousel({
        loop:true,
        margin:10,
        autoplay: true,
        responsiveClass:true,
        dots: true,
        responsive:{
            0:{
                items:1,
                nav:true
            },
            600:{
                items:3,
                nav:false
            },
            1000:{
                items:4,
                nav:false,
                loop:false
            }
        }
    })

    //*************************************************
    //CountDown ******************************************
    //*************************************************
    $('.counter').counterUp({
        delay: 10,
        time: 400
    });

    //*************************************************
    //Portfolio  ****************************************
    //*************************************************
    $('.gallery-block').magnificPopup({
        delegate: 'a',
        type: 'image',
        gallery: {
            enabled: true
        }
    });

    $('.portfolio-masonary').masonry({
        itemSelector: '.portfolio-img'
    });

    $('body').on('click', '.portfolio-filter' ,function(){
        var ele = $(this), value = ele.attr('data-filter');
        $('.portfolio-filter').removeClass('active');
        ele.addClass('active');
        if(value == "all") {
            $('.filter').show('1000');
        } else {
            $(".filter").not('.'+value).hide('2000');
            $('.filter').filter('.'+value).show('3000');
        }
    });

    $('.portfolio-gallery').magnificPopup({
        type:'image',
        gallery: {
            enabled: true
        }
    });

    $('.gallery').magnificPopup({
        type:'image',
        gallery: {
            enabled: true
        }
    });

}(jQuery));