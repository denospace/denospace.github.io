---
title: Self-hosting
section: Integrations
order: 1
blurb: Running Denospace yourself, with Syncthing or without.
---

# Self-hosting

Denospace is MIT licensed and self-hosting is a first-class path, not a grudging one. Everything the hosted service will do, a self-hosted instance does.

## Running it

Build it, point it at a directory, put a reverse proxy in front for TLS:

```
denospace --space /home/you/org
```

It binds `127.0.0.1:27438` by default and does not listen publicly on its own. Configuration lives in an environment file; authentication is a username and password you set there.

Build requirements are Node and a Rust toolchain. A release build embeds the client, so a change to the TypeScript still needs the Rust step to reach what is served.

## Syncthing

The arrangement the author runs: a folder on the laptop, a folder on the server, kept in step by [Syncthing](https://syncthing.net/). No account, no third party, nothing billed.

Exclude Emacs's scratch files at the sync layer with a `.stignore` in the folder:

```
*~
#*#
.#*
.git
```

Keep conflict copies **synced** rather than ignored, so you can see them — then hide them from the page picker with the space's ignore setting instead. A conflict you cannot see is worse than one cluttering a list.

## Service management

There is no systemd on every host. A supervisor of some kind, or a cron `@reboot` entry plus a periodic liveness check, is enough. The binary is a single process.

## Browser caching

Denospace is a progressive web app and registers a service worker, which answers before the network does. After deploying a new build, a browser will keep serving the old client and a hard reload will not dislodge it — you have to unregister the service worker or clear the site's data.

This catches everyone once. If a new feature does not appear after a deploy, check this before you check the deploy.
