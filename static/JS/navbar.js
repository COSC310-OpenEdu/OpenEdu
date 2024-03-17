/*
Creates a template/web component for the navbar that can be used across all pages
to avoid lengthy code in the html files

Usage:

Insert the following into the HTML <head> tag:
<script src="{{ url_for('static', filename='js/navbar.js')}}" type="text/javascript" defer></script>

Insert the following into the HTML <body> tag for the navbar:
<navbar-component></navbar-component>

To change the icon and text from logout to login:
<navbar-component>
    <span slot="log-icon">login</span>
    <span slot="log-text">Login</span>
</navbar-component>
*/
const navbarTemplate = document.createElement('template');

navbarTemplate.innerHTML = `
  <style>
    body {
      font-family: 'Roboto', sans-serif;
    }

    /* Navbar flex container */
    nav {
      background-color: #B4CBC9;
      display: flex;
      flex-direction: column;
      height: 100vh;
      width: 80px;
      justify-content: space-between;
    }

    /* Navigation menu links */
    nav a {
      text-decoration: none;
      color: black;
      display: flex;
      flex-direction: column;
      width: 80px;
      height: 48px;
      text-align: center;
      justify-content: center;
      padding-top: 12px;
      padding-bottom: 12px;
    }

    /* Current navigation menu link */
    nav a.active {
      background-color: white;
    }

    /* Navigation menu links on hover */
    nav a:hover:not(.active) {
      background-color: #99B0AE;
      color: white;
    }

    /* Top navigation menu */
    .top {
      display: flex;
      flex-direction: column;
    }

    /* Bottom navigation menu */
    .bottom {
      display: flex;
      flex-direction: column;
    }

    /* Google material symbol icons */
    .material-symbols-outlined {
      font-family: 'Material Symbols Outlined';
      font-weight: normal;
      font-style: normal;
      font-size: 24px;  /* Preferred icon size */
      display: inline-block;
      line-height: 1;
      text-transform: none;
      letter-spacing: normal;
      word-wrap: normal;
      white-space: nowrap;
      direction: ltr;
    }

    /* Larger icon sizing */
    span.size-36 {
      font-size: 36px;
      font-variation-settings: 'OPSZ' 36;
    }
  </style>
  <nav>
    <div class="top">
      <a href="#" id="Logo"><span class="material-symbols-outlined size-36">school</span></a>
      <a href="#" id="Account" class=""><span class="material-symbols-outlined">account_circle</span>Account</a>
      <a href="#" id="Home" class=""><span class="material-symbols-outlined">home</span>Home</a>
      <a href="#" id="Courses" class=""><span class="material-symbols-outlined">library_books</span>Courses</a>
      <a href="#" id="Search" class=""><span class="material-symbols-outlined">search</span>Search</a>
    </div>
    <div class="bottom">
      <a href="#" id="Log" class="">
        <span class="material-symbols-outlined"><slot name="log-icon">logout</slot></span>
        <slot name="log-text">Logout</slot>
      </a>
    </div>
  </nav>
`;

class Navbar extends HTMLElement {
  constructor() {
    super();
  }

  connectedCallback() {
    const shadowRoot = this.attachShadow({ mode: 'open' });
    shadowRoot.appendChild(navbarTemplate.content);

    // Highlight the active navbar menu item based on current page
    if (window.location.pathname == '/teacher/dashboard') {
      this.shadowRoot.getElementById("Home").classList.add("active");
    } else if (window.location.pathname == '/teacher/courseName/dashboard') {
      this.shadowRoot.getElementById("Courses").classList.add("active");
    }
  }
}

customElements.define('navbar-component', Navbar);
