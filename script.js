var clicked = false
setTimeout(function () {
    if (clicked == false) {
        document.getElementById("knife").classList.remove("hide")
        document.getElementById("imp").setAttribute("onclick", "")
        document.getElementById("not_imp").setAttribute("onclick", "")
        document.getElementById("not_imp2").setAttribute("onclick", "")
        setTimeout(function () {
            document.getElementById("text").innerHTML = "<h1 class='text-warning text-center'>Всі мирні померли :)</h1>"
            document.getElementById("not_imp").classList.add("hide")
            setTimeout(function () {
                document.getElementById("knife").classList.add("hide")
            }, 1000)
        }, 2000)
    }
}, 15000)
function imp() {
    document.getElementById("text").innerHTML = "<h1 class='text-danger text-center'>Ви знайшли імпостора!</h1>"

    cls_lose()
    // var audio = new Audio('./win.mp3');
    // audio.play();
    setTimeout(function () {
        if (clicked == false) {
            document.getElementById("knife").classList.remove("hide")
            document.getElementById("imp").setAttribute("onclick", "")
            document.getElementById("not_imp").setAttribute("onclick", "")
            document.getElementById("not_imp2").setAttribute("onclick", "")
            setTimeout(function () {
                document.getElementById("text").innerHTML = "<h1 class='text-warning text-center'>Всі мирні померли :)</h1>"
                document.getElementById("not_imp").classList.add("hide")
            }, 2000)
        }
    }, 10000)
}
function imp2() {
    clicked = true
    document.getElementById("text").innerHTML = "<h1 class='text-danger text-center'>Ви знайшли всіх імпосторів!</h1>"

    winn()
    var audio = new Audio('./win.mp3');
    audio.play();
}
function fail() {
    document.getElementById("text").innerHTML = "<h1 class='text-warning text-center'>Вас з'їв імпостор на сніданок :)</h1>"
    cls_win()
    var audio = new Audio('./lose.mp3');
    audio.play();
    clicked = true
}
function winn() {
    document.getElementById("not_imp2").classList.add("hide")
    // document.getElementById("not_imp2").classList.add("hide")
    document.getElementById("imp").setAttribute("onclick", "")
    document.getElementById("not_imp2").setAttribute("onclick", "")

    // document.getElementById("images").innerHTML="<img style='margin: 0;position: absolute;top: 60%;left: 50%;-ms-transform: translate(-60%, -50%);transform: translate(-60%, -50%);' src='./amg.png' onclick='console.log()'"
}
function cls_win() {
    document.getElementById("not_imp").classList.add("hide")
    // document.getElementById("not_imp2").classList.add("hide")
    document.getElementById("imp").setAttribute("onclick", "")
    document.getElementById("not_imp").setAttribute("onclick", "")
    // document.getElementById("images").innerHTML="<img style='margin: 0;position: absolute;top: 60%;left: 50%;-ms-transform: translate(-60%, -50%);transform: translate(-60%, -50%);' src='./amg.png' onclick='console.log()'"
}
function cls_lose() {
    document.getElementById("imp").classList.add("hide")
    document.getElementById("imp").setAttribute("onclick", "")
    document.getElementById("not_imp").setAttribute("onclick", "")
    document.getElementById("not_imp2").setAttribute("onclick", "imp2()")
    // document.getElementById("images").innerHTML="<img style='margin: 0;position: absolute;top: 60%;left: 50%;-ms-transform: translate(-60%, -50%);transform: translate(-60%, -50%);' src='./amg.png' onclick='console.log()'"
}