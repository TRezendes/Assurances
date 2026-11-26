# Assurances

## About

**Assurances** is a simple web app that plays audio files at the press of a button.
It is called **Assurances** because it was created to share short
verbal affirmations with someone you love. Just record yourself speaking,
drop the audio files in the appropriate folder, and your special someone can
hear your voice whenever they need a little reassurance.

**Assurances** was lovingly written by hand, by a human, on the ancestral land
of the Susquehannock people. It is made using CSS, [Flask][flask], HTML, and
Javascript in Panic's [Nova text editor][nova].

## Implementation

### Flask & Audio

**Assurances** uses [Flask][flask] primarily to load audio files. Each time the page is loaded, Flask checks the folders and creates a list of file names for each folder. One file from each list is then selected at random and preloaded using Javascript. Each time one of the buttons is clicked, the preloaded file is played, and another file is selected and preloaded. Audio placed in `assurances_app/static/audio/mild` is played using the &ldquo;Click Here&rdquo; button. Audio placed in `assurances_app/static/audio/spicy` is played using the &ldquo;Click Here 🌶️&rdquo; button.

### CSS

The design of **Assurances** is targeted at two very specific devices. This app was designed for my wife, so it is aimed at supporting her specific iPhone (16e) and her specific iPad (Air 3rd Gen). I am sure it will work fine in many other
browsers/&ZeroWidthSpace;devices, but, with the exception of Safari on macOS, they haven't been considered or tested.

The CSS for **Assurances** has a media `(prefers-color-scheme: dark)` media query that triggers not only dark mode, but also &ldquo;After Dark Mode&ldquo;, which reveals the spicy button.

### Authentication

If you're sharing spicy audio with someone special, you'll probably want to keep your implementation of **Assurances** private. **Assurances** does not include its own authentication system. My own implementation is secured using mTLS. Only the intended recipient can access the live app. Anyone without an authorized certificate lands on the [&ldquo;Get Assurances&rdquo;][get] page. For more on setting up mTLS, I recommend [Mastering Mutual TLS (mTLS) with Nginx: A Deep Dive][mtls] by José Manuel Requena Plens. It was the guide that finally helped me get mTLS up and running after weeks of struggling to get it to work right.

## Links
- A creation of [232 Software][232]
- Made by [Timothy Rezendes][info]

<a href="https://oql.avris.it/license/v1.4" target="_blank" rel="noopener"><img src="https://badgers.space/badge/License/OQL/pink" alt="License: OQL" style="vertical-align: middle;"/></a>
  
  
[232]: https://232.software "232 Software"
[flask]: https://flask.palletsprojects.com/en/stable/ "Welcome to Flask — Flask Documentation (3.1.x)" 
[get]: https://assurances.rezendes.info/get-assurances.html "Assurances: For When You Need a Little Reassurance"
[info]: https://timothy.rezendes.info "Timothy Rezendes | Master of Data"
[mtls]: https://jmrp.io/blog/001-secure-nginx-client-certificates/ "Mastering Mutual TLS (mTLS) with Nginx: A Deep Dive | JMRP"
[nova]: https://nova.app "Panic - Nova"
