// Renders every src/*.html banner to export/<name>.png at its exact size.
// Run: docker run --rm -v "$PWD":/w -w /app --entrypoint node ghcr.io/jun101/personalwebsite-web:latest /w/render.mjs
import { createRequire } from 'node:module';
import { readdirSync } from 'node:fs';

// puppeteer-core ships inside the website's web image under /app.
const puppeteer = createRequire('/app/package.json')('puppeteer-core');

const SIZES = { x: [1500, 500], li: [1584, 396], fb: [1640, 624] };
const browser = await puppeteer.launch({
  executablePath: '/usr/bin/chromium-browser',
  args: ['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage', '--hide-scrollbars'],
});
const page = await browser.newPage();
for (const file of readdirSync('/w/src').filter((f) => f.endsWith('.html'))) {
  const name = file.replace('.html', '');
  const [width, height] = SIZES[name.split('-')[1]];
  await page.setViewport({ width, height, deviceScaleFactor: 1 });
  await page.goto(`file:///w/src/${file}`, { waitUntil: 'networkidle0' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: `/w/export/${name}.png`, clip: { x: 0, y: 0, width, height } });
  console.log('rendered', name, width, height);
}
await browser.close();
