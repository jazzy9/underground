//Merci beaucoup Nora! http://pca.louiseveillard.com/experiments.php

$(document).ready(function(){
    moveCrossTo(window.innerWidth/2, window.innerHeight/2);
    $(document).on('click', function() {
      var mouseX = event.clientX;
      var mouseY = event.clientY;
      
      moveCrossTo(mouseX, mouseY);
      
    });
    
    function moveCrossTo(mouseX, mouseY) {
      $('#content_topleft')
        .width(mouseX)
        .height(mouseY)
      ;
      
      $('#content_bottomleft')
        .width(mouseX)
      ;
      
      $('#content_topright')
        .height(mouseY)
      ;      
    }

});