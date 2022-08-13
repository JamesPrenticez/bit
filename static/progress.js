// function progressTest(){
//  let progressBar = document.getElementById("progressBar")
//  let progressText = document.getElementById("progressText")

//  console.log(progressBar)

//  let percentage = 95

//  progressBar.style.width = percentage + "%"
//  progressText.innerText = percentage + "%"

//  set
// }

function progressTest(){
 let progressBar = document.getElementById("progressBar")
 let progressText = document.getElementById("progressText")
 let counter = 10
 
 let loop = setInterval(function(){
   
  progressBar.style.width = counter + "%"
  progressText.innerText = counter + "%"
  console.log(counter)

  counter++

  if (counter === 100) {
    progressBar.style.width = counter + "%"
    progressText.innerText = counter + "%"
    console.log("Download complete!")
    clearInterval(loop)
  }
 }, 100)
}

