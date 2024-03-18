const buttonTemplate = document.createElement('template');

buttonTemplate.innerHTML = `
    <style>
        button {
            width: fit-content;
            height: 46px;
            display: flex;
            flex-direction: row;
            background-color: #F8F8F8;
            border-radius: 8px;
            padding: 10px 16px 10px 16px;
            border: 1px #8C8C8C solid;
            justify-content: center;
            align-items: center;
            gap: 10px;
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

        button:hover {
          background-color: #B4CBC9;
        }
    </style>
    <button>
        <span class="material-symbols-outlined"><slot name="button-icon">upload</slot></span>
        <span><slot name="button-text">Upload File</slot></span>
    </button>
`

class Button extends HTMLElement {
    constructor() {
      super();
    }
  
    connectedCallback() {
      const shadowRoot = this.attachShadow({ mode: 'open' });
      shadowRoot.appendChild(buttonTemplate.content.cloneNode(true));
    }
  }
  
  customElements.define('button-component', Button);
  