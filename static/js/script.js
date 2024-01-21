$(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.slider').slider({edge:"right"});
    $('.collapsible').collapsible();
    $('select').formSelect();
    $(".tooltipped").tooltip();
    $(".datepicker").datepicker({
      format: "dddd mm/yy",
      yearRange: 3,
      showClearBtn: true,
      i18n: {
          done: "Select"
      }
    });
});


function confirmDelete() {
  var result = window.confirm("Are you sure you want to delete?");
  
  if (result) {
      // Call the function to delete the item
      deleteItem();
  } else {
      back()
  }
}