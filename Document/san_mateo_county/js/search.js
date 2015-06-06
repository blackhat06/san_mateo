$(document).ready(function() {
    $('.btn.btn-primary.btn-sm').click(function(){

        key_term = $(this).attr("term");
       // console.log(studentid);
        $.get('/search/' + studentid + '/', function(data){
      //  $.get('/checkout/' + studentid + '/', {studentid: studentid}, function(data){

        });

    });
});