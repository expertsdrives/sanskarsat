function header_top(){
    var header_h = $('header').outerHeight();
    $('body').css('padding-top',header_h);
}

/* Window Load functions */

$(window).on('load',function(){
    setTimeout(function(){

    });
});
$(window).scroll(function() {    
    var scroll = $(window).scrollTop();
    if (scroll >= 50) {
        $("header").addClass("fixed");
    }
    else{
        $("header").removeClass("fixed");
    }
}); //missing );


$(document).ready(function(){
    header_top();
    $('header .search-icon').click(function(e){
        e.preventDefault();
        $('header .search-box').toggleClass('open');
    });
    if($(".banner-slider")[0]){
        $('.banner-slider').slick({
            infinite: true,
            arrows: true,
          });
    }
    if($(".workshop-slider")[0]){
    $('.workshop-slider').slick({
        infinite: true,
        slidesToShow: 3,
        dots: false,
        slidesToScroll: 3,
        responsive: [
            {
              breakpoint: 800,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                infinite: true,
                dots: true
              }
            },
            {
              breakpoint: 600,
              settings: {
                slidesToShow: 2,
                slidesToScroll: 2
              }
            },
            {
              breakpoint: 576,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1
              }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
          ]
      });
    }
    if($(".activity-slider")[0]){
      $('.activity-slider').slick({
          infinite: true,
          slidesToShow: 1,
          dots: false,
          fade: true,
          speed: 500,
        });
      }

    
      if($(window).width() < 768){
        $('header .menu > li').click(function(e){
           e.preventDefault();
            e.stopPropagation();
          $(this).siblings().find('.sub-menu').slideUp();
          $(this).find('.sub-menu').slideToggle();
        });
        $('.mobile-header-top .menu-icon').click(function(){
            $('#mobile_menu').addClass('open');
        });
        $('.header-bottom .close-icon,.header-bottom .menu li a').click(function(){
            $('#mobile_menu').removeClass('open');
        });
      }
      $('.acc-container .acc:nth-child(1) .acc-head').addClass('active');
      $('.acc-container .acc:nth-child(1) .acc-content').slideDown();
      $('.acc-head').on('click', function() {
          if($(this).hasClass('active')) {
            $(this).siblings('.acc-content').slideUp();
            $(this).removeClass('active');
          }
          else {
            $('.acc-content').slideUp();
            $('.acc-head').removeClass('active');
            $(this).siblings('.acc-content').slideToggle();
            $(this).toggleClass('active');
          }
      }); 
});

$(document).on("click", function (e) {
//   if ($(e.target).is("header .search-icon") === false) {
//       $("header .search-box").removeClass("open");
//   }
});

$(window).resize(function(){

})

