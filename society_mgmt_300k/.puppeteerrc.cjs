/**
 * Puppeteer configuration for the documentation diagram pipeline (`npm run docs:diagram`).
 *
 * Security remediation (QA finding F-1 — outdated bundled Chromium):
 *   `@mermaid-js/mermaid-cli@11.16.0` (pinned exactly by the AAP §0.6.1) resolves the
 *   transitive `puppeteer@24.43.1`, which bundles Chromium `148.0.7778.97` — a build
 *   behind the patched `148.0.7778.167` release. The AAP freezes the tooling versions,
 *   so bumping the toolchain to pull a newer Chromium is out of scope. Instead, this
 *   config removes the outdated browser from the pipeline entirely:
 *
 *     1. `skipDownload: true` stops puppeteer's install step from fetching the outdated
 *        bundled Chromium at all (puppeteer reads this via cosmiconfig, so `npm install`
 *        no longer downloads `148.0.7778.97`).
 *     2. `executablePath` points mermaid-cli/puppeteer at the patched, up-to-date
 *        system Chrome/Chromium instead, so every diagram render uses a maintained
 *        browser rather than the outdated bundled one.
 *
 * puppeteer honours `executablePath` from this file at launch time (verified: an invalid
 * path makes the render fail fast rather than silently falling back), and setting it also
 * implies `skipDownload`. If no system browser is present the field is omitted so puppeteer
 * degrades gracefully to its default resolution rather than launching an invalid path.
 *
 * This file is documentation-tooling configuration only — it introduces no runtime
 * dependency and touches no code under `src/**` or `tests/**`.
 */
'use strict';

const fs = require('node:fs');

// Candidate locations for a maintained (patched) system browser, most specific first.
// An explicit PUPPETEER_EXECUTABLE_PATH override wins when provided by the environment.
const candidatePaths = [
  process.env.PUPPETEER_EXECUTABLE_PATH,
  '/usr/bin/google-chrome-stable',
  '/usr/bin/google-chrome',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
  '/snap/bin/chromium',
].filter(Boolean);

const executablePath = candidatePaths.find((candidate) => {
  try {
    return fs.existsSync(candidate);
  } catch {
    return false;
  }
});

/** @type {import('puppeteer').Configuration} */
module.exports = {
  // Never download the AAP-pinned, outdated bundled Chromium (QA F-1).
  skipDownload: true,
  // Render diagrams with the patched system browser when one is available.
  ...(executablePath ? { executablePath } : {}),
};
