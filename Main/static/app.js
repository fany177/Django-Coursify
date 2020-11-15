var library = document.getElementById('library');
var catalog = document.getElementById('videoLibraryCatalog');
var upperbox=document.getElementById('upperbox');
var vlink1 = document.getElementById('vlink1');
library.addEventListener('click', mydisplay);
function mydisplay() {
    if(catalog.style.display=="none"){
        library.style.borderBottom = "2px solid #DB0C3E";
        upperbox.style.display="none";
        catalog.style.display = "flex";
        boardexams.style.display="block";
        vlink1.style.color = 'white';
        vlink1.style.backgroundColor = '#DB0C3E';
    }
    else
    {
        upperbox.style.display="block";
        catalog.style.display = "none";
        library.style.borderBottom = "none";
        for(var i=0;i<links.length;i++)
        {
            links[i].style.color="#1E4190";
            links[i].style.backgroundColor="white";
            boxes[i].style.display="none";
        }
    }
}
var vlink2 = document.getElementById('vlink2');
var vlink3 = document.getElementById('vlink3');
var vlink4 = document.getElementById('vlink4');
var vlink5 = document.getElementById('vlink5');
var vlink6 = document.getElementById('vlink6');
var boardexams = document.getElementById('boardexams');
var schoolexams = document.getElementById('schoolexams');
var jeemains = document.getElementById('jeemains');
var jeeadvanced = document.getElementById('jeeadvanced');
var neet = document.getElementById('neet');
var previousyear = document.getElementById('previousyear');
var links = document.querySelectorAll('.mylink')
var boxes = document.querySelectorAll('.mybox')


vlink1.addEventListener('click',vlink1func);
function vlink1func()
{
    for(var i=0;i<links.length;i++)
    {
        links[i].style.color="#1E4190";
        links[i].style.backgroundColor="white";
        boxes[i].style.display="none";
    }
    links[0].style.backgroundColor="#DB0C3E";
    links[0].style.color="white";
    boardexams.style.display="block";
}

vlink2.addEventListener('click',vlink2func);
function vlink2func()
{
    for(var i=0;i<links.length;i++)
    {
        links[i].style.color="#1E4190";
        links[i].style.backgroundColor="white";
        boxes[i].style.display="none";
    }
    links[1].style.backgroundColor="#DB0C3E";
    links[1].style.color="white";
    schoolexams.style.display="block";
}

vlink3.addEventListener('click',vlink3func);
function vlink3func()
{
    for(var i=0;i<links.length;i++)
    {
        links[i].style.color="#1E4190";
        links[i].style.backgroundColor="white";
        boxes[i].style.display="none";
    }
    links[2].style.backgroundColor="#DB0C3E";
    links[2].style.color="white";
    jeemains.style.display="block";
}

vlink4.addEventListener('click',vlink4func);
function vlink4func()
{
    for(var i=0;i<links.length;i++)
    {
        links[i].style.color="#1E4190";
        links[i].style.backgroundColor="white";
        boxes[i].style.display="none";
    }
    links[3].style.backgroundColor="#DB0C3E";
    links[3].style.color="white";
    jeeadvanced.style.display="block";
}

vlink5.addEventListener('click',vlink5func);
function vlink5func()
{
    for(var i=0;i<links.length;i++)
    {
        links[i].style.color="#1E4190";
        links[i].style.backgroundColor="white";
        boxes[i].style.display="none";
    }
    links[4].style.backgroundColor="#DB0C3E";
    links[4].style.color="white";
    neet.style.display="block";
}

vlink6.addEventListener('click',vlink6func);
function vlink6func()
{
    for(var i=0;i<links.length;i++)
    {
        links[i].style.color="#1E4190";
        links[i].style.backgroundColor="white";
        boxes[i].style.display="none";
    }
    links[5].style.backgroundColor="#DB0C3E";
    links[5].style.color="white";
    previousyear.style.display="block";
}

var goal=document.querySelector('.goal')
var goalsection=document.querySelector('.goalsection')
var show = document.querySelector('.show')

if (window.innerWidth<600)
{
goal.style.width="350px";
goal.style.transform="translateY(-10%)";
goalsection.style.width="50%";
goalsection.style.margin="auto";
catalog.style.flexDirection="column";
show.style.width="350px";
boardexams.style.width="300px";
boardexams.style.margin="auto";
schoolexams.style.width="300px";
jeemains.style.width="300px";
jeeadvanced.style.width="300px";
neet.style.width="300px";
previousyear.style.width="300px";
}
