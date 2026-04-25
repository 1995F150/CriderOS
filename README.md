# CriderOS

A custom Arch-based Linux distribution for the CriderGPT ecosystem.
Built for daily driving on x86_64 desktops, with planned editions for Raspberry Pi and a browser-based shell.

> **Status:** v0.1 "Seedling" — bootable live ISO with KDE Plasma + CriderOS branding.

---

## Quick build (Docker, any host)

You don't need Arch installed. The build runs inside an official Arch container.

```bash
git clone https://github.com/<your-org>/crideros.git
cd crideros
./scripts/build-iso.sh
```

When it finishes you'll have:

```
out/crideros-0.1-x86_64.iso
out/crideros-0.1-x86_64.iso.sha256
```

Flash it to a USB stick:

```bash
sudo dd if=out/crideros-0.1-x86_64.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

…or boot it in QEMU to test:

```bash
qemu-system-x86_64 -enable-kvm -m 4G -cdrom out/crideros-0.1-x86_64.iso
```

---

## What's in v0.1

- Arch base + `linux-zen` kernel (great for Ryzen + RX 580)
- KDE Plasma 6 desktop (Wayland, X11 fallback)
- AMD GPU firmware, NetworkManager, PipeWire, Bluetooth
- Firefox, Konsole, Dolphin, Kate
- CriderOS branding: GRUB splash, SDDM theme, wallpaper, Plasma color scheme
- Live user `crider` (passwordless sudo) for testing
- Calamares installer pre-wired for Phase 2

## Roadmap

See [`CriderOS_Roadmap.pdf`](./docs/CriderOS_Roadmap.pdf).

| Version | Codename | Phase |
| --- | --- | --- |
| 0.1 | Seedling | Bootable live ISO (this release) |
| 0.2 | Pasture | Calamares installer working |
| 0.3 | Herd | CriderGPT app + Docker stack baked in |
| 0.4 | Barn | NFC reader + label printer presets |
| 1.0 | Homestead | Public launch, signed ISOs |

## Repo layout

```
archiso/        # archiso profile (the actual ISO recipe)
branding/       # logo, wallpaper, color schemes, SDDM theme
scripts/        # build helpers
.github/        # nightly build workflow
docs/           # roadmap, install guide
```

## License

GPLv3 for the distro recipe. Branding assets © Jessie Crider.
