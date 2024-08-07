/* function process() {
    var generatordiv = document.getElementById('generatordiv');
    var loaderDiv = document.getElementById('loader');
    if (generatordiv.style.visibility == "hidden") {
        generatordiv.style.visibility = "visible";
        loaderDiv.style.visibility = "hidden";
    } else {
        generatordiv.style.visibility = "hidden";
        loaderDiv.style.visibility = "visible";
    }
    
    document.getElementById('promptform').addEventListener('submit', function(event) {
        event.preventDefault();
        switchTheme();
    });
}

function switchTheme() {
    var theme1 = document.getElementById('mainTheme');
    var theme2 = document.getElementById('loaderTheme');

    if (theme1.disabled) {
        theme1.disabled = false;
        theme2.disabled = true;
    } else {
        theme1.disabled = true;
        theme2.disabled = false;
    }
} */

function process() {
/*     var generatordiv = document.getElementById('generatordiv');
    var loaderDiv = document.getElementById('loader');
    if (generatordiv.style.visibility == "hidden") {
        generatordiv.style.visibility = "visible";
        loaderDiv.style.visibility = "hidden";
    } else {
        generatordiv.style.visibility = "hidden";
        loaderDiv.style.visibility = "visible";
    } */
    
    document.getElementById('promptform').addEventListener('submit', function(event) {
        event.preventDefault();
        switchTheme();

        setTimeout(function() {
            var formData = new FormData(document.getElementById('promptform'));
            var xhr = new XMLHttpRequest();
            xhr.open('POST', document.getElementById('promptform').action, true);
            xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');
            xhr.onreadystatechange = function () {
                if (xhr.readyState === XMLHttpRequest.DONE) {
                    animation.style.display = 'none'; // Hide the animation when the request is done
                    if (xhr.status === 200) {
                        // Handle success
                        console.log('Request successful');
                    } else {
                        // Handle error
                        console.log('Request failed');
                    }
                }
            };
            xhr.send(formData);
        }, 2000);
    });
}

function switchTheme() {
    var theme1 = document.getElementById('mainTheme');
    var theme2 = document.getElementById('loaderTheme');

    if (theme1.disabled) {
        theme1.disabled = false;
        theme2.disabled = true;
    } else {
        theme1.disabled = true;
        theme2.disabled = false;
    }
}

function dropDown() {
    var extras = document.getElementById("extras");
    text = extras.textContent.substring(0, extras.textContent.length - 2);
    var features = document.getElementById("features");

    if (features.style.visibility == "hidden") {
        features.style.visibility = "visible";
        features.style.display = "block";
        extras.textContent = text + " ▼";
        extras.style.fontSize = '24px';
    } else {
        features.style.visibility = "hidden";
        features.style.display = "none";
        extras.textContent = text + " ►";
        extras.style.fontSize = '24px';
    }
}


function copy() {
    var copyText = document.getElementById("title");
    var text = copyText.textContent
    navigator.clipboard.writeText(text.substring(10));
}
/* function toggleSidebar() {
    var arrow = document.getElementById("arrowbar");
    var sideBar = document.getElementById("sidebar");
    var sideBarText = document.getElementById("sideBarText");

    if (arrow.src == "file:///C:/Users/shado/OneDrive/Desktop/betterEncryptV2/pages/arrow-bar-right.svg") {
        arrow.src = "file:///C:/Users/shado/OneDrive/Desktop/betterEncryptV2/pages/arrow-bar-left.svg";
        sideBar.style.width = '30vh';
        sideBarText.style.visibility = 'visible';
    } else {
        arrow.src = "file:///C:/Users/shado/OneDrive/Desktop/betterEncryptV2/pages/arrow-bar-right.svg";
        sideBar.style.width = '5vh';
        sideBarText.style.visibility = 'hidden';
    }
} */