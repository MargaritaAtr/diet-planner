$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.slider').slider({edge:"right"});
    $('.collapsible').collapsible();
    $('select').formSelect();
    $(".tooltipped").tooltip();
    $('.modal').modal();
    $(".datepicker").datepicker({
      format: "dddd dd/mm",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
    });
});

