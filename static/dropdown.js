customElements.define('search-dropdown',
  class extends HTMLElement {
    constructor() {
      super();
      const template = document.getElementById('dropdown-template').content
      
      const shadowRoot = this.attachShadow({mode: 'open'})
      
      shadowRoot.appendChild(template.cloneNode(true))

      template.addEventListener('mousemove', (e) => {
        console.log("here")
        console.log(e.offsetX, e.offsetY)
      })
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
https://stackoverflow.com/questions/152975/how-do-i-detect-a-click-outside-an-element
function closeDropdown(self){
  //if !element.contains(event.target)
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
    // case "Escape":
    //   handleEscape(self)
    //   break
    // case "Enter":
    //   console.log(e)
    //   select(self, e)
    //   break
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
  let listRef = list[0].children

  //console.log(listRef[0].innerText)

  for(i=0; i <= listRef.length -1; i++){
    if(searchTerm == listRef[i].innerText){
      console.log("Match")
      listRef[i].style.backgroundColor = "green"
    }
  }
}

function select(self, event){
  let inputBox = self.parentNode.children[0]
  let selection = event.target
  inputBox.innerText = selection.innerText
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