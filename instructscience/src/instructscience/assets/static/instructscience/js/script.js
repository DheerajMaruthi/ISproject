$(document).ready(function () {
  $('.down-arrow img').click(function () {
    $('html, body').animate({
      'scrollTop': $("#expertise").position().top
    });
  });
  // $(".card--section--two").css('display', 'none');
  //
  // $(".card--section--two").slice(0, 2).show();
  // $(".load--more").click(function (e) {
  //   e.preventDefault();
  //   $(".card--section--two:hidden").slice(0, 2).fadeIn("slow");
  //
  //   if ($(".card--section--two:hidden").length == 0) {
  //     $(".load--more").fadeOut("slow");
  //   }
  // });
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
    navText: ["<img src='/static/instructscience/images/Bleft.png'>", "<img src='/static/instructscience/images/Bnext.png'>"],
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

  $('#videosection').owlCarousel({
    autoplay: true,
    autoplayTimeout: 5000,
    autoplayHoverPause: true,
    margin: 10,
    responsiveClass: true,
    navText: ["<img src='/static/instructscience/images/Bleft.png'>", "<img src='/static/instructscience/images/Bnext.png'>"],
    loop: true,
    responsive: {
      0: {
        items: 1,
        nav:false,
        dots:true
      },
      568: {
        items: 2,
        nav:false,
        dots:true
      },
      600: {
        items: 3,
        nav:true
      },
      1000: {
        items: 3,
        nav:true,
        center:true
      }
    }
  })
  $(document).ready(function() {
    $('.popup-youtube').magnificPopup({
      disableOn: 320,
      type: 'iframe',
      mainClass: 'mfp-fade',
      removalDelay: 160,
      preloader: false,
      fixedContentPos: true
    });
  });
  $('.item').magnificPopup({
    delegate: 'a',
  });
  $('#social-carousel').owlCarousel({
    autoplay: true,
    center: true,
    loop: true,
    nav: true,
    stagepadding: 0,
    navText: ["<img src='/static/instructscience/images/car-left.png'>", "<img src='/static/instructscience/images/car-right.png'>"],
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

$('#quote-carousel').owlCarousel({
  autoplay: true,
  center: true,
  loop: true,
  nav: true,
  navText: ["<img src='/static/instructscience/images/Bleft_small.png'>", "<img src='/static/instructscience/images/Bnext_small.png'>"],
  responsive: {
    0: {
     items: 1,
     dots:false,
     nav:true,
    },
    600: {
      items: 1,
      dots:false,
      nav:true,
    },
    992: {
      items: 2,
      dots:false,
      nav:true,
    },
    1200: {
      items: 3,
      dots:true,
      nav:false,
    },
  }
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
