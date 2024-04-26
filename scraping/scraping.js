// Purpose：The goal of this program is to extract article title and URL by scraping.
// Author：@hal40n

'use strict';
// import any modules
const puppeteer = require('puppeteer');

//start work flow
(async() => {
  // Launch browser
  const browser = await puppeteer.launch({
    headless: false, //headless off
    slowMo: 50 // moving slowly
  });

  // Launch a new page
  const page = await browser.newPage();

  try {
    // Access to Google
    await page.goto('https://google.com/');

    // Query for an element handle

    // Search by entering values in the search form
    // after entering, press enter button
    await page.type('.a4bIc', 'AWS 導入事例');
    await page.keyboard.press('Enter');

    // Get title and link list of search results
    await page.waitForSelector(".LC20lb", {visible: true});
    const searchResults = await page.evaluate(() =>
      [...document.querySelectorAll(".LC20lb")].map(e => ({
        title: e.innerText,
        link: e.parentNode.href
      }))
    );
    console.log(searchResults);

  } catch(err) {
    console.log('Error!')
  } finally {
    // Close browser
    await browser.close();
  }
})();