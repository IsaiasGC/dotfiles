Note: Based on [antoniosarosi -> dotfiles](https://github.com/antoniosarosi/dotfiles)

# Overview

This guide will walk you through the process of building a desktop environment
starting with a fresh Arch based installation. I will assume that you are
comfortable with Linux based operating systems and command line interfaces.
Because you are reading this, I will also assume that you've looked through some
"tiling window manager" videos on Youtube, because that's where the rabbit hole
starts. You can pick any window managers you want, but I'm going to use Qtile
as a first tiling window manager because that's what I started with. This is
basically a description of how I made my desktop environment from scratch.

# Arch installation

The starting point of this guide is right after a complete clean Arch based
distro installation. The
**[Arch Wiki](https://wiki.archlinux.org/index.php/Installation_guide)**
doesn't tell you what to do after setting the root password, it suggests installing
a bootloader, but before that I would make sure to have working internet:

```bash
pacman -S networkmanager
systemctl enable NetworkManager
```

Now you can install a bootloader and test it "safely", this is how to do it on
modern hardware,
[assuming you've mounted the efi partition on /boot](https://wiki.archlinux.org/index.php/Installation_guide#Example_layouts):

```bash
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot
os-prober
grub-mkconfig -o /boot/grub/grub.cfg
```

Now you can create your user:

```bash
useradd -m username
passwd username
usermod -aG wheel,video,audio,storage username
```

In order to have root privileges we need sudo:

```bash
pacman -S sudo
```

Edit **/etc/sudoers** with nano or vim by uncommenting this line:

```bash
## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL) ALL
```

Now you can reboot:

```bash
# Exit out of ISO image, unmount it and remove it
exit
umount -R /mnt
reboot
```

After logging in, your internet should be working just fine, but that's only if
your computer is plugged in. If you're on a laptop with no Ethernet ports, you
might have used **[iwctl](https://wiki.archlinux.org/index.php/Iwd#iwctl)**
during installation, but that program is not available anymore unless you have
installed it explicitly. However, we've installed
**[NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager)**,
so no problem, this is how you connect to a wireless LAN with this software:

```bash
# List all available networks
nmcli device wifi list
# Connect to your network
nmcli device wifi connect YOUR_SSID password YOUR_PASSWORD
```

Check [this page](https://wiki.archlinux.org/index.php/NetworkManager#nmcli_examples)
for other options provided by _nmcli_. The last thing we need to do before
thinking about desktop environments is installing **[Xorg](https://wiki.archlinux.org/index.php/Xorg)**:

```bash
sudo pacman -S xorg
```

# Login and window manager

First, we need to be able to login and open some programs like a browser and a
terminal, so we'll start by installing **[lighdm](https://wiki.archlinux.org/index.php/LightDM)**
and **[qtile](https://wiki.archlinux.org/index.php/Qtile)**. Lightdm will not
work unless we install a **[greeter](https://wiki.archlinux.org/index.php/LightDM#Greeter)**.
We also need
**[xterm](https://wiki.archlinux.org/index.php/Xterm)** because that's the
terminal emulator qtile will open by default, until we change the config file.
Then, a text editor is necessary for editing config files, you can use
**[vscode](https://wiki.archlinux.org/index.php/Visual_Studio_Code)** or jump
straight into **[neovim](https://wiki.archlinux.org/index.php/Neovim)** if you
have previous experience, otherwise I wouldn't suggest it. Last but not least,
we need a browser.

```bash
sudo pacman -S git lightdm lightdm-gtk-greeter qtile xterm code firefox
```

Enable _lightdm_ service and restart your computer, you should be able to log into
Qtile through _lightdm_.

```bash
sudo systemctl enable lightdm
reboot
```

# Fast configuration

## Qtile basic things

Now that you're in Qtile, you should know some of the default keybindings.

| Key                  | Action                     |
| -------------------- | -------------------------- |
| **mod + return**     | launch xterm               |
| **mod + k**          | next window                |
| **mod + j**          | previous window            |
| **mod + w**          | kill window                |
| **mod + [asdfuiop]** | go to workspace [asdfuiop] |
| **mod + ctrl + r**   | restart qtile              |
| **mod + ctrl + q**   | logout                     |

Before doing anything else, if you don't have a US keyboard, you should
change it using _setxkbmap_. To open xterm use **mod + return**. For example to
change your layout to latam:

```bash
setxkbmap latam
```

Note that this change is not permanent, if you reboot you have to type that
command again. See [this section](#xprofile) for making it permanent, or
follow the natural order of this guide if you have enough time.

## Load system config

First, we need to open a terminal for download this github [repo](https://github.com/IsaiasGC/dotfiles), you could clone this repo in `Document` dir. For example:

```bash
cd Documents
git clone https://github.com/IsaiasGC/dotfiles
```

Now we need install all the needed packages, those package are declared in the `.pkgs` file. For install it we need run:

```bash
cd dotfiles
sudo pacman -S --needed - < list.pkgs
yay -S --needed - < aurlist.pkgs
```

Note: for aur packages, we need download and install [`yay`](#add-support-for-aur-packages).

Then you need copy all config file to your home directory, this directory generally is `/home/username` or you will be declare the home path as `~` character. Well for copy the files we need run a comand like this:

```bash
copy .config ~
copy .local ~
copy .bashrc ~
copy .tmux.conf.local ~
copy .vimrc ~
copy .xprofile ~
copy .Xresources ~
copy picom.conf ~
```

As last step, we need reboot the system for load the actual config.

```bash
reboot
```

That's it for Qtile, now you can start hacking on it and make it your own.

# Extra

- ## Add support for AUR packages

We need install some tools like `yay` for install packages from github.
```bash
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```
