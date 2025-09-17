const menuButton = document.getElementsByClassName('menu-button')
const mainNav = document.getElementById('main-nav')
const mottoTxt = document.getElementById('motto-text')
const COST_CALCULATOR = document.getElementById('item-choice')
const shipToIreland = 4.99
const shipToUK = 8.99
const shipToEurope = 5.50
const shipToWorld = 9.99
const importFees = 0.2
const address = document.getElementById('shipping-location')
const mainImg = document.getElementById('Main-img');
const SMALL_PRINT = 13
const MEDIUM_PRINT = 17
const LARGE_PRINT = 21
const XLARGE_PRINT = 25
const WITH_FRAME = 20
const NO_FRAME = 0
const IMG_ID_SRC = {
  'Main-img': "static/images/lake.jpg",
  'smaller-img1': "static/images/black-castle.jpg",
  'smaller-img2': "static/images/faces.jpg",
  'smaller-img3': "static/images/rock.jpg",
  'smaller-img4': "static/images/bike.jpeg",
}

function imgSwap(imgSrc) {
  mainImg.src = imgSrc;


}
function imgSwapBack() {
  mainImg.src = "static/images/lake.jpg"

}
let count = 6;
function redirectPage() {
  // countdown for the redirect that once it hits 0 redirects the page back to '/'
  count--;
  document.getElementById('countDown').innerHTML = count;
  if (count == 0) {
    window.location = "/";
  }
}
function redirectPageAccountCreation() {
  // countdown for the redirect that once it hits 0 redirects the page back to '/'
  count--;
  document.getElementById('countDown').innerHTML = count;
  if (count == 0) {
    window.location = "/store";
  }
}

function shippingCalcultor(selectedAddress) {

  // function takes the selection from the drop down and then outputs a price to a span dependant on the selection
  document.getElementById('drop-selection').innerText = selectedAddress.options[address.selectedIndex].text;
  let selection = selectedAddress.value
  console.log(selection)
    if (selection === "1") {
      document.getElementById('calculator-output').innerText = shipToIreland.toFixed(2);
    } else if (selection === "2") {
      document.getElementById('calculator-output').innerText = shipToUK + ' with Import Fees the total will be ' + '€' +((shipToUK * importFees)+shipToUK).toFixed(2);
    } else if (selection === "3") {
      document.getElementById('calculator-output').innerText = shipToEurope.toFixed(2);
    } else if (selection === "4") {
      document.getElementById('calculator-output').innerText = shipToWorld + ' with Import Fees the total will be ' + '€' + ((shipToWorld * importFees)+shipToWorld).toFixed(2);
    }
}

function runFullCalculation(event) {

  // The final calculation for the store item using all the helper functions and calculates the cost to then finally output the price to the span //
  if (event) {
    event.preventDefault();
  }

  const sizeSelection = document.getElementById('print-size').options[document.getElementById('print-size').selectedIndex].text;
  const addFrame = document.getElementById('check').checked;

  const printPrice = printPriceF(sizeSelection);
  const framePrice = framePriceF(addFrame);

  const finalPrice = (printPrice + framePrice)
  outputToSpan('item-price', finalPrice.toFixed(2))
}
function outputToSpan(spanId, value) {
  document.getElementById(spanId).innerText = "€" + value;
}


function printPriceF(sizeSelection) {
  // checks the selection from the drop down and returns appropriate price
  if (sizeSelection === '11"x17"') {
    return SMALL_PRINT;
  } else if (sizeSelection === '18"x24"' ) {
    return MEDIUM_PRINT;
  } else if (sizeSelection === '24"x36"') {
    return LARGE_PRINT;
  } else if (sizeSelection === '27"x40"') {
    return XLARGE_PRINT;
  }
}

function framePriceF(addFrame) {
  //takes the check of if the checkbox is checked as an input and returns the correct img src and alt
  const FRAME_PIC = document.getElementById('framed-img').src
  const FRAME_PIC_ALT = document.getElementById('framed-img').alt
  const NO_FRAME_PIC = document.getElementById('no-frame').src
  const NO_FRAME_PIC_ALT = document.getElementById('no-frame').alt
  const FRAME = addFrame ? WITH_FRAME : NO_FRAME;
  document.getElementById('main-display').src = addFrame ? FRAME_PIC : NO_FRAME_PIC;
  document.getElementById('main-display').alt = addFrame ? FRAME_PIC_ALT : NO_FRAME_PIC_ALT
  return FRAME;
}

function storeItemInit() {
  //init function to add event listeners

  menuButton[0].addEventListener('click', () => {
    mainNav.classList.toggle('hidden');
    mottoTxt.classList.toggle('hidden');
  });
  COST_CALCULATOR.addEventListener('submit', runFullCalculation)
  runFullCalculation();
}

function initIndex() {
  //init function to add event listeners
  menuButton[0].addEventListener('click', () => {
    mainNav.classList.toggle('hidden');
    mottoTxt.classList.toggle('hidden');

  });

  Object.entries(IMG_ID_SRC).forEach(([imgId, imgSrc]) => {
    const imgElem = document.getElementById(imgId);
    imgElem.addEventListener("mouseover", () => imgSwap(imgSrc) );
    imgElem.addEventListener("mouseout", imgSwapBack);
    imgElem.addEventListener("touchstart", () => imgSwap(imgSrc) );
    imgElem.addEventListener("touchcancel", imgSwapBack);
  });
}
function initAccount() {
  menuButton[0].addEventListener('click', () => {
    mainNav.classList.toggle('hidden');
    mottoTxt.classList.toggle('hidden');
  });

  }

function initStore() {
  //init function to add event listeners
 menuButton[0].addEventListener('click', () => {
    mainNav.classList.toggle('hidden');
    mottoTxt.classList.toggle('hidden');
 });
  shippingCalcultor(address)
  document.getElementById('shipping-calculator').addEventListener('change', () => shippingCalcultor(address))
}

function initRedirect() {
  //runs the redirect function
  setInterval(redirectPage, 1000)
}
function initRedirectAccountCreation() {
  //runs the redirect function
  setInterval(redirectPageAccountCreation, 1000)
}
