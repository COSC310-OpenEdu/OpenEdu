document.addEventListener("DOMContentLoaded", function() {
    
    var currentTime = new Date();
    var assignments = document.getElementsByClassName("assign");
    for (let i = 0; i < assignments.length; i++) {
        let assignment = assignments[i];
        let assignmentDate = new Date(assignment.querySelector(":last-child").id.replace(" ", "T"));
        console.log(assignmentDate);
        if (currentTime >= assignmentDate) {
            
            assignment.classList.add("grey");
            assignment.querySelector(":nth-last-child(2)").innerHTML = "Past Due";
        }
    }

});