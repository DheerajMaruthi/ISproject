$(document).ready(function () {
  $('.down-arrow img').click(function () {
    $('html, body').animate({
      'scrollTop': $("#expertise").position().top
    });
  });
  $(".card--section--two").css('display', 'none');

  $(".card--section--two").slice(0, 2).show();
  $(".load--more").click(function (e) {
    e.preventDefault();
    $(".card--section--two:hidden").slice(0, 2).fadeIn("slow");

    if ($(".card--section--two:hidden").length == 0) {
      $(".load--more").fadeOut("slow");
    }
  });
              $('.slide-main').slick({
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
                fade: true,
                asNavFor: '.slide-nav'
              });
              $('.slide-nav').slick({
                slidesToShow: 3,
                slidesToScroll: 1,
                asNavFor: '.slide-main',
                dots: false,
                centerMode: false,
                arrows: false,
                focusOnSelect: true
              });
  $("#related").owlCarousel({
    loop: true,
    margin: 50,
    dots: false,
    navText: ["<img src='images/Bleft.png'>", "<img src='images/Bnext.png'>"],
    responsive: {
      0: {
        items: 1,
        nav: false,
        dots: true
      },
      700: {
        items: 2,
        nav: true,
        dots: false
      },
      1100: {
        items: 3,
        nav: true,
        loop: true
      }
    },
  })
  $('#social-carousel').owlCarousel({
    autoplay: true,
    center: true,
    loop: true,
    nav: true,
    autoplay: true,
    stagepadding: 0,
    navText: ["<img src='images/car-left.png'>", "<img src='images/car-right.png'>"],
    responsive: {
      0: {
       items: 1,
       dots:false, 
       nav:true,
       center: false,
      },
      600: { 
        items: 1, 
        dots:false, 
        nav:true, 
        stagePadding: 0 
      },
      992: { 
        items: 1, 
        dots:false, 
        nav:true, 
        stagePadding: 0 
      },
      1200: { items: 2, 
        dots:false, 
        nav:true, 
        stagePadding: 0 
      },
    }
  });
});
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

(function () {
  $(document).on("click", ".click-to-expand", function () {
    var imageSrc = $(this).parents(".image-grid").find("img").attr("src");
    $(".js-modal-image").attr("src", imageSrc);
  });
})();

$(window).scroll(function () {
  if ($(window).scrollTop() >= 200) {
    $('header').addClass('fixed-header');
  }
  else {
    $('header').removeClass('fixed-header');
  }
});
