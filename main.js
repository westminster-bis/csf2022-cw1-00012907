// Navbar Responsive Hamburger
const hamburger=document.querySelector(".hamburger");
//getting/adding the elemnts by their class name
const navbar=document.querySelector(".navbar");
hamburger.addEventListener("click", ()=>{
    hamburger.classList.toggle("active")
    navbar.classList.toggle("active")
})

document.querySelectorAll(".navbar a").forEach(n=>n.addEventListener("click",()=>{
    hamburger.classList.remove("active");
    navbar.classList.remove("active");
}))

let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" slideActive", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " slideActive";
  setTimeout(showSlides, 3000); // Change image every 3 seconds
}

function validateEmail(emailId)
{
var mailformat = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/; //checking if email address contains correct characters
if(emailId.value.match(mailformat))
{
document.form1.text1.focus();
return true;
}
else
{
alert("Invalid email address");
document.form1.text1.focus();
return false;
}
}    