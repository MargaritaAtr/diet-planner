$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.slider').slider({edge:"right"});
    $('.collapsible').collapsible();
    $('select').formSelect();
    $(".datepicker").datepicker({
      format: "dddd mm/yy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
    });
});

