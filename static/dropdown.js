customElements.define('search-dropdown',
  class extends HTMLElement {
    constructor() {
      super();
      const template = document.getElementById('dropdown-template').content
      
      const shadowRoot = this.attachShadow({mode: 'open'})
      
      shadowRoot.appendChild(template.cloneNode(true))
    }
  }
)

function toggle(self){
  let dropdown_items = self.children[2].style.display 
  
  self.style.outline = 'solid 2px #007BFF'
  self.children[1].style.transform='rotate(0deg)'
  self.children[2].style.display = 'block'
  
  if(dropdown_items == 'block'){
    self.style.outline = 'solid 2px transparent'
    self.children[1].style.transform='rotate(90deg)'
    self.children[2].style.display = 'none'
  }
}

function closeDropdown(self){
  self.style.outline = 'solid 2px transparent'
  self.children[1].style.transform='rotate(90deg)'
  self.children[2].style.display = 'none'
}

function handleKeyUp(self, e){
  // console.log(self.parentNode) 
  // console.log(self.innerText) 
  // console.log(e) 

  switch(e.key){
    case "ArrowUp":
      handleArrowUp(self)
      break
    case "ArrowDown":
      handleArrowDown(self)
      break
    case "Escape":
      handleEscape(self)
      break
    default:
      search(self)
    }
}

function handleArrowUp(self){
  console.log("up", self)
}

function handleArrowDown(self){
  console.log("down", self)
}

function handleEscape(self){
  console.log("esc", self)
}

function search(self){
  let searchTerm = self.innerText
  let list = self.parentNode.children[2].children['dropdown-items'].assignedNodes()
  let listCopy = Array.from(list[0].children)

  for(i=0; i <= listCopy.length -1; i++){
    if(searchTerm == listCopy[i].innerText) console.log("Match")
  }
}

// let x = self.parentNode.children[2].children['dropdown-items'].assignedNodes()
// let y = itemList[0].children

  // const template = document.getElementById('dropdown-template').content
  // let itemList = template.querySelectorAll("div")
  // console.log(itemList)
  
  // let itemList = self.parentNode.children[2].children['dropdown-items'].assignedNodes()
  // console.log(itemList[0].children.innerText)

  // let fuck = document.getElementById('dropdown-items')
  // console.log(fuck)