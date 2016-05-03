/**
 * Created by Ricky on 3/14/2016.
 */
$(function() {
  $('#id_username').addClass('form-control');
  $('#id_username').attr('placeholder', 'Username');
  $('#id_email').addClass('form-control');
  $('#id_email').attr('placeholder', 'Email');
  $('#id_password').addClass('form-control');
  $('#id_password').attr('placeholder', 'Password');
});
/* CODE IS ATTRIBUTED TO CLAUDIA ROMANO at https://codyhouse.co/gem/back-to-top/ */
jQuery(document).ready(function ($) {
    // browser window scroll (in pixels) after which the "back to top" link is shown
    var offset = 300,
    //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        offset_opacity = 4000,
    //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,
    //grab the "back to top" link
        $back_to_top = $('.cd-top');

    //hide or show the "back to top" link
    $(window).scroll(function () {
        ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('cd-is-visible') : $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }
    });

    //smooth scroll to top
    $back_to_top.on('click', function (event) {
        event.preventDefault();
        $('body,html').animate({
                scrollTop: 0,
            }, scroll_top_duration
        );
    });
});
/* END ATTRIBUTION */
