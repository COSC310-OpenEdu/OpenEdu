document.addEventListener("DOMContentLoaded", function() {
    // Create variables
    let groups = document.getElementsByClassName("grade");
    let assignmentButton = groups[0].children[0];
   
    let buttons = [];
    let toggle = true;
    
    // Adds hide class to each gradeItem
    for (let i = 0; i < groups.length; i++) {
        buttons.push(groups[i].children[0]);
        for (let j = 1; j < groups[i].children.length; j++) {
            groups[i].children[j].classList.add("hide");
        }
    }
    
    // When element is clicked, sets distance a variable for animation and unhides/hides gradeItems
    function click(index) {
        for (let i = 1; i < groups[index].children.length; i++) {
            let t = i*-3.3 + "";
            t += "em";
            groups[index].children[i].style.setProperty("--slide", t);
            toggle = groups[index].children[i].classList.toggle("hide");
            
        }
    }
    // Creates onClick listeners for each gradeGroup
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", function() {
            click(i);
        });
    }
});