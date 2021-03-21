
console.log("Connected");


$( ".school_select" ).change(function() {
  $(".course_option").addClass('hide');
  console.log("changed");
  var value = $("#school_select_1").val();
  console.log(value);
  $(`.${value}`).removeClass('hide');
});


// $( ".add_button" ).click(function() {
//     $("#test").html(`
//     <select id="school_select_1" class="school_select" name="school_code">
//             <option value="" selected disabled>Select a school</option>
//             {% for school in schools %}
//             <!-- Change the value to school coe once they're included -->
    
//             <option value="{{school.school_code}}">{{school.name}}</option>
//             {% endfor %}
//         </select>
    
//     <select name="course_code" id="course_select"> 
//         <option value="" selected disabled>Select a school first</option>
//             {% for course in courses %}
//                 <option class="hide {{course.school_code}} course_option" id="" value="{{course.course_code}}">{{course.course_name}}</option>
//             {% endfor %}
//         </select>`
        
        
//         );

// });