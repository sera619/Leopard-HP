const BackButton = document.getElementById('back-button');

if(BackButton != null){
    BackButton.addEventListener('click', function(){
        scrollToTop();
    })
    window.onscroll = function() {showScrollButton()};
}



function showScrollButton(){
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20){
        BackButton.style.display = "block";
    } else {
        BackButton.style.display = 'none';
    }
}

function scrollToTop(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}