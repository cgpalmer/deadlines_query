
console.log("Connected");


$( ".school_select" ).change(function() {
  console.log("changed");
  var value = $("#school_select_1").val();
  console.log(value);
  var option_val = $("#course_school_name").val();
  console.log(option_val);
});
