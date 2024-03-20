const courseCardTemplate = document.createElement('template');

courseCardTemplate.innerHTML = `
<style>
    .course-container {
        display: flex;
        flex-direction: column;
        width: 260px;
        height: 260px;
        border-radius: 24px;
        background-color: white;
    }
    
    .colorCard {
        border-top-left-radius: inherit;
        border-top-right-radius: inherit;
        height: 70%;
    }

    .course-info {
        height: 30%;
        display: flex;
        flex-direction: column;
        padding: 10px;
    }

    .course-info p {
        text-decoration: none;
        margin: 0 0 8px 0;
    }

    .col1 { background-color: #CEECC0}
    .col2 { background-color: #ECE4C0}
    .col3 { background-color: #FFDAD6}
    .col4 { background-color: #C0DCEC}
</style>

    <div class="course-container">
        <div class="colorCard" id="colorCard"></div>
        <div class="course-info">
            <p><slot name="courseId"></slot></p>
            <p><slot name="courseName"></slot></p>
        </div>
    </div>
`;

class CourseCard extends HTMLElement {
    constructor() {

        super();
    }

    connectedCallback() {
        const shadowRoot = this.attachShadow({ mode: 'open' });
        shadowRoot.appendChild(courseCardTemplate.content.cloneNode(true));
        this.shadowRoot.getElementById('colorCard').id = courseList[0] + 'color';
        courseList.splice(0,1);
        if (this.shadowRoot.getElementById("COSC303color")) {
            this.shadowRoot.getElementById("COSC303color").classList.add("col1");
        }
        if (this.shadowRoot.getElementById("COSC310color")) {
            this.shadowRoot.getElementById("COSC310color").classList.add("col2");
        }
        if (this.shadowRoot.getElementById("COSC304color")) {
            this.shadowRoot.getElementById("COSC304color").classList.add("col3");
        }
        if (this.shadowRoot.getElementById("COSC404color")) {
            this.shadowRoot.getElementById("COSC404color").classList.add("col4");
        }
    }
}

customElements.define('course-card-component', CourseCard);
