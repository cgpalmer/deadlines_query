
console.log("Connected");


$( ".school_select" ).change(function() {
  $(".course_option").addClass('hide');
  console.log("changed");
  var value = $(this).val();
  console.log(value);
  $(`.${value}`).removeClass('hide');
});

$( "#date_button" ).click(function() {
  $(".by_date").removeClass('hide');
  $(".by_course").addClass('hide');
});

$( "#course_button" ).click(function() {
  $(".by_date").addClass('hide');
  $(".by_course").removeClass('hide');
});

$( "#both_button" ).click(function() {
  $(".by_date").removeClass('hide');
  $(".by_course").removeClass('hide');
});