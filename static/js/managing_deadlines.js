
console.log("Connected");


$( ".school_select" ).change(function() {
  $(".course_option").addClass('hide');
  console.log("changed");
  var value = $("#school_select_1").val();
  console.log(value);
  $(`.${value}`).removeClass('hide');
});

