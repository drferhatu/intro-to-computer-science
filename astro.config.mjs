// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';
import tailwindcss from '@tailwindcss/vite';
import remarkCallouts from './src/lib/remark-callouts.mjs';
import rehypeBaseLinks from './src/lib/rehype-base-links.mjs';

// GitHub Pages: https://drferhatu.github.io/intro-to-computer-science/
// For a custom domain, build with SITE_URL and BASE_PATH=/ environment variables.
const site = process.env.SITE_URL ?? 'https://drferhatu.github.io';
const base = process.env.BASE_PATH ?? '/intro-to-computer-science';

export default defineConfig({
  site,
  base,
  trailingSlash: 'ignore',
  // Inline CSS into each page: GitHub Pages caches HTML for ~10 minutes, and a cached page pointing at a
  // renamed (hashed) stylesheet would otherwise render unstyled right after every deploy.
  build: { inlineStylesheets: 'always' },
  integrations: [mdx(), sitemap()],
  markdown: {
    remarkPlugins: [remarkCallouts],
    rehypePlugins: [[rehypeBaseLinks, { base }]],
    shikiConfig: { themes: { light: 'github-light', dark: 'github-dark' }, wrap: true },
  },
  vite: { plugins: [tailwindcss()] },
});
