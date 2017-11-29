var acc = document.getElementsByClassName("accordion");
var i;
var j;
acc[0].nextElementSibling.style.maxHeight = acc[0].nextElementSibling.scrollHeight + "px";
for (i = 0; i < acc.length; i++) {
  acc[i].onclick = function() {
    
    for (j = 0; j < acc.length; j++){
      var pepe = acc[j].nextElementSibling;
      pepe.style.maxHeight = null;
    }
    
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight){
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    } 
  }
}

var acc1 = document.getElementsByClassName("accordeon");
var i1;
var j1;
acc1[0].nextElementSibling.style.maxHeight = acc1[0].nextElementSibling.scrollHeight + "px";
for (i1 = 0; i1 < acc1.length; i1++) {
  acc1[i1].onclick = function() {
    
    for (j1 = 0; j1 < acc1.length; j1++){
      var pepe1 = acc1[j1].nextElementSibling;
      pepe1.style.maxHeight = null;
    }
    
    this.classList.toggle("active");
    var panel1 = this.nextElementSibling;
    if (panel1.style.maxHeight){
      panel1.style.maxHeight = null;
    } else {
      panel1.style.maxHeight = panel1.scrollHeight + "px";
    } 
  }
}