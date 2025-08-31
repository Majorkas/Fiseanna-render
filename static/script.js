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
const SMALL_PRINT = 6
const MEDIUM_PRINT = 8
const LARGE_PRINT = 12
const XLARGE_PRINT = 16
const WITH_FRAME = 9.99
const NO_FRAME = 0
const IMG_ID_SRC = {
  'Main-img': "static/images/lake.jpg",
  'smaller-img1': "static/images/black-castle.jpg",
  'smaller-img2': "static/images/faces.jpg",
  'smaller-img3': "static/images/rock.jpg",
  'smaller-img4': "static/images/bike.jpeg",
}

function redirect() {
  window.location = "/success";
}

function imgSwap(imgSrc) {
  mainImg.src = imgSrc;


}
function imgSwapBack() {
  mainImg.src = "static/images/lake.jpg"

}
let count = 6;
function redirectPage() {
  count--;
  document.getElementById('countDown').innerHTML = count;
  if (count == 0) {
    window.location = "/";
  }
}

function shippingCalcultor(selectedAddress) {
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
  menuButton[0].addEventListener('click', () => {
    mainNav.classList.toggle('hidden');
    mottoTxt.classList.toggle('hidden');
  });
  COST_CALCULATOR.addEventListener('submit', runFullCalculation)
  runFullCalculation();
}

function initIndex() {
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

function initStore() {
 menuButton[0].addEventListener('click', () => {
    mainNav.classList.toggle('hidden');
    mottoTxt.classList.toggle('hidden');
 });
  shippingCalcultor(address)
  document.getElementById('shipping-calculator').addEventListener('change', () => shippingCalcultor(address))
}

function initRedirect() {
  setInterval(redirectPage, 1000)
}
