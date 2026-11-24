# Assurances

## About

**Assurances** is a simple web app that plays audio files at the press of a button.
It is called **Assurances** because it was created to share short
verbal affirmations with someone you love. Just record yourself speaking,
drop the audio files in the appropriate folder, and your special someone can
hear your voice whenever they need a little reassurance.

**Assurances** does not include its own authentication system. If you want to keep
your implementation private, you will need to implement one. This implementation
of **Assurances** is secured using mTLS. Only the intended recipient can access the live app.
Anyone without an authorized certificate lands on this page instead.
For more on setting up mTLS, I recommend [Mastering Mutual TLS (mTLS) with Nginx: A Deep Dive][mtls]
by José Manuel Requena Plens. It was the guide that finally helped me get mTLS up
and running after weeks of struggling to get it to work right.

**Assurances** was lovingly written by hand, by a human, on the ancestral land
of the Susquehannock people. It is made using CSS, [Flask][flask], HTML, and
Javascript in Panic's [Nova text editor][nova].

## Implementation

More information coming soon!

## Links
- A creation of [232 Software][232]
- Made by [Timothy Rezendes][info]

<a href="https://oql.avris.it/license/v1.4" target="_blank" rel="noopener"><img src="https://badgers.space/badge/License/OQL/pink" alt="License: OQL" style="vertical-align: middle;"/></a>
  
  
[mtls]: https://jmrp.io/blog/001-secure-nginx-client-certificates/ "Mastering Mutual TLS (mTLS) with Nginx: A Deep Dive | JMRP"
[flask]: https://flask.palletsprojects.com/en/stable/ "Welcome to Flask — Flask Documentation (3.1.x)" 
[nova]: https://nova.app "Panic - Nova"
[232]: https://232.software "232 Software"
[info]: https://timothy.rezendes.info "Timothy Rezendes | Master of Data"
