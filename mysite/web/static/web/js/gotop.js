	// When the user scrolls down 20px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};
    
    function scrollFunction() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            document.getElementById("myBtn").style.display = "block";
        } else {
            document.getElementById("myBtn").style.display = "none";
        }
    }
    
    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }

var count = 0;
    function twtPopUp(){
        if (count == 0){
            document.getElementById("twitter-container").style.display = "block";
            count = 1;
        }else{
            document.getElementById("twitter-container").style.display = "none";
            count = 0;
        }
    }
