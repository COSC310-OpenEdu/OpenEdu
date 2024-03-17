/*
Creates a template/web component for the secondary header that can be used across all course pages
to avoid lengthy code in the html files

Usage:

Insert the following into the HTML <head> tag:
<script src="{{ url_for('static', filename='js/courseHeader.js')}}" type="text/javascript" defer></script>

Insert the following into the HTML <body> tag for the navbar:
<header-component></header-component>
*/
const headerTemplate = document.createElement('template');

headerTemplate.innerHTML = `
    <style>
    /* Header flex container */
    header {
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        border-bottom: 1px #8C8C8C solid;
        padding: 0 36px 0 36px;
        gap: 18px;
    }

    /* Header menu links */
    header a {
        text-decoration: none;
        color: black;
        display: flex;
        text-align: center;
        justify-content: center;
        padding: 18px 36px 18px 36px;
        border-bottom: 12px solid rgb(0 0 0 / 0%);
    }

    /* Current header menu link */
    header a.active {
        border-bottom: 12px #B4CBC9 solid;
    }

    /* Header menu links on hover */
    header a:hover:not(.active) {
        border-bottom: 12px #99B0AE solid;
    }
    </style>
    <header>
        <a href="dashboard.html" id="Dashboard">
            <slot name="dashboard">Dashboard</slot>
        </a>
        <a href="#" id="Assignments">
            <slot name="assignments">Assignments</slot>
        </a>
        <a href="#" id="Grading">
            <slot name="grading">Grading</slot>
        </a>
        <a href="#" id="People">
            <slot name="people">People</slot>
        </a>
    </header>
`;

class CourseHeader extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        const shadowRoot = this.attachShadow({ mode: 'open' });
        shadowRoot.appendChild(headerTemplate.content);

        // Highlight the active header menu item based on current page
        if (window.location.pathname == "/teacher/courseName/dashboard") {
            this.shadowRoot.getElementById("Dashboard").classList.add("active");
        }
    }
}

customElements.define('header-component', CourseHeader);
