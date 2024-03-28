document.addEventListener("DOMContentLoaded", function() {
    var questions = document.getElementsByClassName("avg");
    var questions2 = document.getElementsByClassName("avg2");
    average();

    function average() {
        for (let i = 0; i < questions.length; i++) {
            let grades = document.getElementsByClassName(questions[i].id);
            let avg = 0;
            for (let j = 0; j < grades.length; j++) {
                avg += parseFloat(grades[j].value);
            }
            questions[i].innerHTML = "Average: "+ (avg/grades.length) + "%";
            questions2[i].innerHTML = "Average: "+ (avg/grades.length);
        }
    }

    var inputs = $("input");
    inputs.on("blur", function() {
        let qId = this.id[0];
        let aId = this.id[1];
        let sId = this.id[2];
        const url = "{{ url_for('updateGrade')|tojson }}";
        fetch(url);
        //$.post("{{url_for('updateGrade')}}", {courseId:1, questionId:qId, assignmentId:aId, studentId:sId});
    });

});