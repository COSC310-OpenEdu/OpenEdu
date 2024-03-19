/*
Creates a template/web component for the page body that can be used across all pages
to avoid lengthy code in the html files

Usage:

Insert the following into the HTML <head> tag:
<script src="{{ url_for('static', filename='js/pageBody.js')}}" type="text/javascript" defer></script>

Insert the following into the HTML <body> tag:
<body-component></body-component>
*/
const bodyTemplate = document.createElement('template');

bodyTemplate.innerHTML = `
  <style>
    .page-container {
        display: flex;
        flex-direction: column;
        padding: 36px;
        width: Calc(100vw - 152px);
        height: Calc(100vh - 72px);
        overflow: hidden;
    }
    
    .container {
        display: flex;
        flex-direction: column;
        border-radius: 24px;
        background-color: #F8F8F8;
        flex-grow: 1;
        overflow: hidden;
    }

    .header {
        background-color: #B4CBC9;
        height: fit-content;
        border-top-left-radius: inherit;
        border-top-right-radius: inherit;
        padding: 36px;
        align-items: center;
        font-size: 24px;
        font-family: Roboto, sans-serif;
        font-weight: 700;
        position: sticky;
        overflow: hidden;
    }

    .container-body {
        font-family: Roboto, sans-serif;
        display: flex;
        flex-direction: row;
        flex: 1;
        padding: 60px;
        gap: 36px;
        overflow: auto;
    }

    .overflow {
        display: flex;
        flex-wrap: wrap;
    }

  </style>

    <div class="page-container">
        <div class="container">
            <div class="header"><slot name="header">Header</slot></div>
            <div><slot name="secondHeader"></slot></div>
            <div class="container-body" id="container-body">
                    <slot name="contents"></slot>

            </div>
        </div>
    </div>
`
class PageBody extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        const shadowRoot = this.attachShadow({ mode: 'open' });
        shadowRoot.appendChild(bodyTemplate.content.cloneNode(true));

        if (window.location.pathname == '/teacher/dashboard') {
            this.shadowRoot.getElementById('container-body').classList.add("overflow");
        }
    }
}

customElements.define('body-component', PageBody);