# Meditation Online

This is the source code for [meditationonline.org](https://www.meditationonline.org/), hosted through GitHub Pages.

## Deploying an Update

The site is deployed from the `gh-pages` branch, which is currently updated manually.

To update that branch, run `make build`, which creates the `build/` directory.
Switch to the `gh-pages` branch and overwrite the files with the contents of `build/`.
