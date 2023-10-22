$(function() {
    $('#lottery').on('click',function() {
        $('#lottery').hide();
        $('#winner').show();
        setTimeout(function(){
            $('#winner0').show(); 
        },1000);
        setTimeout(function(){
            $('#winner1').show(); 
        },2000);
        setTimeout(function(){
            $('#winner2').show(); 
        },3000);
        
        // .fadeIn(1000,function() {
        //     $('#winner1').fadeIn(1000,function(){
        //         $('#winner2').fadeIn(1000);
        //     });
        // });
    });
});